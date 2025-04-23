
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
        Process input stimuli and generate outputs for the 4-input AND, OR, XOR gates.
        '''
        output_list = []

        for stimulus in stimulus_dict['input variable']:
            # Convert binary string input to integer
            in_val = int(stimulus['in'], 2)
            
            # Calculate outputs
            # AND: All bits must be 1
            out_and = 1 if in_val == 0b1111 else 0
            
            # OR: At least one bit must be 1
            out_or = 1 if in_val > 0 else 0
            
            # XOR: Count number of 1s, result is 1 if odd number of 1s
            out_xor = bin(in_val).count('1') % 2
            
            # Add results to output list
            output_list.append({
                'out_and': str(out_and),
                'out_or': str(out_or),
                'out_xor': str(out_xor)
            })

        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': output_list
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

