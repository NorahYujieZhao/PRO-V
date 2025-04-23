import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize state variables"""
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        """Process inputs and generate outputs"""
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            in_val = BinaryValue(stimulus["in"], n_bits=1, bigEndian=False)
            state_val = BinaryValue(stimulus["state"], n_bits=4, bigEndian=False)

            # Calculate next state based on current state and input
            next_state = BinaryValue(value=0, n_bits=4, bigEndian=False)

            # State A (0001)
            if state_val.integer == 0b0001:
                if in_val.integer == 0:
                    next_state.value = 0b0001  # Stay in A
                else:
                    next_state.value = 0b0010  # Go to B

            # State B (0010)
            elif state_val.integer == 0b0010:
                if in_val.integer == 0:
                    next_state.value = 0b0100  # Go to C
                else:
                    next_state.value = 0b0010  # Stay in B

            # State C (0100)
            elif state_val.integer == 0b0100:
                if in_val.integer == 0:
                    next_state.value = 0b0001  # Go to A
                else:
                    next_state.value = 0b1000  # Go to D

            # State D (1000)
            elif state_val.integer == 0b1000:
                if in_val.integer == 0:
                    next_state.value = 0b0100  # Go to C
                else:
                    next_state.value = 0b0010  # Go to B

            # Calculate output (1 only in state D)
            out = "1" if state_val.integer == 0b1000 else "0"

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
