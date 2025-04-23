
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state registers needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        outputs = []
        
        # Process each input stimulus
        for stimulus in stimulus_dict['input variable']:
            # Get input bits
            in_bits = stimulus['in']
            
            # Verify input format
            if not isinstance(in_bits, str) or len(in_bits) != 100 or not all(b in '01' for b in in_bits):
                raise ValueError(f'Invalid input: {in_bits}. Expected 100-bit binary string.')
            
            # Reverse the bits
            out_bits = in_bits[::-1]
            
            # Add to outputs
            outputs.append({'out': out_bits})
        
        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': outputs
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

