import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to integers
            a = int(stimulus["a"], 2)
            b = int(stimulus["b"], 2)
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)

            # Combine inputs into 4-bit value
            input_val = (a << 3) | (b << 2) | (c << 1) | d

            # Check if input matches conditions for output 1
            # 2 (0010), 7 (0111), 15 (1111)
            output = 1 if input_val in [2, 7, 15] else 0

            # Create output dictionary with both outputs
            output_dict = {
                "out_sop": format(output, "b"),
                "out_pos": format(output, "b"),
            }
            output_list.append(output_dict)

        return {"scenario": stimulus_dict["scenario"], "output variable": output_list}


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
