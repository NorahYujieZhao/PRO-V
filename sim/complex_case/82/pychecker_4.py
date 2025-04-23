import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            x = int(stimulus["x"], 2)  # Convert binary string to integer

            # Extract individual bits
            x1 = (x >> 0) & 1  # LSB
            x2 = (x >> 1) & 1
            x3 = (x >> 2) & 1
            x4 = (x >> 3) & 1  # MSB

            # Implement the K-map logic
            if x4 == 0 and x3 == 0:  # 00xx
                f = 0 if (x2 == 0 and x1 == 1) else 0  # Choose 0 for don't cares
            elif x4 == 0 and x3 == 1:  # 01xx
                if x2 == 1 and x1 == 1:  # xx11
                    f = 1
                else:
                    f = 0
            elif x4 == 1 and x3 == 1:  # 11xx
                f = 1 if (x2 == 0 or x1 == 0) else 0
            else:  # 10xx
                if x2 == 1 and x1 == 1:  # xx11
                    f = 0
                else:
                    f = 1

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
