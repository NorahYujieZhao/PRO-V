import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to boolean values
            a = int(stimulus["a"], 2)
            b = int(stimulus["b"], 2)
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)

            # Calculate out_sop using sum of products form
            # out_sop = !a!bc!d + !abcd + abcd
            out_sop = (
                ((not a) and (not b) and c and (not d))
                or ((not a) and b and c and d)
                or (a and b and c and d)
            )

            # Calculate out_pos using product of sums form
            # Same logic, different representation
            out_pos = out_sop

            # Convert boolean results to binary strings
            output_dict = {
                "out_sop": format(int(out_sop), "b"),
                "out_pos": format(int(out_pos), "b"),
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
