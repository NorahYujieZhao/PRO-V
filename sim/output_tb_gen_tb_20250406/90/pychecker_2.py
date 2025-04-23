import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for this combinational circuit
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        # Process each set of inputs
        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue objects
            a = BinaryValue(value=stimulus["a"], n_bits=1, bigEndian=False)
            b = BinaryValue(value=stimulus["b"], n_bits=1, bigEndian=False)
            sel_b1 = BinaryValue(value=stimulus["sel_b1"], n_bits=1, bigEndian=False)
            sel_b2 = BinaryValue(value=stimulus["sel_b2"], n_bits=1, bigEndian=False)

            # Calculate outputs
            # For out_assign and out_always, select b if both sel_b1 and sel_b2 are true
            select_b = sel_b1.integer and sel_b2.integer

            # Create output values
            out_assign = b if select_b else a
            out_always = b if select_b else a

            # Convert to BinaryValue for consistent output format
            out_assign_bv = BinaryValue(
                value=out_assign.integer, n_bits=1, bigEndian=False
            )
            out_always_bv = BinaryValue(
                value=out_always.integer, n_bits=1, bigEndian=False
            )

            # Add outputs to result list
            stimulus_outputs.append(
                {"out_assign": out_assign_bv.binstr, "out_always": out_always_bv.binstr}
            )

        # Return formatted output
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
