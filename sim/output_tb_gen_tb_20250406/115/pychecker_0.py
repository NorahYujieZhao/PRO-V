
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This module is combinational, so no state registers needed.
        '''
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process input stimuli and return minimum value output
        '''
        output_list = []

        for stimulus in stimulus_dict['input variable']:
            # Convert binary strings to integers
            a = int(stimulus['a'], 2)
            b = int(stimulus['b'], 2)
            c = int(stimulus['c'], 2)
            d = int(stimulus['d'], 2)
            
            # Find minimum value
            min_val = min(a, b, c, d)
            
            # Convert back to 8-bit binary string
            min_bin = format(min_val, '08b')
            
            # Add to output list
            output_list.append({'min': min_bin})

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

