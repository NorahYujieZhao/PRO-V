import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert inputs to BinaryValue objects
            a = BinaryValue(value=int(stimulus["a"], 2), n_bits=1, bigEndian=False)
            b = BinaryValue(value=int(stimulus["b"], 2), n_bits=1, bigEndian=False)
            c = BinaryValue(value=int(stimulus["c"], 2), n_bits=1, bigEndian=False)
            d = BinaryValue(value=int(stimulus["d"], 2), n_bits=1, bigEndian=False)
            e = BinaryValue(value=int(stimulus["e"], 2), n_bits=1, bigEndian=False)

            # Create 25-bit output
            out = 0
            inputs = [a, b, c, d, e]
            pos = 24

            # Compute all pairwise comparisons
            for i in range(5):  # First input
                for j in range(5):  # Second input
                    # XNOR operation: ~(a ^ b) = 1 when a == b
                    result = ~(inputs[i].integer ^ inputs[j].integer) & 1
                    out |= result << pos
                    pos -= 1

            # Convert output to binary string
            out_bv = BinaryValue(value=out, n_bits=25, bigEndian=False)
            stimulus_outputs.append({"out": out_bv.binstr})

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
