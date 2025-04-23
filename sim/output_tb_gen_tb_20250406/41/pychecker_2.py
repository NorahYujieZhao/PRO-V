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
            # Convert input binary strings to BinaryValue
            a = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False).integer
            b = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False).integer
            c = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False).integer
            d = BinaryValue(stimulus["d"], n_bits=1, bigEndian=False).integer

            # Implement the combinational logic
            and1 = a & b
            and2 = c & d
            out = and1 | and2
            out_n = ~out & 1  # Ensure single bit

            # Convert results back to binary strings
            out_bv = BinaryValue(value=out, n_bits=1, bigEndian=False)
            out_n_bv = BinaryValue(value=out_n, n_bits=1, bigEndian=False)

            # Add outputs to result list
            stimulus_outputs.append({"out": out_bv.binstr, "out_n": out_n_bv.binstr})

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
