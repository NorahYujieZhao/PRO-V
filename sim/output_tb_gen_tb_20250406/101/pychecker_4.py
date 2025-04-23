import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize internal state variables"""
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        """Process input stimuli and generate outputs"""
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input signals to BinaryValue
            in_signal = int(stimulus["in"], 2)
            state = int(stimulus["state"], 2)

            # Compute next state based on current state and input
            if state == 0b00:  # State A
                next_state = 0b00 if in_signal == 0 else 0b01
            elif state == 0b01:  # State B
                next_state = 0b10 if in_signal == 0 else 0b01
            elif state == 0b10:  # State C
                next_state = 0b00 if in_signal == 0 else 0b11
            else:  # State D (0b11)
                next_state = 0b10 if in_signal == 0 else 0b01

            # Compute output (1 only in state D)
            out = 1 if state == 0b11 else 0

            # Convert outputs to BinaryValue format
            next_state_bv = BinaryValue(value=next_state, n_bits=2, bigEndian=False)
            out_bv = BinaryValue(value=out, n_bits=1, bigEndian=False)

            # Add outputs to results
            stimulus_outputs.append(
                {"next_state": next_state_bv.binstr, "out": out_bv.binstr}
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
