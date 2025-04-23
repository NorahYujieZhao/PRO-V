
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Combinational circuit - no state registers needed
        self._TRUTH_TABLE = {
            '0100': '0',  # ab=01,cd=00 (d->0)
            '0000': '0',  # ab=00,cd=00
            '1000': '1',  # ab=10,cd=00
            '1100': '1',  # ab=11,cd=00
            '0101': '0',  # ab=01,cd=01
            '0001': '0',  # ab=00,cd=01
            '1001': '0',  # ab=10,cd=01 (d->0)
            '1101': '0',  # ab=11,cd=01 (d->0)
            '0111': '0',  # ab=01,cd=11
            '0011': '1',  # ab=00,cd=11
            '1011': '1',  # ab=10,cd=11
            '1111': '1',  # ab=11,cd=11
            '0110': '0',  # ab=01,cd=10
            '0010': '1',  # ab=00,cd=10
            '1010': '1',  # ab=10,cd=10
            '1110': '1'   # ab=11,cd=10
        }
        
    def load(self, stimulus_dict: Dict[str, any]):
        outputs = []
        
        for cycle in stimulus_dict.get('input variable', []):
            # Extract inputs
            a = int(cycle['a'])
            b = int(cycle['b'])
            c = int(cycle['c'])
            d = int(cycle['d'])
            
            # Construct lookup key
            key = f'{a}{b}{c}{d}'
            
            # Validate input
            if not all(bit in '01' for bit in key):
                raise ValueError(f'Invalid binary input: {key}')
                
            # Lookup output
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

