
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational circuit, so no state initialization needed.
        '''
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process input stimuli and compute logic gate outputs
        '''
        output_list = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input strings to integers
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            
            # Compute all logic operations
            out_and = a & b
            out_or = a | b
            out_xor = a ^ b
            out_nand = 1 if (a & b) == 0 else 0
            out_nor = 1 if (a | b) == 0 else 0
            out_xnor = 1 if (a ^ b) == 0 else 0
            out_anotb = a & (1 if b == 0 else 0)
            
            # Create output dictionary for this stimulus
            output_dict = {
                'out_and': str(out_and),
                'out_or': str(out_or),
                'out_xor': str(out_xor),
                'out_nand': str(out_nand),
                'out_nor': str(out_nor),
                'out_xnor': str(out_xnor),
                'out_anotb': str(out_anotb)
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

