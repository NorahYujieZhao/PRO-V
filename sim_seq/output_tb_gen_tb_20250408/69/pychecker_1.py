
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state variables
        '''
        self.current_state = 0  # 3-bit state initialized to 000

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        # Convert input signals from binary strings to integers
        x = int(stimulus_dict['x'], 2)
        y = int(stimulus_dict['y'], 2)
        
        # Update current state on rising edge
        if clk == 1:
            self.current_state = y
            
        # Determine Y0 (LSB of next state) based on current state and input x
        Y0 = 0
        if self.current_state == 0:  # 000
            Y0 = 1 if x else 0
        elif self.current_state == 1:  # 001
            Y0 = 0 if x else 1
        elif self.current_state == 2:  # 010
            Y0 = 1 if x else 0
        elif self.current_state == 3:  # 011
            Y0 = 0 if x else 1
        elif self.current_state == 4:  # 100
            Y0 = 0 if x else 1
            
        # Determine output z based on current state
        z = 1 if self.current_state in [3, 4] else 0
        
        # Convert outputs to binary strings
        return {
            'Y0': format(Y0, 'b'),
            'z': format(z, 'b')
        }
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


