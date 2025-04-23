
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        No state registers needed for this combinational logic.
        '''
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Count number of 1s in 255-bit input vector.
        Returns 8-bit output representing the count.
        '''
        stimulus_outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Get input vector as string and convert to integer
            in_vector = int(stimulus['in'], 2)
            
            # Count number of 1s in binary representation
            ones_count = bin(in_vector).count('1')
            
            # Format as 8-bit binary string without '0b' prefix
            out_binary = format(ones_count, '08b')
            
            stimulus_outputs.append({'out': out_binary})
        
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

