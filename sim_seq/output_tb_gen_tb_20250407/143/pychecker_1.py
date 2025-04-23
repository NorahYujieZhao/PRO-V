import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []
        for stimulus in stimulus_dict["input variable"]:
            # Get the 4-bit input x
            x = int(stimulus["x"], 2)

            # Extract individual bits
            x1 = (x >> 0) & 1  # LSB
            x2 = (x >> 1) & 1
            x3 = (x >> 2) & 1
            x4 = (x >> 3) & 1  # MSB

            # Implement the logic function based on K-map
            f = (
                1
                if (
                    (x4 == 0 and x3 == 0 and x2 == 0 and x1 == 1)
                    or (x4 == 0 and x3 == 0 and x2 == 1 and x1 == 0)
                    or (x4 == 1 and x3 == 0 and x2 == 0 and x1 == 1)
                    or (x4 == 1 and x3 == 0 and x2 == 1 and x1 == 0)
                    or (x4 == 1 and x3 == 1 and x2 == 0 and x1 == 1)
                    or (x4 == 1 and x3 == 1 and x2 == 1 and x1 == 0)
                    or (x4 == 1 and x3 == 1 and x2 == 1 and x1 == 1)
                )
                else 0
            )

            # Add the output to the list
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
