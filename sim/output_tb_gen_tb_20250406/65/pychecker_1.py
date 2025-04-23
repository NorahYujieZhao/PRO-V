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
            # Convert input strings to BinaryValue objects
            a = BinaryValue(value=stimulus["a"], n_bits=1, bigEndian=False).integer
            b = BinaryValue(value=stimulus["b"], n_bits=1, bigEndian=False).integer
            c = BinaryValue(value=stimulus["c"], n_bits=1, bigEndian=False).integer
            d = BinaryValue(value=stimulus["d"], n_bits=1, bigEndian=False).integer
            e = BinaryValue(value=stimulus["e"], n_bits=1, bigEndian=False).integer

            # Initialize output vector
            out = 0

            # Compute all 25 comparisons
            # Compare 'a' with all inputs
            out |= int(not (a ^ a)) << 24  # out[24]
            out |= int(not (a ^ b)) << 23  # out[23]
            out |= int(not (a ^ c)) << 22  # out[22]
            out |= int(not (a ^ d)) << 21  # out[21]
            out |= int(not (a ^ e)) << 20  # out[20]

            # Compare 'b' with all inputs
            out |= int(not (b ^ a)) << 19  # out[19]
            out |= int(not (b ^ b)) << 18  # out[18]
            out |= int(not (b ^ c)) << 17  # out[17]
            out |= int(not (b ^ d)) << 16  # out[16]
            out |= int(not (b ^ e)) << 15  # out[15]

            # Compare 'c' with all inputs
            out |= int(not (c ^ a)) << 14  # out[14]
            out |= int(not (c ^ b)) << 13  # out[13]
            out |= int(not (c ^ c)) << 12  # out[12]
            out |= int(not (c ^ d)) << 11  # out[11]
            out |= int(not (c ^ e)) << 10  # out[10]

            # Compare 'd' with all inputs
            out |= int(not (d ^ a)) << 9  # out[9]
            out |= int(not (d ^ b)) << 8  # out[8]
            out |= int(not (d ^ c)) << 7  # out[7]
            out |= int(not (d ^ d)) << 6  # out[6]
            out |= int(not (d ^ e)) << 5  # out[5]

            # Compare 'e' with all inputs
            out |= int(not (e ^ a)) << 4  # out[4]
            out |= int(not (e ^ b)) << 3  # out[3]
            out |= int(not (e ^ c)) << 2  # out[2]
            out |= int(not (e ^ d)) << 1  # out[1]
            out |= int(not (e ^ e))  # out[0]

            # Convert output to 25-bit BinaryValue
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
