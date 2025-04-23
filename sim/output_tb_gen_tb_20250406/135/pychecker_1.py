import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # This is a combinational circuit, no state needed
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert binary strings to integers
            a = int(stimulus["a"], 2)
            b = int(stimulus["b"], 2)
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)

            # Count number of 1s
            ones_count = a + b + c + d

            # Output is 1 when:
            # - ones_count is 0 (no 1s)
            # - ones_count is 2 (exactly two 1s)
            # - ones_count is 4 (all 1s)
            q = 1 if (ones_count == 0 or ones_count == 2 or ones_count == 4) else 0

            # Convert output to binary string
            stimulus_outputs.append({"q": format(q, "b")})

        output_dict = {
            "scenario": stimulus_dict["scenario"],
            "output variable": stimulus_outputs,
        }

        return output_dict


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
