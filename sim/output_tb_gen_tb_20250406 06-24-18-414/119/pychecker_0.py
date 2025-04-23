
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
        Implements 8-bit to 32-bit sign extension
        '''
        stimulus_outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input binary string to integer
            in_val = int(stimulus['in'], 2)
            
            # Extract sign bit (MSB, bit 7)
            sign_bit = (in_val >> 7) & 1
            
            # Create sign extension (24 copies of sign bit)
            if sign_bit:
                # For negative numbers, extend with 1s
                extension = 0xFFFFFF00 | in_val
            else:
                # For positive numbers, extend with 0s
                extension = in_val
            
            # Format as 32-bit binary string without '0b' prefix
            out_val = format(extension & 0xFFFFFFFF, '032b')
            
            # Add to output list
            stimulus_outputs.append({"out": out_val})
        
        return {
            "scenario": stimulus_dict['scenario'],
            "output variable": stimulus_outputs
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

