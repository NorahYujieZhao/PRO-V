
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # State encoding
        self.WALK_LEFT = 0
        self.WALK_RIGHT = 1
        self.FALL_LEFT = 2
        self.FALL_RIGHT = 3
        self.DIG_LEFT = 4
        self.DIG_RIGHT = 5
        
        # Initialize state
        self.state = self.WALK_LEFT
    
    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        # Convert inputs from binary strings to integers
        areset = int(stimulus_dict.get('areset', '0'), 2)
        bump_left = int(stimulus_dict.get('bump_left', '0'), 2)
        bump_right = int(stimulus_dict.get('bump_right', '0'), 2)
        ground = int(stimulus_dict.get('ground', '0'), 2)
        dig = int(stimulus_dict.get('dig', '0'), 2)
        
        # Asynchronous reset
        if areset:
            self.state = self.WALK_LEFT
        # Synchronous state update on rising clock edge
        elif clk:
            next_state = self.state
            
            # State transition logic
            if self.state in [self.WALK_LEFT, self.WALK_RIGHT]:
                if not ground:
                    next_state = self.FALL_LEFT if self.state == self.WALK_LEFT else self.FALL_RIGHT
                elif dig:
                    next_state = self.DIG_LEFT if self.state == self.WALK_LEFT else self.DIG_RIGHT
                elif bump_left:
                    next_state = self.WALK_RIGHT
                elif bump_right:
                    next_state = self.WALK_LEFT
            
            elif self.state in [self.FALL_LEFT, self.FALL_RIGHT]:
                if ground:
                    next_state = self.WALK_LEFT if self.state == self.FALL_LEFT else self.WALK_RIGHT
            
            elif self.state in [self.DIG_LEFT, self.DIG_RIGHT]:
                if not ground:
                    next_state = self.FALL_LEFT if self.state == self.DIG_LEFT else self.FALL_RIGHT
            
            self.state = next_state
        
        # Output logic
        walk_left = '1' if self.state in [self.WALK_LEFT] else '0'
        walk_right = '1' if self.state in [self.WALK_RIGHT] else '0'
        aaah = '1' if self.state in [self.FALL_LEFT, self.FALL_RIGHT] else '0'
        digging = '1' if self.state in [self.DIG_LEFT, self.DIG_RIGHT] else '0'
        
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


