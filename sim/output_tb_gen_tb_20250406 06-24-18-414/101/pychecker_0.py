
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        Each internal register/state variable must align with the module header.
        Explicitly initialize these states according to the RTL specification.
        '''
        # This module implements combinational logic only
        # No internal state registers needed
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process input stimuli and compute next state and output
        '''
        next_state_list = []
        out_list = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs from strings to integers
            in_val = int(stimulus['in'])
            state = int(stimulus['state'], 2)  # Convert binary string to int
            
            # Compute next state based on current state and input
            if state == 0:  # State A
                next_state = 0 if in_val == 0 else 1  # A->A or A->B
            elif state == 1:  # State B
                next_state = 2 if in_val == 0 else 1  # B->C or B->B
            elif state == 2:  # State C
                next_state = 0 if in_val == 0 else 3  # C->A or C->D
            else:  # State D
                next_state = 2 if in_val == 0 else 1  # D->C or D->B
            
            # Compute output (1 only in state D)
            out = 1 if state == 3 else 0
            
            # Format next_state as 2-bit binary string
            next_state_bin = format(next_state, '02b')
            
            next_state_list.append(next_state_bin)
            out_list.append(str(out))
        
        return {
            "scenario": stimulus_dict['scenario'],
            "output variable": [
                {"next_state": ns, "out": o}
                for ns, o in zip(next_state_list, out_list)
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

