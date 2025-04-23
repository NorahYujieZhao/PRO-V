
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        self.walking_left = 1  # Start walking left
        self.falling = 0
        self.digging = 0
        self.fall_duration = 0
        self.splattered = 0
        self.last_walk_dir_left = 1  # Remember direction before falling

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert inputs from binary strings to integers
        areset = int(stimulus_dict.get('areset', '0'), 2)
        bump_left = int(stimulus_dict.get('bump_left', '0'), 2)
        bump_right = int(stimulus_dict.get('bump_right', '0'), 2)
        ground = int(stimulus_dict.get('ground', '0'), 2)
        dig = int(stimulus_dict.get('dig', '0'), 2)

        # Asynchronous reset
        if areset:
            self.walking_left = 1
            self.falling = 0
            self.digging = 0
            self.fall_duration = 0
            self.splattered = 0
            self.last_walk_dir_left = 1
        elif clk and not self.splattered:  # Only update if not splattered
            # Check for falling
            if not ground:
                if not self.falling:  # Start falling
                    self.falling = 1
                    self.digging = 0
                    self.fall_duration = 0
                    self.last_walk_dir_left = self.walking_left
                self.fall_duration += 1
            else:  # On ground
                if self.falling:  # Just landed
                    self.falling = 0
                    if self.fall_duration > 20:  # Splatter condition
                        self.splattered = 1
                    else:  # Resume walking in previous direction
                        self.walking_left = self.last_walk_dir_left
                elif dig and not self.digging:  # Start digging
                    self.digging = 1
                    self.walking_left = self.last_walk_dir_left
                elif not self.digging:  # Handle direction changes
                    if bump_left:
                        self.walking_left = 0
                    elif bump_right:
                        self.walking_left = 1

        # Prepare outputs
        walk_left = '1' if self.walking_left and not self.falling and not self.digging and not self.splattered else '0'
        walk_right = '1' if not self.walking_left and not self.falling and not self.digging and not self.splattered else '0'
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


