import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Get all 5-bit input vectors
            a = int(stimulus["a"], 2)
            b = int(stimulus["b"], 2)
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)
            e = int(stimulus["e"], 2)
            f = int(stimulus["f"], 2)

            # Concatenate all inputs and add two '1' bits at LSB
            # Shift each value left by appropriate amount and combine
            result = (
                (a << 27)
                | (b << 22)
                | (c << 17)
                | (d << 12)
                | (e << 7)
                | (f << 2)
                | 0b11
            )

            # Extract 8-bit segments for outputs
            w = (result >> 24) & 0xFF
            x = (result >> 16) & 0xFF
            y = (result >> 8) & 0xFF
            z = result & 0xFF

            # Format outputs as 8-bit binary strings
            output_dict = {
                "w": format(w, "08b"),
                "x": format(x, "08b"),
                "y": format(y, "08b"),
                "z": format(z, "08b"),
            }
            stimulus_outputs.append(output_dict)

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
