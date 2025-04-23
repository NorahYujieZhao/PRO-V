
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
        Process input stimuli and generate outputs according to the logic:
        q = (c OR b)
        '''
        # Initialize output list
        q_outputs = []
        
        # Process each input stimulus
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs from string to int
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            c = int(stimulus['c'])
            d = int(stimulus['d'])
            
            # Compute output q
            q = 1 if (c or b) else 0
            
            # Add to output list
            q_outputs.append({"q": str(q)})

        # Format output dictionary
        output_dict = {
            "scenario": stimulus_dict['scenario'],
            "output variable": q_outputs
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

