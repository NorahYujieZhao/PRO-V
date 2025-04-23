import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to boolean values
            a = int(stimulus["a"], 2)
            b = int(stimulus["b"], 2)
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)

            # Implement the logic based on Karnaugh map
            out = (
                (not c and not d and (not a or not b))  # cd=00 cases
                or (not c and d and not a and not b)  # cd=01, ab=00
                or (not c and d and a and not b)  # cd=01, ab=10
                or (c and d and (not a or b))  # cd=11 cases
                or (c and not d and not b)  # cd=10 cases
            )

            # Convert boolean to binary string
            out_val = "1" if out else "0"
            stimulus_outputs.append({"out": out_val})

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
