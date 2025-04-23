import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state variables needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Get input x and convert to BinaryValue
            x = BinaryValue(value=stimulus["x"], n_bits=4, bigEndian=False)

            # Extract pairs of bits
            x1x2 = (x[0:2]).integer  # x[1]x[2]
            x3x4 = (x[2:4]).integer  # x[3]x[4]

            # Implement K-map logic
            f = 0
            if x3x4 == 0b00 and (x1x2 == 0b00 or x1x2 == 0b10):
                f = 1
            elif x3x4 == 0b10 and (x1x2 == 0b00 or x1x2 == 0b01 or x1x2 == 0b10):
                f = 1
            elif x3x4 == 0b11 and (x1x2 == 0b00 or x1x2 == 0b01 or x1x2 == 0b11):
                f = 1

            stimulus_outputs.append(
                {"f": BinaryValue(value=f, n_bits=1, bigEndian=False).binstr}
            )

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
