
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Truth table mapping input combinations to outputs
        # Key format: x[4]x[3]x[1]x[2]
        _TRUTH_TABLE = {
            '0000': '0',  # d->0
            '0001': '0',
            '0011': '0',  # d->0
            '0010': '0',  # d->0
            '0100': '0',
            '0101': '0',  # d->0
            '0111': '1',
            '0110': '0',
            '1100': '1',
            '1101': '1',
            '1111': '0',  # d->0
            '1110': '0',  # d->0
            '1000': '1',
            '1001': '1',
            '1011': '0',
            '1010': '0',  # d->0
        }

        outputs = []

        for cycle in stimulus_dict['input variable']:
            x_bits = cycle['x']
            # Rearrange bits to match truth table key format
            key = x_bits[0] + x_bits[1] + x_bits[2] + x_bits[3]
            f_val = _TRUTH_TABLE[key]
            outputs.append({'f': f_val})

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

