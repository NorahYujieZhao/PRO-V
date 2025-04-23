
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 4-bit shift register to 0
        '''
        self.q = 0  # 4-bit register

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Handle shift register logic with asynchronous reset
        '''
        # Convert input binary strings to integers
        areset_val = int(stimulus_dict['areset'], 2)
        load_val = int(stimulus_dict['load'], 2)
        ena_val = int(stimulus_dict['ena'], 2)
        data_val = int(stimulus_dict['data'], 2)

        # Handle asynchronous reset
        if areset_val == 1:
            self.q = 0
        # On clock edge
        elif clk == 1:
            if load_val == 1:  # Load has priority
                self.q = data_val & 0xF  # Mask to 4 bits
            elif ena_val == 1:  # Shift right if enabled
                self.q = (self.q >> 1) & 0xF  # Right shift and mask

        # Convert output to 4-bit binary string
        q_str = format(self.q, '04b')
        
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


