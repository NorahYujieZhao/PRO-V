
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        Each internal register/state variable must align with the module header.
        Explicitly initialize these states according to the RTL specification.
        '''
        # This is a combinational logic circuit, no state registers needed
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        stimulus_dict: a dictionary formatted as shown above.
        Parse each input variable and use it to perform RTL state updates.
        Please note input variable is in string format and you need to convert it to the corresponding type.
        Returns a dictionary of the outputs aligned with the RTL module outputs and updated states for verification.
        '''
        # Initialize output list
        z_outputs = []
        
        # Process each stimulus input
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs to integers
            x = int(stimulus['x'])
            y = int(stimulus['y'])
            
            # Compute z = (x^y) & x
            xor_result = x ^ y  # XOR operation
            z = xor_result & x  # AND operation
            
            # Append result to output list
            z_outputs.append({'z': str(z)})
        
        # Create output dictionary
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

