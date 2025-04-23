
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational circuit with no state.
        '''
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Reverse the bits of an 8-bit input vector.
        '''
        stimulus_outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Get input value and convert to integer
            in_val = int(stimulus['in'], 2)
            
            # Reverse the bits
            out_val = 0
            for i in range(8):
                # Extract bit i from input
                bit = (in_val >> i) & 1
                # Place it at position 7-i in output
                out_val |= (bit << (7-i))
            
            # Format output as 8-bit binary string
            out_str = format(out_val, '08b')
            
            # Add to output list
            stimulus_outputs.append({'out': out_str})
        
        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': stimulus_outputs
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

