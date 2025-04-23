
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
        Process inputs according to truth table and generate outputs.
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs to integers
            x3 = int(stimulus['x3'])
            x2 = int(stimulus['x2'])
            x1 = int(stimulus['x1'])
            
            # Implement truth table logic
            f = 1 if ((x2 == 1 and x1 == 1) or
                      (x2 == 1 and x1 == 0 and x3 == 0) or
                      (x2 == 0 and x1 == 1 and x3 == 1)) else 0
            
            outputs.append({'f': str(f)})
        
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

