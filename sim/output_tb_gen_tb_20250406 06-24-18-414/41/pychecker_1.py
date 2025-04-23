import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        output_list = []

        # Process each stimulus input
        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            a = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False)
            b = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False)
            c = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False)
            d = BinaryValue(stimulus["d"], n_bits=1, bigEndian=False)

            # Calculate intermediate AND results
            and1 = BinaryValue(value=(a.integer & b.integer), n_bits=1, bigEndian=False)
            and2 = BinaryValue(value=(c.integer & d.integer), n_bits=1, bigEndian=False)

            # Calculate OR result
            out = BinaryValue(
                value=(and1.integer | and2.integer), n_bits=1, bigEndian=False
            )

            # Calculate inverted output
            out_n = BinaryValue(value=(~out.integer & 1), n_bits=1, bigEndian=False)

            # Add outputs to result list
            output_list.append({"out": out.binstr, "out_n": out_n.binstr})

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
