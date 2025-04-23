
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        Each internal register/state variable must align with the module header.
        Explicitly initialize these states according to the RTL specification.
        '''
        # No internal state needed - combinational logic only
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process inputs and generate outputs according to state machine logic
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs to integers
            in_val = int(stimulus['in'])
            state = int(stimulus['state'], 2)  # Convert binary string to int
            
            # Calculate next state based on current state and input
            next_state = 0
            if state == 0b0001:  # State A
                next_state = 0b0001 if in_val == 0 else 0b0010
            elif state == 0b0010:  # State B
                next_state = 0b0100 if in_val == 0 else 0b0010
            elif state == 0b0100:  # State C
                next_state = 0b0001 if in_val == 0 else 0b1000
            elif state == 0b1000:  # State D
                next_state = 0b0100 if in_val == 0 else 0b0010
            
            # Output is 1 only in state D
            out = 1 if state == 0b1000 else 0
            
            # Format outputs as dictionary
            output = {
                'next_state': format(next_state, '04b'),
                'out': str(out)
            }
            outputs.append(output)
        
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

