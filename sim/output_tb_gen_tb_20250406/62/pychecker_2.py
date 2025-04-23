import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # Initialize to S0 (one-hot encoding)
        self.current_state = BinaryValue(value=1, n_bits=10, bigEndian=False)

    def load(self, stimulus_dict: Dict[str, any]):
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Get input value
            in_val = int(stimulus["in"])
            state_val = int(stimulus["state"], 2)

            # Calculate next state based on current state and input
            next_state = 0

            # S0 transitions
            if state_val & 0b0000000001:
                next_state = 0b0000000001 if not in_val else 0b0000000010
            # S1 transitions
            elif state_val & 0b0000000010:
                next_state = 0b0000000001 if not in_val else 0b0000000100
            # S2 transitions
            elif state_val & 0b0000000100:
                next_state = 0b0000000001 if not in_val else 0b0000001000
            # S3 transitions
            elif state_val & 0b0000001000:
                next_state = 0b0000000001 if not in_val else 0b0000010000
            # S4 transitions
            elif state_val & 0b0000010000:
                next_state = 0b0000000001 if not in_val else 0b0000100000
            # S5 transitions
            elif state_val & 0b0000100000:
                next_state = 0b0100000000 if not in_val else 0b0001000000
            # S6 transitions
            elif state_val & 0b0001000000:
                next_state = 0b1000000000 if not in_val else 0b0010000000
            # S7 transitions
            elif state_val & 0b0010000000:
                next_state = 0b0000000001 if not in_val else 0b0010000000
            # S8 transitions
            elif state_val & 0b0100000000:
                next_state = 0b0000000001 if not in_val else 0b0000000010
            # S9 transitions
            elif state_val & 0b1000000000:
                next_state = 0b0000000001 if not in_val else 0b0000000010

            # Calculate outputs
            out1 = 1 if (state_val & 0b1100000000) else 0
            out2 = 1 if (state_val & 0b1010000000) else 0

            # Create output dictionary
            output_dict = {
                "next_state": format(next_state, "010b"),
                "out1": format(out1, "b"),
                "out2": format(out2, "b"),
            }
            output_list.append(output_dict)

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
