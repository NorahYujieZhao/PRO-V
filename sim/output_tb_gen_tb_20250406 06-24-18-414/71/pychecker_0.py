
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        Each internal register/state variable must align with the module header.
        Explicitly initialize these states according to the RTL specification.
        '''
        # No state registers needed for this design
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        stimulus_dict: a dictionary formatted as shown above.
        Parse each input variable and use it to perform RTL state updates.
        Returns a dictionary of the outputs aligned with the RTL module outputs.
        '''
        output_list = []
        
        # Process each input stimulus
        for stimulus in stimulus_dict['input variable']:
            # Get input values
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            c = int(stimulus['c'])
            
            # Create output dictionary for current stimulus
            output = {
                'w': str(a),  # w = a
                'x': str(b),  # x = b
                'y': str(b),  # y = b
                'z': str(c)   # z = c
            }
            output_list.append(output)
        
        # Return formatted output dictionary
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

