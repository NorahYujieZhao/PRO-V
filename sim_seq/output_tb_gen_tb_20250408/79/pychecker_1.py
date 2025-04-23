
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 3-bit counter state
        '''
        self.q = 0  # 3-bit counter

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''
        Update counter state based on input a
        '''
        # Convert input a from binary string to integer
        a = int(stimulus_dict['a'], 2)
        
        # Only update on rising clock edge
        if clk == 1:
            if a == 1:
                # When a is 1, force q to 4
                self.q = 4
            else:
                # When a is 0, implement counting sequence
                if self.q == 4:
                    self.q = 5
                elif self.q == 5:
                    self.q = 6
                elif self.q == 6:
                    self.q = 0
                elif self.q < 4:
                    self.q = (self.q + 1) % 8
        
        # Convert 3-bit output to binary string
        q_str = format(self.q, '03b')
        
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


