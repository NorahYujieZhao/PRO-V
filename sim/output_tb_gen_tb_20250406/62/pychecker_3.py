import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # Initialize to state S0 (one-hot encoding)
        self.current_state = BinaryValue(
            value=1, n_bits=10, bigEndian=False
        )  # S0: 0000000001

    def load(self, stimulus_dict: Dict[str, Any]):
        outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Get input value
            input_in = int(stimulus["in"], 2)
            state_val = int(stimulus["state"], 2)

            # Convert current state to BinaryValue
            current_state = BinaryValue(value=state_val, n_bits=10, bigEndian=False)

            # Calculate next state based on current state and input
            next_state = BinaryValue(value=0, n_bits=10, bigEndian=False)

            if current_state[0] == 1:  # S0
                next_state = (
                    2 if input_in else 1
                )  # Go to S1 if in=1, stay in S0 if in=0
            elif current_state[1] == 1:  # S1
                next_state = 4 if input_in else 1  # Go to S2 if in=1, go to S0 if in=0
            elif current_state[2] == 1:  # S2
                next_state = 8 if input_in else 1  # Go to S3 if in=1, go to S0 if in=0
            elif current_state[3] == 1:  # S3
                next_state = 16 if input_in else 1  # Go to S4 if in=1, go to S0 if in=0
            elif current_state[4] == 1:  # S4
                next_state = 32 if input_in else 1  # Go to S5 if in=1, go to S0 if in=0
            elif current_state[5] == 1:  # S5
                next_state = (
                    64 if input_in else 256
                )  # Go to S6 if in=1, go to S8 if in=0
            elif current_state[6] == 1:  # S6
                next_state = (
                    128 if input_in else 512
                )  # Go to S7 if in=1, go to S9 if in=0
            elif current_state[7] == 1:  # S7
                next_state = (
                    128 if input_in else 1
                )  # Stay in S7 if in=1, go to S0 if in=0
            elif current_state[8] == 1:  # S8
                next_state = 2 if input_in else 1  # Go to S1 if in=1, go to S0 if in=0
            elif current_state[9] == 1:  # S9
                next_state = 2 if input_in else 1  # Go to S1 if in=1, go to S0 if in=0

            # Calculate outputs
            out1 = 1 if (current_state[8] == 1 or current_state[9] == 1) else 0
            out2 = 1 if (current_state[7] == 1 or current_state[9] == 1) else 0

            # Convert next_state to binary string
            next_state_bin = BinaryValue(
                value=next_state, n_bits=10, bigEndian=False
            ).binstr

            # Create output dictionary for this stimulus
            output_dict = {
                "next_state": next_state_bin,
                "out1": BinaryValue(value=out1, n_bits=1, bigEndian=False).binstr,
                "out2": BinaryValue(value=out2, n_bits=1, bigEndian=False).binstr,
            }
            outputs.append(output_dict)

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
