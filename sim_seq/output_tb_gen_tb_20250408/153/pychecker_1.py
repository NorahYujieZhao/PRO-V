
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Initialize state variables
        self.direction_left = 1  # 1 = walking left, 0 = walking right
        self.falling = 0
        self.is_digging = 0
        self.prev_ground = 1

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert inputs from binary strings to integers
        areset = int(stimulus_dict.get('areset', '0'), 2)
        bump_left = int(stimulus_dict.get('bump_left', '0'), 2)
        bump_right = int(stimulus_dict.get('bump_right', '0'), 2)
        ground = int(stimulus_dict.get('ground', '0'), 2)
        dig = int(stimulus_dict.get('dig', '0'), 2)

        # Asynchronous reset
        if areset:
            self.direction_left = 1
            self.falling = 0
            self.is_digging = 0
            self.prev_ground = 1
        elif clk == 1:  # Rising edge
            # Check for falling (highest priority)
            if not ground:
                self.falling = 1
                self.is_digging = 0
            elif self.falling:
                self.falling = 0
                # Keep previous direction after falling

            # Check for digging (second priority)
            elif dig and ground and not self.falling:
                self.is_digging = 1
            elif self.is_digging and not ground:
                self.is_digging = 0
                self.falling = 1

            # Direction changes (lowest priority)
            elif not self.falling and not self.is_digging:
                if bump_left:
                    self.direction_left = 0
                elif bump_right:
                    self.direction_left = 1

            self.prev_ground = ground

        # Prepare outputs
        walk_left = '1' if self.direction_left and not self.falling and not self.is_digging else '0'
        walk_right = '1' if not self.direction_left and not self.falling and not self.is_digging else '0'
        aaah = '1' if self.falling else '0'
        digging = '1' if self.is_digging else '0'

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


