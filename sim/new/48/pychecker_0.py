
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        Each internal register/state variable must align with the module header.
        Explicitly initialize these states according to the RTL specification.
        '''
        # This is a purely combinational circuit, no state registers needed
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        stimulus_dict: a dictionary formatted as shown above.
        Parse each input variable and use it to perform RTL state updates.
        Returns a dictionary of the outputs aligned with the RTL module outputs.
        '''
        p1y_list = []
        p2y_list = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input strings to integers
            p1a = int(stimulus['p1a'])
            p1b = int(stimulus['p1b'])
            p1c = int(stimulus['p1c'])
            p1d = int(stimulus['p1d'])
            p2a = int(stimulus['p2a'])
            p2b = int(stimulus['p2b'])
            p2c = int(stimulus['p2c'])
            p2d = int(stimulus['p2d'])
            
            # Implement NAND gate logic
            # NAND output is 0 only when all inputs are 1
            p1y = 0 if (p1a and p1b and p1c and p1d) else 1
            p2y = 0 if (p2a and p2b and p2c and p2d) else 1
            
            p1y_list.append(p1y)
            p2y_list.append(p2y)
        
        # Format output dictionary
        output_dict = {
            'scenario': stimulus_dict['scenario'],
            'output variable': [
                {'p1y': str(p1y), 'p2y': str(p2y)} 
                for p1y, p2y in zip(p1y_list, p2y_list)
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

