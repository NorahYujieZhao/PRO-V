import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        # Process each input stimulus
        output_values = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input to BinaryValue
            in_bv = BinaryValue(value=stimulus["in"], n_bits=100, bigEndian=False)

            # Reverse the bits
            out_str = ""
            for i in range(99, -1, -1):
                out_str += in_bv.binstr[i]

            # Create output dictionary entry
            output_values.append({"out": out_str})

        # Return formatted output dictionary
        return {"scenario": stimulus_dict["scenario"], "output variable": output_values}


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
