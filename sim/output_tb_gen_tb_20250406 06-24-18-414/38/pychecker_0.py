
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is combinational logic, so no state initialization needed.
        '''
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process scancode input and determine which arrow key (if any) was pressed.
        Returns dictionary with output signals for left, down, right, and up arrows.
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert scancode string to integer
            scancode = int(stimulus['scancode'], 2)
            
            # Initialize all outputs to 0
            left = down = right = up = 0
            
            # Check scancode against predefined values
            if scancode == 0xe06b:  # left arrow
                left = 1
            elif scancode == 0xe072:  # down arrow
                down = 1
            elif scancode == 0xe074:  # right arrow
                right = 1
            elif scancode == 0xe075:  # up arrow
                up = 1
            
            # Add outputs to result list
            outputs.append({
                'left': str(left),
                'down': str(down),
                'right': str(right),
                'up': str(up)
            })
        
        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': outputs
        }
def check_output(stimulus_list):

    dut = GoldenDUT()
    tb_outputs = []


    for stimulus in stimulus_list:

        tb_outputs.append(dut.load(stimulus))

    return tb_outputs

if __name__ == "__main__":

    with open("stimulus.json", "r") as f:
        stimulus_data = json.load(f)


    if isinstance(stimulus_data, dict):
        stimulus_list = stimulus_data.get("input variable", [])
    else:
        stimulus_list = stimulus_data



    outputs = check_output(stimulus_list)

    print(json.dumps(outputs, indent=2))

