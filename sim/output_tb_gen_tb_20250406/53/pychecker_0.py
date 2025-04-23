
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        Each internal register/state variable must align with the module header.
        Explicitly initialize these states according to the RTL specification.
        '''
        # This is a combinational circuit, no state registers needed
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        stimulus_dict: a dictionary formatted as shown above.
        Parse each input variable and use it to perform RTL state updates.
        Returns a dictionary of the outputs aligned with the RTL module outputs.
        '''
        output_list = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input strings to integers
            in1 = int(stimulus['in1'])
            in2 = int(stimulus['in2'])
            
            # Implement AND gate with inverted in2
            out = in1 & (not in2)
            
            # Convert boolean result to integer
            out = 1 if out else 0
            
            # Add to output list
            output_list.append({'out': str(out)})
        
        # Create output dictionary
        output_dict = {
            'scenario': stimulus_dict['scenario'],
            'output variable': output_list
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

