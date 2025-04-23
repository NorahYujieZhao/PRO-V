
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # State constants
        self.WALKING = 0
        self.FALLING = 1
        self.DIGGING = 2
        self.SPLAT = 3
        
        # Initialize state variables
        self.state = self.WALKING
        self.walking_left = True  # True for left, False for right
        self.fall_counter = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert inputs from binary strings to integers
        areset = int(stimulus_dict['areset'], 2)
        bump_left = int(stimulus_dict['bump_left'], 2)
        bump_right = int(stimulus_dict['bump_right'], 2)
        ground = int(stimulus_dict['ground'], 2)
        dig = int(stimulus_dict['dig'], 2)

        # Handle asynchronous reset
        if areset:
            self.state = self.WALKING
            self.walking_left = True
            self.fall_counter = 0
            return {'walk_left': '1', 'walk_right': '0', 'aaah': '0', 'digging': '0'}

        # State updates on clock edge
        if clk == 1:
            if self.state == self.SPLAT:
                # Stay in splat state forever
                pass
            elif not ground:
                # Falling has highest priority
                if self.state != self.FALLING:
                    self.state = self.FALLING
                    self.fall_counter = 0
                else:
                    self.fall_counter += 1
            elif self.state == self.FALLING:
                # Landing after fall
                if self.fall_counter > 20:
                    self.state = self.SPLAT
                else:
                    self.state = self.WALKING
            elif dig and ground and self.state == self.WALKING:
                # Start digging if on ground
                self.state = self.DIGGING
            elif self.state == self.DIGGING and not ground:
                # Fall after digging through
                self.state = self.FALLING
                self.fall_counter = 0
            elif self.state == self.WALKING:
                # Handle direction changes
                if bump_left and not bump_right:
                    self.walking_left = False
                elif bump_right and not bump_left:
                    self.walking_left = False
                elif bump_left and bump_right:
                    self.walking_left = not self.walking_left

        # Generate outputs based on current state
        walk_left = '1' if self.state == self.WALKING and self.walking_left else '0'
        walk_right = '1' if self.state == self.WALKING and not self.walking_left else '0'
        aaah = '1' if self.state == self.FALLING else '0'
        digging = '1' if self.state == self.DIGGING else '0'

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


