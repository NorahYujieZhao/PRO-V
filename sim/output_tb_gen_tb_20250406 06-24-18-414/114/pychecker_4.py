import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            in_val = BinaryValue(stimulus["in"], n_bits=1, bigEndian=False)
            state_val = BinaryValue(stimulus["state"], n_bits=4, bigEndian=False)

            # Initialize next_state
            next_state = BinaryValue(value=0, n_bits=4, bigEndian=False)

            # State transition logic
            if state_val.binstr == "0001":  # State A
                if in_val.integer == 0:
                    next_state = BinaryValue(
                        "0001", n_bits=4, bigEndian=False
                    )  # Stay in A
                else:
                    next_state = BinaryValue(
                        "0010", n_bits=4, bigEndian=False
                    )  # Go to B
            elif state_val.binstr == "0010":  # State B
                if in_val.integer == 0:
                    next_state = BinaryValue(
                        "0100", n_bits=4, bigEndian=False
                    )  # Go to C
                else:
                    next_state = BinaryValue(
                        "0010", n_bits=4, bigEndian=False
                    )  # Stay in B
            elif state_val.binstr == "0100":  # State C
                if in_val.integer == 0:
                    next_state = BinaryValue(
                        "0001", n_bits=4, bigEndian=False
                    )  # Go to A
                else:
                    next_state = BinaryValue(
                        "1000", n_bits=4, bigEndian=False
                    )  # Go to D
            elif state_val.binstr == "1000":  # State D
                if in_val.integer == 0:
                    next_state = BinaryValue(
                        "0100", n_bits=4, bigEndian=False
                    )  # Go to C
                else:
                    next_state = BinaryValue(
                        "0010", n_bits=4, bigEndian=False
                    )  # Go to B

            # Output logic - 1 only when in state D
            out = "1" if state_val.binstr == "1000" else "0"

            # Add outputs to results
            stimulus_outputs.append({"next_state": next_state.binstr, "out": out})

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
