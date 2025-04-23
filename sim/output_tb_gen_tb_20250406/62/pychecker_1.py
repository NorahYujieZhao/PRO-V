import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        Initialize state variables
        """
        self.current_state = 0  # Start in S0

    def load(self, stimulus_dict: Dict[str, Any]):
        """
        Process inputs and generate outputs according to state machine logic
        """
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            in_bv = BinaryValue(stimulus["in"], n_bits=1, bigEndian=False)
            state_bv = BinaryValue(stimulus["state"], n_bits=10, bigEndian=False)

            # Get integer values
            in_val = in_bv.integer
            state_val = state_bv.integer

            # Calculate next state
            next_state = 0

            # State transition logic
            if state_val & (1 << 5):  # S5
                next_state = (1 << 8) if in_val == 0 else (1 << 6)
            elif state_val & (1 << 6):  # S6
                next_state = (1 << 9) if in_val == 0 else (1 << 7)
            elif state_val & (1 << 7):  # S7
                next_state = (1 << 0) if in_val == 0 else (1 << 7)
            elif state_val & ((1 << 8) | (1 << 9)):  # S8 or S9
                next_state = (1 << 0) if in_val == 0 else (1 << 1)
            else:  # S0-S4
                if in_val == 0:
                    next_state = 1  # S0
                else:
                    # Find current state number and increment
                    for i in range(5):
                        if state_val & (1 << i):
                            next_state = 1 << (i + 1)
                            break

            # Calculate outputs
            out1 = 1 if state_val & ((1 << 8) | (1 << 9)) else 0
            out2 = 1 if state_val & ((1 << 7) | (1 << 9)) else 0

            # Convert outputs to BinaryValue
            next_state_bv = BinaryValue(value=next_state, n_bits=10, bigEndian=False)
            out1_bv = BinaryValue(value=out1, n_bits=1, bigEndian=False)
            out2_bv = BinaryValue(value=out2, n_bits=1, bigEndian=False)

            # Add outputs to result
            stimulus_outputs.append(
                {
                    "next_state": next_state_bv.binstr,
                    "out1": out1_bv.binstr,
                    "out2": out2_bv.binstr,
                }
            )

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
