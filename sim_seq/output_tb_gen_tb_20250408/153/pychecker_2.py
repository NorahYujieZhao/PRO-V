
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        self.walking_left = 1  # Start walking left
        self.is_falling = 0
        self.is_digging = 0
        self.prev_direction_left = 1  # Store direction before falling

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        # Convert inputs from binary strings to integers
        areset = int(stimulus_dict.get('areset', '0'), 2)
        bump_left = int(stimulus_dict.get('bump_left', '0'), 2)
        bump_right = int(stimulus_dict.get('bump_right', '0'), 2)
        ground = int(stimulus_dict.get('ground', '0'), 2)
        dig = int(stimulus_dict.get('dig', '0'), 2)

        # Handle asynchronous reset
        if areset:
            self.walking_left = 1
            self.is_falling = 0
            self.is_digging = 0
            self.prev_direction_left = 1
        elif clk:
            # Update state on rising clock edge
            if not ground:
                # Falling has highest priority
                if not self.is_falling:
                    # Start falling - save direction
                    self.prev_direction_left = self.walking_left
                self.is_falling = 1
                self.is_digging = 0
            else:
                # Ground present
                if self.is_falling:
                    # Just landed - restore previous direction
                    self.walking_left = self.prev_direction_left
                    self.is_falling = 0
                elif dig and not self.is_digging and not self.is_falling:
                    # Start digging if on ground and not already digging/falling
                    self.is_digging = 1
                elif not self.is_digging:
                    # Handle direction changes if not digging
                    if bump_left:
                        self.walking_left = 0
                    elif bump_right:
                        self.walking_left = 1

        # Prepare outputs
        return {
            'walk_left': format(self.walking_left, 'b'),
            'walk_right': format(1 - self.walking_left, 'b'),
            'aaah': format(self.is_falling, 'b'),
            'digging': format(self.is_digging, 'b')
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


