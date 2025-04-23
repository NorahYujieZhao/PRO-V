import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            a = BinaryValue(value=stimulus["a"], n_bits=1, bigEndian=False)
            b = BinaryValue(value=stimulus["b"], n_bits=1, bigEndian=False)
            c = BinaryValue(value=stimulus["c"], n_bits=1, bigEndian=False)
            d = BinaryValue(value=stimulus["d"], n_bits=1, bigEndian=False)
            e = BinaryValue(value=stimulus["e"], n_bits=1, bigEndian=False)

            # Convert to integers for easier manipulation
            a_int = a.integer
            b_int = b.integer
            c_int = c.integer
            d_int = d.integer
            e_int = e.integer

            # Calculate all 25 comparisons
            out = 0
            signals = [a_int, b_int, c_int, d_int, e_int]
            bit_pos = 24

            # Generate all pairwise comparisons
            for i in range(5):  # First signal
                for j in range(5):  # Second signal
                    # ~x ^ y is 1 when x == y
                    comparison = ~(signals[i] ^ signals[j]) & 1
                    out |= comparison << bit_pos
                    bit_pos -= 1

            # Convert output to BinaryValue with proper width
            out_bv = BinaryValue(value=out, n_bits=25, bigEndian=False)
            output_list.append({"out": out_bv.binstr})

        return {"scenario": stimulus_dict["scenario"], "output variable": output_list}


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
