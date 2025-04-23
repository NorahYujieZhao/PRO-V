
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
        Process inputs and generate outputs according to AND gate functionality
        '''
        # Initialize output lists
        out_assign_list = []
        out_alwaysblock_list = []
        
        # Process each stimulus
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs to integers
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            
            # Compute AND operation
            result = a & b
            
            # Both outputs implement the same AND gate
            out_assign_list.append(result)
            out_alwaysblock_list.append(result)
        
        # Format output dictionary
        output_dict = {
            "scenario": stimulus_dict['scenario'],
            "output variable": [
                {"out_assign": str(val),
                 "out_alwaysblock": str(val)} for val in out_assign_list
            ]
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

