import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed as this is combinational logic only
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            in_val = int(stimulus["in"])
            state_bv = BinaryValue(
                value=int(stimulus["state"], 2), n_bits=4, bigEndian=False
            )

            # Calculate next state based on current state and input
            next_state = 0

            # State A (0001)
            if state_bv.integer == 0b0001:
                next_state = 0b0001 if in_val == 0 else 0b0010

            # State B (0010)
            elif state_bv.integer == 0b0010:
                next_state = 0b0100 if in_val == 0 else 0b0010

            # State C (0100)
            elif state_bv.integer == 0b0100:
                next_state = 0b0001 if in_val == 0 else 0b1000

            # State D (1000)
            elif state_bv.integer == 0b1000:
                next_state = 0b0100 if in_val == 0 else 0b0010

            # Calculate output (1 only in state D)
            out = 1 if state_bv.integer == 0b1000 else 0

            # Convert next_state to BinaryValue for proper formatting
            next_state_bv = BinaryValue(value=next_state, n_bits=4, bigEndian=False)

            # Add to output list
            stimulus_outputs.append(
                {"next_state": next_state_bv.binstr, "out": str(out)}
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
