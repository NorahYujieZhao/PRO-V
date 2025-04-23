
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
        Process input stimuli and generate outputs according to the specification.
        '''
        # Initialize output list
        z_outputs = []
        
        # Process each input stimulus
        for stimulus in stimulus_dict['input variable']:
            # Convert input strings to integers
            x = int(stimulus['x'])
            y = int(stimulus['y'])
            
            # Implement the logic: z = (NOT x AND NOT y) OR (x AND y)
            z = (not x and not y) or (x and y)
            
            # Convert boolean result to integer
            z_int = 1 if z else 0
            
            # Add to output list
            z_outputs.append({'z': str(z_int)})
        
        # Format output dictionary
        output_dict = {
            'scenario': stimulus_dict['scenario'],
            'output variable': z_outputs
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

