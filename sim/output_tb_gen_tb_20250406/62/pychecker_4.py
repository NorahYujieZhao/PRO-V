import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # Initialize state to S0 (one-hot encoding)
        self.current_state = BinaryValue(
            value=1, n_bits=10, bigEndian=False
        )  # S0: 0000000001

    def load(self, stimulus_dict: Dict[str, any]):
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input signals to BinaryValue
            input_in = int(stimulus["in"], 2)
            state_bv = BinaryValue(
                value=int(stimulus["state"], 2), n_bits=10, bigEndian=False
            )

            # Calculate next state based on current state and input
            next_state = BinaryValue(value=0, n_bits=10, bigEndian=False)

            if input_in == 0:
                # Most states go back to S0 when input is 0
                if state_bv[5] == 1:  # S5
                    next_state = BinaryValue(
                        value=1 << 8, n_bits=10, bigEndian=False
                    )  # Go to S8
                elif state_bv[6] == 1:  # S6
                    next_state = BinaryValue(
                        value=1 << 9, n_bits=10, bigEndian=False
                    )  # Go to S9
                else:
                    next_state = BinaryValue(
                        value=1, n_bits=10, bigEndian=False
                    )  # Go to S0
            else:  # input_in == 1
                if state_bv[0] == 1:  # S0 -> S1
                    next_state = BinaryValue(value=1 << 1, n_bits=10, bigEndian=False)
                elif state_bv[1] == 1:  # S1 -> S2
                    next_state = BinaryValue(value=1 << 2, n_bits=10, bigEndian=False)
                elif state_bv[2] == 1:  # S2 -> S3
                    next_state = BinaryValue(value=1 << 3, n_bits=10, bigEndian=False)
                elif state_bv[3] == 1:  # S3 -> S4
                    next_state = BinaryValue(value=1 << 4, n_bits=10, bigEndian=False)
                elif state_bv[4] == 1:  # S4 -> S5
                    next_state = BinaryValue(value=1 << 5, n_bits=10, bigEndian=False)
                elif state_bv[5] == 1:  # S5 -> S6
                    next_state = BinaryValue(value=1 << 6, n_bits=10, bigEndian=False)
                elif state_bv[6] == 1:  # S6 -> S7
                    next_state = BinaryValue(value=1 << 7, n_bits=10, bigEndian=False)
                elif state_bv[7] == 1:  # S7 -> S7
                    next_state = BinaryValue(value=1 << 7, n_bits=10, bigEndian=False)
                elif state_bv[8] == 1 or state_bv[9] == 1:  # S8/S9 -> S1
                    next_state = BinaryValue(value=1 << 1, n_bits=10, bigEndian=False)

            # Calculate outputs based on current state
            out1 = "1" if (state_bv[8] == 1 or state_bv[9] == 1) else "0"
            out2 = "1" if (state_bv[7] == 1 or state_bv[9] == 1) else "0"

            output_list.append(
                {"next_state": next_state.binstr, "out1": out1, "out2": out2}
            )

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
