import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        # Process each input stimulus
        for stimulus in stimulus_dict["input variable"]:
            # Create BinaryValue objects for inputs and outputs
            code = BinaryValue(
                value=int(stimulus["code"], 2), n_bits=8, bigEndian=False
            )
            out = BinaryValue(value=0, n_bits=4, bigEndian=False)
            valid = BinaryValue(value=0, n_bits=1, bigEndian=False)

            # Check for valid scancodes and set outputs
            code_int = code.integer
            if code_int == 0x45:
                out.value = 0
                valid.value = 1
            elif code_int == 0x16:
                out.value = 1
                valid.value = 1
            elif code_int == 0x1E:
                out.value = 2
                valid.value = 1
            elif code_int == 0x26:
                out.value = 3
                valid.value = 1
            elif code_int == 0x25:
                out.value = 4
                valid.value = 1
            elif code_int == 0x2E:
                out.value = 5
                valid.value = 1
            elif code_int == 0x36:
                out.value = 6
                valid.value = 1
            elif code_int == 0x3D:
                out.value = 7
                valid.value = 1
            elif code_int == 0x3E:
                out.value = 8
                valid.value = 1
            elif code_int == 0x46:
                out.value = 9
                valid.value = 1
            else:
                out.value = 0
                valid.value = 0

            # Add outputs to results
            stimulus_outputs.append({"out": out.binstr, "valid": valid.binstr})

        # Return formatted output dictionary
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
