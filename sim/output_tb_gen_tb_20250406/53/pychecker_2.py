import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize internal state registers"""
        # No state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        """Process inputs and generate outputs"""
        output_values = []

        # Process each input stimulus
        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            in1_bv = BinaryValue(stimulus["in1"], n_bits=1, bigEndian=False)
            in2_bv = BinaryValue(stimulus["in2"], n_bits=1, bigEndian=False)

            # Implement NAND logic
            in1_val = in1_bv.integer
            in2_val = in2_bv.integer
            out_val = not (in1_val and (not in2_val))

            # Convert output to BinaryValue
            out_bv = BinaryValue(value=int(out_val), n_bits=1, bigEndian=False)

            # Add to output list
            output_values.append({"out": out_bv.binstr})

        # Format output dictionary
        output_dict = {
            "scenario": stimulus_dict["scenario"],
            "output variable": output_values,
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
