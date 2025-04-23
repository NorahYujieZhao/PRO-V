import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary strings to integers
            a = int(stimulus["a"], 2)
            b = int(stimulus["b"], 2)
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)

            # Combine inputs into 4-bit value
            input_val = (a << 3) | (b << 2) | (c << 1) | d

            # Check for output conditions
            # Logic 1 for 2 (0010), 7 (0111), 15 (1111)
            out_sop = 1 if input_val in [2, 7, 15] else 0

            # Logic 0 for 0,1,4,5,6,9,10,13,14
            # Logic 1 for 2,7,15
            out_pos = 1 if input_val in [2, 7, 15] else 0

            # Format outputs as binary strings
            output = {"out_sop": format(out_sop, "b"), "out_pos": format(out_pos, "b")}
            stimulus_outputs.append(output)

        return {
            "scenario": stimulus_dict["scenario"],
            "output variable": stimulus_outputs,
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
