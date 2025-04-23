
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize internal state registers.
        Default state is walk_left (1,0)
        '''
        self.walking_left = 1  # Start walking left

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        # Convert input binary strings to integers
        areset = int(stimulus_dict['areset'], 2)
        bump_left = int(stimulus_dict['bump_left'], 2)
        bump_right = int(stimulus_dict['bump_right'], 2)

        # Handle asynchronous reset
        if areset:
            self.walking_left = 1
        # State transitions on clock edge
        elif clk == 1:
            if bump_left or bump_right:
                self.walking_left = not self.walking_left

        # Generate outputs based on current state
        walk_left = '1' if self.walking_left else '0'
        walk_right = '0' if self.walking_left else '1'

        return {
            'walk_left': walk_left,
            'walk_right': walk_right
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


