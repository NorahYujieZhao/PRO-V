
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
        Calculate even parity bit for each 8-bit input.
        Returns dictionary with parity bit outputs.
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input binary string to integer
            in_val = int(stimulus['in'], 2)
            
            # Calculate parity by XORing all bits
            parity = 0
            for i in range(8):
                parity ^= ((in_val >> i) & 1)
            
            outputs.append({"parity": str(parity)})

        return {
            "scenario": stimulus_dict['scenario'],
            "output variable": outputs
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

