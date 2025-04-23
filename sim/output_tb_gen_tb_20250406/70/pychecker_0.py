
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
        Returns a dictionary of the outputs aligned with the RTL module outputs.
        '''
        out_list = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert string inputs to integers
            in1 = int(stimulus['in1'])
            in2 = int(stimulus['in2'])
            
            # Implement NOR gate logic
            # Output is 1 only when both inputs are 0
            out = 1 if (in1 == 0 and in2 == 0) else 0
            
            out_list.append({'out': str(out)})
        
        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': out_list
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

