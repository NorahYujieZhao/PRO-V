
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''Initialize state variables'''
        pass  # No state initialization needed as state is provided as input
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''Process inputs and generate outputs'''
        next_state_list = []
        out1_list = []
        out2_list = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs to integers
            in_val = int(stimulus['in'])
            state_val = int(stimulus['state'], 2)  # Convert binary string to int
            
            # Initialize next state
            next_state = 0
            
            # Calculate next state based on current state and input
            if state_val & 0b0000000001:  # S0
                next_state = 0b0000000010 if in_val else 0b0000000001
            elif state_val & 0b0000000010:  # S1
                next_state = 0b0000000100 if in_val else 0b0000000001
            elif state_val & 0b0000000100:  # S2
                next_state = 0b0000001000 if in_val else 0b0000000001
            elif state_val & 0b0000001000:  # S3
                next_state = 0b0000010000 if in_val else 0b0000000001
            elif state_val & 0b0000010000:  # S4
                next_state = 0b0000100000 if in_val else 0b0000000001
            elif state_val & 0b0000100000:  # S5
                next_state = 0b0001000000 if in_val else 0b0100000000
            elif state_val & 0b0001000000:  # S6
                next_state = 0b0010000000 if in_val else 0b1000000000
            elif state_val & 0b0010000000:  # S7
                next_state = 0b0010000000 if in_val else 0b0000000001
            elif state_val & 0b0100000000:  # S8
                next_state = 0b0000000010 if in_val else 0b0000000001
            elif state_val & 0b1000000000:  # S9
                next_state = 0b0000000010 if in_val else 0b0000000001
            
            # Calculate outputs
            out1 = 1 if (state_val & 0b1100000000) else 0  # S8 or S9
            out2 = 1 if (state_val & 0b1010000000) else 0  # S7 or S9
            
            # Convert next_state to binary string
            next_state_bin = format(next_state, '010b')
            
            # Append results
            next_state_list.append(next_state_bin)
            out1_list.append(out1)
            out2_list.append(out2)
        
        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': [
                {
                    'next_state': ns,
                    'out1': o1,
                    'out2': o2
                }
                for ns, o1, o2 in zip(next_state_list, out1_list, out2_list)
            ]
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

