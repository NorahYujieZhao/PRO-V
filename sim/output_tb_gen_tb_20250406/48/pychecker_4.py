import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state needed for combinational logic
        pass

    def nand4(self, a: str, b: str, c: str, d: str) -> str:
        # Convert inputs to BinaryValue
        a_bv = BinaryValue(value=a, n_bits=1, bigEndian=False)
        b_bv = BinaryValue(value=b, n_bits=1, bigEndian=False)
        c_bv = BinaryValue(value=c, n_bits=1, bigEndian=False)
        d_bv = BinaryValue(value=d, n_bits=1, bigEndian=False)

        # Perform NAND operation
        result = not (a_bv.integer and b_bv.integer and c_bv.integer and d_bv.integer)

        # Convert back to BinaryValue and return binstr
        return BinaryValue(value=int(result), n_bits=1, bigEndian=False).binstr

    def load(self, stimulus_dict: Dict[str, any]):
        output_list = []

        # Process each set of inputs
        for stimulus in stimulus_dict["input variable"]:
            # Compute both NAND4 outputs
            p1y = self.nand4(
                stimulus["p1a"], stimulus["p1b"], stimulus["p1c"], stimulus["p1d"]
            )
            p2y = self.nand4(
                stimulus["p2a"], stimulus["p2b"], stimulus["p2c"], stimulus["p2d"]
            )

            # Add outputs to result list
            output_list.append({"p1y": p1y, "p2y": p2y})

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
