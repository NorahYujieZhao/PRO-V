
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Combinational circuit - no state registers needed
        self._TRUTH_TABLE = {
            '0000': '1',  # ab=00,cd=00 
            '0001': '1',  # ab=00,cd=01
            '0011': '0',  # ab=00,cd=11
            '0010': '1',  # ab=00,cd=10
            '0100': '1',  # ab=01,cd=00
            '0101': '0',  # ab=01,cd=01
            '0111': '1',  # ab=01,cd=11
            '0110': '1',  # ab=01,cd=10
            '1100': '0',  # ab=11,cd=00
            '1101': '0',  # ab=11,cd=01
            '1111': '1',  # ab=11,cd=11
            '1110': '0',  # ab=11,cd=10
            '1000': '1',  # ab=10,cd=00
            '1001': '1',  # ab=10,cd=01
            '1011': '1',  # ab=10,cd=11
            '1010': '0'   # ab=10,cd=10
        }
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        outputs = []
        
        for cycle in stimulus_dict.get('input variable', []):
            # Extract inputs
            a = cycle['a']
            b = cycle['b']
            c = cycle['c']
            d = cycle['d']
            
            # Form lookup key
            key = a + b + c + d
            
            # Get output from truth table
            out = self._TRUTH_TABLE[key]
            
            outputs.append({'out': out})
            
        return outputs
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

