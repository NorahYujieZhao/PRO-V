import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        Initialize internal state registers
        """
        # No state registers needed for this implementation
        pass

    def _compute_mux(self, a: str, b: str, sel_b1: str, sel_b2: str) -> str:
        """
        Helper method to compute mux output
        """
        # Convert input strings to BinaryValue
        a_bv = BinaryValue(value=a, n_bits=1, bigEndian=False)
        b_bv = BinaryValue(value=b, n_bits=1, bigEndian=False)
        sel_b1_bv = BinaryValue(value=sel_b1, n_bits=1, bigEndian=False)
        sel_b2_bv = BinaryValue(value=sel_b2, n_bits=1, bigEndian=False)

        # Compute select condition
        select_b = sel_b1_bv.integer and sel_b2_bv.integer

        # Select output based on condition
        result = b_bv.binstr if select_b else a_bv.binstr
        return result

    def load(self, stimulus_dict: Dict[str, any]):
        """
        Process inputs and generate outputs
        """
        outputs = []

        # Process each stimulus
        for stimulus in stimulus_dict["input variable"]:
            a = stimulus["a"]
            b = stimulus["b"]
            sel_b1 = stimulus["sel_b1"]
            sel_b2 = stimulus["sel_b2"]

            # Compute mux outputs
            out_value = self._compute_mux(a, b, sel_b1, sel_b2)

            # Both outputs have same logic
            outputs.append({"out_assign": out_value, "out_always": out_value})

        return {"scenario": stimulus_dict["scenario"], "output variable": outputs}


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
