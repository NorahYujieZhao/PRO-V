
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        Each internal register/state variable must align with the module header.
        Explicitly initialize these states according to the RTL specification.
        '''
        # No internal state needed for this constant output module
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        stimulus_dict: a dictionary formatted as shown above.
        Parse each input variable and use it to perform RTL state updates.
        Returns a dictionary of the outputs aligned with the RTL module outputs.
        '''
        # Create list of 1's with same length as input stimuli
        num_stimuli = len(stimulus_dict['input variable'])
        output_ones = [1] * num_stimuli
        
        # Return output dictionary with constant 1's
        output_dict = {
            "scenario": stimulus_dict['scenario'],
            "output variable": [
                {"one": 1} for _ in range(num_stimuli)
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

