import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # This is a combinational circuit, no state needed
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            a = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False).integer
            b = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False).integer
            c = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False).integer
            d = BinaryValue(stimulus["d"], n_bits=1, bigEndian=False).integer

            # Count number of 1s in inputs
            ones_count = a + b + c + d

            # Output is 1 if number of 1s is even (0,2,4), 0 if odd (1,3)
            q = 1 if ones_count % 2 == 0 else 0

            # Convert output to BinaryValue string format
            q_bv = BinaryValue(value=q, n_bits=1, bigEndian=False)

            # Add to output list
            stimulus_outputs.append({"q": q_bv.binstr})

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
