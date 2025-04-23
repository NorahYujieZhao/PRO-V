
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
        Process input stimuli and compute outputs according to the XNOR-XOR logic.
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input strings to integers
            in1 = int(stimulus['in1'])
            in2 = int(stimulus['in2'])
            in3 = int(stimulus['in3'])
            
            # Calculate XNOR of in1 and in2
            xnor_result = 1 if in1 == in2 else 0
            
            # Calculate XOR of XNOR result and in3
            out = 1 if xnor_result != in3 else 0
            
            # Add result to outputs list
            outputs.append({'out': str(out)})
        
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

