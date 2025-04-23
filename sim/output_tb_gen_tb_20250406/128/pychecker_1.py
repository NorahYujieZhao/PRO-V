import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue objects
            x3_bv = BinaryValue(value=stimulus["x3"], n_bits=1, bigEndian=False)
            x2_bv = BinaryValue(value=stimulus["x2"], n_bits=1, bigEndian=False)
            x1_bv = BinaryValue(value=stimulus["x1"], n_bits=1, bigEndian=False)

            # Convert to integers for logical operations
            x3 = x3_bv.integer
            x2 = x2_bv.integer
            x1 = x1_bv.integer

            # Implement truth table logic
            # f = 1 when:
            # (x3=0 AND x2=1) OR
            # (x3=1 AND x2=0 AND x1=1) OR
            # (x3=1 AND x2=1 AND x1=1)
            f = ((not x3) and x2) or (x3 and (not x2) and x1) or (x3 and x2 and x1)

            # Convert result to BinaryValue
            f_bv = BinaryValue(value=int(f), n_bits=1, bigEndian=False)

            # Add to outputs
            stimulus_outputs.append({"f": f_bv.binstr})

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
