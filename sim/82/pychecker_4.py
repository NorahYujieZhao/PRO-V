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
            # Convert input string to BinaryValue
            x_bv = BinaryValue(value=stimulus["x"], n_bits=4, bigEndian=False)

            # Extract individual bits
            x1 = bool(x_bv[0])
            x2 = bool(x_bv[1])
            x3 = bool(x_bv[2])
            x4 = bool(x_bv[3])

            # Implement the boolean function based on Karnaugh map
            f = (
                ((x3 and not x4) and (not x1 or not x2))
                or ((x3 and x4) and (not x1 and not x2 or not x1 and x2))
                or ((not x3 and x4) and x1 and not x2)
            )

            # Convert result to binary string
            result_bv = BinaryValue(value=int(f), n_bits=1, bigEndian=False)
            stimulus_outputs.append({"f": result_bv.binstr})

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
