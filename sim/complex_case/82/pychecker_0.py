import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        outputs = []
        for stimulus in stimulus_dict["input variable"]:
            # Convert input string to integer
            x = int(stimulus["x"], 2)

            # Extract individual bits
            x1 = (x >> 0) & 1  # LSB
            x2 = (x >> 1) & 1
            x3 = (x >> 2) & 1
            x4 = (x >> 3) & 1  # MSB

            # Implement K-map logic
            # Don't care conditions are optimized for minimal logic
            if (
                (x3 == 1 and x4 == 1 and (x1 == 0 or x2 == 0))
                or (x3 == 1 and x4 == 0 and (x1 == 0 or x2 == 0))
                or (x3 == 0 and x4 == 1 and x1 == 1 and x2 == 1)
            ):
                f = 1
            else:
                f = 0

            # Convert output to binary string
            outputs.append({"f": format(f, "b")})

        return {"scenario": stimulus_dict["scenario"], "output variable": outputs}


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
