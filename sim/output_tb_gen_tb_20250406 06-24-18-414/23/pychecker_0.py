
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state storage needed for combinational circuit
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        outputs = []

        # Process each input stimulus
        for stimulus in stimulus_dict['input variable']:
            # Get input vector and selector
            in_vector = stimulus['in']
            sel = stimulus['sel']

            # Validate inputs
            if not isinstance(in_vector, str) or len(in_vector) != 256:
                raise ValueError(f'Invalid input vector: {in_vector}')
            if not isinstance(sel, str) or len(sel) != 8:
                raise ValueError(f'Invalid selector: {sel}')

            # Convert selector to integer
            sel_val = int(sel, 2)

            # Extract the selected bit
            out_bit = in_vector[255 - sel_val]

            # Add to outputs
            outputs.append({'out': out_bit})

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

