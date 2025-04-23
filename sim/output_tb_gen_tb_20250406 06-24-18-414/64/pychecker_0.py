
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational circuit, so no state registers are needed.
        '''
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Count number of 1's in 3-bit input vector and output 2-bit result
        '''
        stimulus_outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input string to integer
            in_val = int(stimulus['in'], 2)
            
            # Count number of 1's in binary representation
            ones_count = bin(in_val).count('1')
            
            # Format output as 2-bit binary string
            out_val = format(ones_count, '02b')
            
            # Add to output list
            stimulus_outputs.append({'out': out_val})
        
        output_dict = {
            'scenario': stimulus_dict['scenario'],
            'output variable': stimulus_outputs
        }
        
        return output_dict
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

