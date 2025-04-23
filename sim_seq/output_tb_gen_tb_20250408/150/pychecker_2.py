
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Initialize state variables
        self.walking_left = True  # Start walking left
        self.falling = False
        self.digging = False
        self.splattered = False
        self.fall_counter = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        # Convert inputs from binary strings to integers
        areset = int(stimulus_dict.get('areset', '0'), 2)
        bump_left = int(stimulus_dict.get('bump_left', '0'), 2)
        bump_right = int(stimulus_dict.get('bump_right', '0'), 2)
        ground = int(stimulus_dict.get('ground', '0'), 2)
        dig = int(stimulus_dict.get('dig', '0'), 2)

        # Handle asynchronous reset
        if areset:
            self.walking_left = True
            self.falling = False
            self.digging = False
            self.splattered = False
            self.fall_counter = 0
        elif clk and not self.splattered:  # Only update if not splattered
            # Check for falling
            if not ground:
                if not self.falling:  # Start falling
                    self.falling = True
                    self.digging = False
                if self.falling:  # Update fall counter
                    self.fall_counter += 1
            else:  # On ground
                if self.falling:  # Landing
                    self.falling = False
                    if self.fall_counter > 20:  # Splatter check
                        self.splattered = True
                    self.fall_counter = 0
                elif dig and not self.digging:  # Start digging
                    self.digging = True
                elif not self.digging:  # Handle direction changes
                    if bump_left and not bump_right:
                        self.walking_left = False
                    elif bump_right and not bump_left:
                        self.walking_left = True
                    elif bump_left and bump_right:
                        self.walking_left = not self.walking_left

        # Prepare outputs
        walk_left = '1' if self.walking_left and not (self.falling or self.digging or self.splattered) else '0'
        walk_right = '1' if not self.walking_left and not (self.falling or self.digging or self.splattered) else '0'
        aaah = '1' if self.falling and not self.splattered else '0'
        digging = '1' if self.digging and not self.splattered else '0'

        return {
            'walk_left': walk_left,
            'walk_right': walk_right,
            'aaah': aaah,
            'digging': digging
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


