
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational circuit, so no state registers needed.
        '''
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process inputs and generate outputs according to RTL specification.
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input binary strings to integers
            a = int(stimulus['a'], 2)
            b = int(stimulus['b'], 2)
            
            # Compute bitwise-OR
            out_or_bitwise = a | b
            
            # Compute logical-OR
            out_or_logical = 1 if (a or b) else 0
            
            # Compute NOT
            # For 3-bit values, use mask 0b111 = 7
            not_a = (~a) & 0b111
            not_b = (~b) & 0b111
            # Place not_b in upper half (bits [5:3]) and not_a in lower half
            out_not = (not_b << 3) | not_a
            
            # Format outputs as binary strings
            output_dict = {
                'out_or_bitwise': format(out_or_bitwise, '03b'),
                'out_or_logical': format(out_or_logical, '01b'),
                'out_not': format(out_not, '06b')
            }
            
            outputs.append(output_dict)
        
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

