import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize state variables"""
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert inputs to BinaryValue
            d = int(stimulus["d"])
            done_counting = int(stimulus["done_counting"])
            ack = int(stimulus["ack"])
            state = BinaryValue(
                value=int(stimulus["state"], 2), n_bits=10, bigEndian=False
            )

            # Extract current states
            S = state[0]
            S1 = state[1]
            S11 = state[2]
            S110 = state[3]
            B0 = state[4]
            B1 = state[5]
            B2 = state[6]
            B3 = state[7]
            Count = state[8]
            Wait = state[9]

            # Calculate next states
            B3_next = B2
            S_next = ((S | S1 | S11 | S110) & ~d) | (Wait & ack)
            S1_next = S & d
            Count_next = B3 | (Count & ~done_counting)
            Wait_next = (Count & done_counting) | (Wait & ~ack)

            # Calculate outputs
            done = Wait
            counting = Count
            shift_ena = B0 | B1 | B2 | B3

            # Create output dictionary for this stimulus
            outputs = {
                "B3_next": str(int(B3_next)),
                "S_next": str(int(S_next)),
                "S1_next": str(int(S1_next)),
                "Count_next": str(int(Count_next)),
                "Wait_next": str(int(Wait_next)),
                "done": str(int(done)),
                "counting": str(int(counting)),
                "shift_ena": str(int(shift_ena)),
            }
            stimulus_outputs.append(outputs)

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
