
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state needed for combinational logic
        self._TRUTH_TABLE = {
            '0000': '1',  # x[3]x[4]=00, x[1]x[2]=00
            '0001': '0',  # x[3]x[4]=00, x[1]x[2]=01
            '0011': '0',  # x[3]x[4]=00, x[1]x[2]=11
            '0010': '1',  # x[3]x[4]=00, x[1]x[2]=10
            '0100': '0',  # x[3]x[4]=01, x[1]x[2]=00
            '0101': '0',  # x[3]x[4]=01, x[1]x[2]=01
            '0111': '0',  # x[3]x[4]=01, x[1]x[2]=11
            '0110': '0',  # x[3]x[4]=01, x[1]x[2]=10
            '1100': '1',  # x[3]x[4]=11, x[1]x[2]=00
            '1101': '1',  # x[3]x[4]=11, x[1]x[2]=01
            '1111': '1',  # x[3]x[4]=11, x[1]x[2]=11
            '1110': '0',  # x[3]x[4]=11, x[1]x[2]=10
            '1000': '1',  # x[3]x[4]=10, x[1]x[2]=00
            '1001': '1',  # x[3]x[4]=10, x[1]x[2]=01
            '1011': '0',  # x[3]x[4]=10, x[1]x[2]=11
            '1010': '1'   # x[3]x[4]=10, x[1]x[2]=10
        }

    def load(self, stimulus_dict: Dict[str, any]):
        outputs = []
        
        for cycle in stimulus_dict.get("input variable", []):
            x_bits = cycle["x"]
            # Create lookup key in format x[3]x[4]x[1]x[2]
            lookup_key = x_bits[1] + x_bits[0] + x_bits[3] + x_bits[2]
            f_val = self._TRUTH_TABLE[lookup_key]
            outputs.append({"f": f_val})
            
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

