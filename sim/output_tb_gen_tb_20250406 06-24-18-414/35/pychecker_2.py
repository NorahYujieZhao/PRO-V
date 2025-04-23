import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """Initialize internal state variables"""
        # No internal state needed as this is combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        """Process inputs and generate outputs"""
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Extract inputs
            d = int(stimulus["d"], 2)
            done_counting = int(stimulus["done_counting"], 2)
            ack = int(stimulus["ack"], 2)
            state = int(stimulus["state"], 2)

            # Extract current states from one-hot encoding
            S = state & 0b0000000001
            S1 = state & 0b0000000010
            S11 = state & 0b0000000100
            S110 = state & 0b0000001000
            B0 = state & 0b0000010000
            B1 = state & 0b0000100000
            B2 = state & 0b0001000000
            B3 = state & 0b0010000000
            Count = state & 0b0100000000
            Wait = state & 0b1000000000

            # Compute next states
            B3_next = 1 if B2 else 0
            S_next = (
                1
                if (
                    (S and not d)
                    or (S1 and not d)
                    or (S110 and not d)
                    or (Wait and ack)
                )
                else 0
            )
            S1_next = 1 if (S and d) else 0
            Count_next = 1 if (B3 or (Count and not done_counting)) else 0
            Wait_next = 1 if ((Count and done_counting) or (Wait and not ack)) else 0

            # Compute outputs
            shift_ena = 1 if (B0 or B1 or B2 or B3) else 0
            counting = 1 if Count else 0
            done = 1 if Wait else 0

            # Convert to BinaryValue with correct bit widths
            B3_next_bv = BinaryValue(value=B3_next, n_bits=1, bigEndian=False)
            S_next_bv = BinaryValue(value=S_next, n_bits=1, bigEndian=False)
            S1_next_bv = BinaryValue(value=S1_next, n_bits=1, bigEndian=False)
            Count_next_bv = BinaryValue(value=Count_next, n_bits=1, bigEndian=False)
            Wait_next_bv = BinaryValue(value=Wait_next, n_bits=1, bigEndian=False)
            done_bv = BinaryValue(value=done, n_bits=1, bigEndian=False)
            counting_bv = BinaryValue(value=counting, n_bits=1, bigEndian=False)
            shift_ena_bv = BinaryValue(value=shift_ena, n_bits=1, bigEndian=False)

            # Create output dictionary for this stimulus
            output = {
                "B3_next": B3_next_bv.binstr,
                "S_next": S_next_bv.binstr,
                "S1_next": S1_next_bv.binstr,
                "Count_next": Count_next_bv.binstr,
                "Wait_next": Wait_next_bv.binstr,
                "done": done_bv.binstr,
                "counting": counting_bv.binstr,
                "shift_ena": shift_ena_bv.binstr,
            }
            stimulus_outputs.append(output)

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
