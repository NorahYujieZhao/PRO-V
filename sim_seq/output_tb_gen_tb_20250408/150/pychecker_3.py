
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        self.state = 'WALK_LEFT'  # Initial state
        self.fall_counter = 0      # Counter for fall duration
        self.last_walk_dir = 'LEFT' # Remember direction before fall/dig

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert inputs from binary strings to integers
        areset = int(stimulus_dict['areset'], 2)
        bump_left = int(stimulus_dict['bump_left'], 2)
        bump_right = int(stimulus_dict['bump_right'], 2)
        ground = int(stimulus_dict['ground'], 2)
        dig = int(stimulus_dict['dig'], 2)

        # Initialize outputs
        walk_left = walk_right = aaah = digging = 0

        # Handle asynchronous reset
        if areset == 1:
            self.state = 'WALK_LEFT'
            self.fall_counter = 0
            self.last_walk_dir = 'LEFT'
        elif clk == 1:  # State transitions on clock edge
            if self.state == 'SPLAT':
                pass  # Stay in splat state forever
            elif ground == 0 and self.state != 'FALLING':  # Start falling
                if self.state in ['WALK_LEFT', 'WALK_RIGHT']:
                    self.last_walk_dir = 'LEFT' if self.state == 'WALK_LEFT' else 'RIGHT'
                self.state = 'FALLING'
                self.fall_counter = 0
            elif self.state == 'FALLING':
                if ground == 1:  # Landing
                    if self.fall_counter > 20:
                        self.state = 'SPLAT'
                    else:
                        self.state = 'WALK_LEFT' if self.last_walk_dir == 'LEFT' else 'WALK_RIGHT'
                else:  # Continue falling
                    self.fall_counter += 1
            elif self.state in ['WALK_LEFT', 'WALK_RIGHT']:
                if dig == 1 and ground == 1:
                    self.state = 'DIGGING'
                    self.last_walk_dir = 'LEFT' if self.state == 'WALK_LEFT' else 'RIGHT'
                elif bump_left == 1 and self.state == 'WALK_LEFT':
                    self.state = 'WALK_RIGHT'
                elif bump_right == 1 and self.state == 'WALK_RIGHT':
                    self.state = 'WALK_LEFT'
            elif self.state == 'DIGGING' and ground == 0:
                self.state = 'FALLING'
                self.fall_counter = 0

        # Set outputs based on current state
        if self.state == 'WALK_LEFT':
            walk_left = 1
        elif self.state == 'WALK_RIGHT':
            walk_right = 1
        elif self.state == 'FALLING':
            aaah = 1
        elif self.state == 'DIGGING':
            digging = 1

        # Convert outputs to binary strings
        return {
            'walk_left': format(walk_left, 'b'),
            'walk_right': format(walk_right, 'b'),
            'aaah': format(aaah, 'b'),
            'digging': format(digging, 'b')
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


