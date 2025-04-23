
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational logic
        self.scancode_map = {
            0x45: 0, 0x16: 1, 0x1e: 2, 0x26: 3, 0x25: 4,
            0x2e: 5, 0x36: 6, 0x3d: 7, 0x3e: 8, 0x46: 9
        }

    def load(self, stimulus_dict: Dict[str, any]):
        output_list = []

        for stimulus in stimulus_dict['input variable']:
            # Convert input binary string to integer
            code = int(stimulus['code'], 2)
            
            # Check if code is in valid scancodes
            if code in self.scancode_map:
                out = self.scancode_map[code]
                valid = 1
            else:
                out = 0
                valid = 0
            
            # Create output dictionary for this stimulus
            output_list.append({
                'out': format(out, '04b'),
                'valid': format(valid, '01b')
            })

        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': output_list
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

