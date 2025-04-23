
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
        Process input stimuli and generate outputs according to 2-to-1 mux logic
        '''
        outputs = []
        
        # Process each input stimulus
        for stimulus in stimulus_dict['input variable']:
            # Convert binary string inputs to integers
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            sel = int(stimulus['sel'])
            
            # Implement 2-to-1 mux logic
            out = a if sel == 0 else b
            
            # Add output to results list
            outputs.append({'out': str(out)})
        
        # Format output dictionary
        output_dict = {
            'scenario': stimulus_dict['scenario'],
            'output variable': outputs
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

