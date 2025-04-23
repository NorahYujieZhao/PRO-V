
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state machine registers
        States: WALK_LEFT=0, WALK_RIGHT=1, FALL_LEFT=2, FALL_RIGHT=3
        '''
        self.state = 0  # Initial state is WALK_LEFT
        self.walk_left = 1
        self.walk_right = 0
        self.aaah = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state machine based on inputs
        '''
        # Convert inputs from binary strings to integers
        areset = int(stimulus_dict['areset'], 2)
        bump_left = int(stimulus_dict['bump_left'], 2)
        bump_right = int(stimulus_dict['bump_right'], 2)
        ground = int(stimulus_dict['ground'], 2)

        # Handle asynchronous reset
        if areset == 1:
            self.state = 0  # WALK_LEFT
        # Process on rising clock edge
        elif clk == 1:
            if ground == 0:  # Start falling
                if self.state == 0 or self.state == 2:  # Was going left
                    self.state = 2  # FALL_LEFT
                else:  # Was going right
                    self.state = 3  # FALL_RIGHT
            else:  # Ground present
                if self.state == 2:  # Was falling left
                    self.state = 0  # Resume WALK_LEFT
                elif self.state == 3:  # Was falling right
                    self.state = 1  # Resume WALK_RIGHT
                else:  # Walking - check bumps
                    if bump_left == 1:
                        self.state = 1  # WALK_RIGHT
                    elif bump_right == 1:
                        self.state = 0  # WALK_LEFT

        # Update outputs based on state
        self.walk_left = 1 if self.state == 0 else 0
        self.walk_right = 1 if self.state == 1 else 0
        self.aaah = 1 if self.state in [2, 3] else 0

        # Return outputs as binary strings
        return {
            'walk_left': format(self.walk_left, 'b'),
            'walk_right': format(self.walk_right, 'b'),
            'aaah': format(self.aaah, 'b')
        }
def check_output(stimulus_list_scenario):

    dut = GoldenDUT()
    tb_outputs = []


    for stimulus_list in stimulus_list_scenario["input variable"]:


        clock_cycles = stimulus_list['clock cycles']
        
        input_vars_list = {k: v for k, v in stimulus_list.items() if k != "clock cycles"}
        output_vars_list = {'clock cycles':clock_cycles}
        for k,v in input_vars_list.items():
            if len(v) < clock_cycles:
                v.extend([v[-1]] * (clock_cycles - len(v)))
                
        

        for i in range(clock_cycles):
            input_vars = {k:v[i] for k,v in input_vars_list.items()}
            
            clk= 0
            output_vars = dut.load(clk,input_vars)
            clk = 1
            output_vars = dut.load(clk,input_vars)
            for k,v in output_vars.items():
                if k not in output_vars_list:
                    output_vars_list[k] = []
                output_vars_list[k].append(v)
            


        tb_outputs.append(output_vars_list)

    return tb_outputs

if __name__ == "__main__":
    stimulus_file_name = "stimulus.json"
    with open(stimulus_file_name, "r") as f:
        stimulus_data = json.load(f)


    if isinstance(stimulus_data, dict):
        stimulus_list_scenarios = stimulus_data.get("input variable", [])
    else:
        stimulus_list_scenarios = stimulus_data

    outputs=[]
    for stimulus_list_scenario in stimulus_list_scenarios:
        outputs.append( check_output(stimulus_list_scenario))
    with open(stimulus_file_name, "w") as f:
        json.dump(stimulus_list_scenarios, f, indent=4)

    print(json.dumps(outputs, indent=2))



