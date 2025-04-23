import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]) -> Dict[str, Any]:
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Extract inputs
            a = int(stimulus["a"], 2)
            b = int(stimulus["b"], 2)
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)
            e = int(stimulus["e"], 2)

            # Initialize output
            out = 0

            # Compute all 25 comparisons
            # Compare a with all inputs including itself
            out |= (~(a ^ a) & 1) << 24
            out |= (~(a ^ b) & 1) << 23
            out |= (~(a ^ c) & 1) << 22
            out |= (~(a ^ d) & 1) << 21
            out |= (~(a ^ e) & 1) << 20

            # Compare b with all inputs including itself
            out |= (~(b ^ a) & 1) << 19
            out |= (~(b ^ b) & 1) << 18
            out |= (~(b ^ c) & 1) << 17
            out |= (~(b ^ d) & 1) << 16
            out |= (~(b ^ e) & 1) << 15

            # Compare c with all inputs including itself
            out |= (~(c ^ a) & 1) << 14
            out |= (~(c ^ b) & 1) << 13
            out |= (~(c ^ c) & 1) << 12
            out |= (~(c ^ d) & 1) << 11
            out |= (~(c ^ e) & 1) << 10

            # Compare d with all inputs including itself
            out |= (~(d ^ a) & 1) << 9
            out |= (~(d ^ b) & 1) << 8
            out |= (~(d ^ c) & 1) << 7
            out |= (~(d ^ d) & 1) << 6
            out |= (~(d ^ e) & 1) << 5

            # Compare e with all inputs including itself
            out |= (~(e ^ a) & 1) << 4
            out |= (~(e ^ b) & 1) << 3
            out |= (~(e ^ c) & 1) << 2
            out |= (~(e ^ d) & 1) << 1
            out |= (~(e ^ e) & 1) << 0

            # Convert to BinaryValue for output
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
