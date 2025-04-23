import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state variables needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary string to integer
            x = int(stimulus["x"], 2)

            # Extract individual bits
            x1 = (x >> 0) & 1  # x[1]
            x2 = (x >> 1) & 1  # x[2]
            x3 = (x >> 2) & 1  # x[3]
            x4 = (x >> 3) & 1  # x[4]

            # Implement K-map logic
            if x3 == 0 and x4 == 0:  # First row
                f = 1 if (x1 == 0 and x2 == 0) or (x1 == 1 and x2 == 0) else 0
            elif x3 == 0 and x4 == 1:  # Second row
                f = 0
            elif x3 == 1 and x4 == 1:  # Third row
                f = 0 if (x1 == 1 and x2 == 0) else 1
            else:  # Fourth row (x3 == 1 and x4 == 0)
                f = 0 if (x1 == 1 and x2 == 1) else 1

            # Convert output to binary string
            stimulus_outputs.append({"f": format(f, "b")})

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
