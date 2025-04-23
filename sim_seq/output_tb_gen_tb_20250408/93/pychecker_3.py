
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the counter to 0
        '''
        self.counter = 0  # 4-bit counter initialized to 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert reset input from binary string to integer
        reset_val = int(stimulus_dict['reset'], 2)

        # Only update on rising clock edge
        if clk == 1:
            if reset_val == 1:
                # Synchronous reset
                self.counter = 0
            else:
                # Increment counter if less than 9, wrap to 0 if at 9
                if self.counter == 9:
                    self.counter = 0
                else:
                    self.counter = (self.counter + 1) & 0xF  # Mask to 4 bits

        # Format output as 4-bit binary string
        q_str = format(self.counter, '04b')
        
        return {'q': q_str}
def check_output(stimulus_list_scenario):

    dut = GoldenDUT()
    tb_outputs = []


    for stimulus_list in stimulus_list_scenario["input variable"]:


        clock_cycles = stimulus_list['clock cycles']
        clk = 1
        input_vars_list = {k: v for k, v in stimulus_list.items() if k != "clock cycles"}
        output_vars_list = {'clock cycles':clock_cycles}

        for i in range(clock_cycles):
            input_vars = {k:v[i] for k,v in input_vars_list.items()}

            output_vars = dut.load(clk,input_vars)
            for k,v in output_vars.items():
                if k not in output_vars_list:
                    output_vars_list[k] = []
                output_vars_list[k].append(v)
            


        tb_outputs.append(output_vars_list)

    return tb_outputs

if __name__ == "__main__":

    with open("stimulus.json", "r") as f:
        stimulus_data = json.load(f)


    if isinstance(stimulus_data, dict):
        stimulus_list_scenarios = stimulus_data.get("input variable", [])
    else:
        stimulus_list_scenarios = stimulus_data

    outputs=[]
    for stimulus_list_scenario in stimulus_list_scenarios:
        outputs.append( check_output(stimulus_list_scenario))

    print(json.dumps(outputs, indent=2))


