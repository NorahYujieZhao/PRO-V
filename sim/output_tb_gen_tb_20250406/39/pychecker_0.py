
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        No state registers needed for combinational adder.
        '''
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process input stimuli and compute sum with overflow.
        Returns dictionary with sum results.
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert binary string inputs to integers
            x = int(stimulus['x'], 2)
            y = int(stimulus['y'], 2)
            
            # Perform addition
            sum_result = x + y
            
            # Mask to 5 bits to handle overflow
            sum_result = sum_result & 0x1F
            
            # Convert to 5-bit binary string
            sum_binary = format(sum_result, '05b')
            
            # Add result to outputs
            outputs.append({'sum': sum_binary})
        
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

