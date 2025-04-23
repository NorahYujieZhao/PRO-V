
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
        Process input stimuli and generate corresponding outputs.
        '''
        output_list = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input binary string to integer
            vec = int(stimulus['vec'], 2)
            
            # Output is same as input vector
            outv = vec
            
            # Extract individual bits
            o2 = (vec >> 2) & 1
            o1 = (vec >> 1) & 1
            o0 = vec & 1
            
            # Create output dictionary for this stimulus
            output_dict = {
                'outv': format(outv, '03b'),
                'o2': format(o2, 'b'),
                'o1': format(o1, 'b'),
                'o0': format(o0, 'b')
            }
            output_list.append(output_dict)
        
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

