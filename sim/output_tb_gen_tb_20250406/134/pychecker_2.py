import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Get 5-bit input vectors
            a = BinaryValue(value=stimulus["a"], n_bits=5, bigEndian=False)
            b = BinaryValue(value=stimulus["b"], n_bits=5, bigEndian=False)
            c = BinaryValue(value=stimulus["c"], n_bits=5, bigEndian=False)
            d = BinaryValue(value=stimulus["d"], n_bits=5, bigEndian=False)
            e = BinaryValue(value=stimulus["e"], n_bits=5, bigEndian=False)
            f = BinaryValue(value=stimulus["f"], n_bits=5, bigEndian=False)

            # Concatenate all inputs (30 bits) plus two '1' bits
            # Convert each to integer, shift and combine
            result = (
                (a.integer << 27)
                | (b.integer << 22)
                | (c.integer << 17)
                | (d.integer << 12)
                | (e.integer << 7)
                | (f.integer << 2)
                | 0b11
            )

            # Create 32-bit BinaryValue for the complete result
            result_bv = BinaryValue(value=result, n_bits=32, bigEndian=False)

            # Split into four 8-bit outputs
            w = BinaryValue(value=result_bv[24:32].integer, n_bits=8, bigEndian=False)
            x = BinaryValue(value=result_bv[16:24].integer, n_bits=8, bigEndian=False)
            y = BinaryValue(value=result_bv[8:16].integer, n_bits=8, bigEndian=False)
            z = BinaryValue(value=result_bv[0:8].integer, n_bits=8, bigEndian=False)

            # Add outputs to stimulus_outputs list
            stimulus_outputs.append(
                {"w": w.binstr, "x": x.binstr, "y": y.binstr, "z": z.binstr}
            )

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
