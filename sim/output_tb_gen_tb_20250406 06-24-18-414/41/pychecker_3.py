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
            # Convert input strings to BinaryValue
            a = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False)
            b = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False)
            c = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False)
            d = BinaryValue(stimulus["d"], n_bits=1, bigEndian=False)

            # Compute intermediate AND results
            and1_out = BinaryValue(
                value=(a.integer & b.integer), n_bits=1, bigEndian=False
            )
            and2_out = BinaryValue(
                value=(c.integer & d.integer), n_bits=1, bigEndian=False
            )

            # Compute OR output
            out = BinaryValue(
                value=(and1_out.integer | and2_out.integer), n_bits=1, bigEndian=False
            )

            # Compute inverted output
            out_n = BinaryValue(value=(~out.integer & 0x1), n_bits=1, bigEndian=False)

            # Add outputs to results
            stimulus_outputs.append({"out": out.binstr, "out_n": out_n.binstr})

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
