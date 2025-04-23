import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        No internal state needed for this combinational logic
        """
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Get input values and convert to BinaryValue
            a = BinaryValue(stimulus["a"], n_bits=5, bigEndian=False)
            b = BinaryValue(stimulus["b"], n_bits=5, bigEndian=False)
            c = BinaryValue(stimulus["c"], n_bits=5, bigEndian=False)
            d = BinaryValue(stimulus["d"], n_bits=5, bigEndian=False)
            e = BinaryValue(stimulus["e"], n_bits=5, bigEndian=False)
            f = BinaryValue(stimulus["f"], n_bits=5, bigEndian=False)

            # Concatenate all inputs and add two '1' bits
            concat_str = (
                f"{a.binstr}{b.binstr}{c.binstr}{d.binstr}{e.binstr}{f.binstr}11"
            )

            # Convert concatenated string to BinaryValue
            concat_val = BinaryValue(concat_str, n_bits=32, bigEndian=False)

            # Split into 8-bit outputs
            w = BinaryValue(concat_val[24:32], n_bits=8, bigEndian=False)
            x = BinaryValue(concat_val[16:24], n_bits=8, bigEndian=False)
            y = BinaryValue(concat_val[8:16], n_bits=8, bigEndian=False)
            z = BinaryValue(concat_val[0:8], n_bits=8, bigEndian=False)

            # Add outputs to result
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
