import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed as this is purely combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        outputs = []
        for stimulus in stimulus_dict["input variable"]:
            # Extract inputs
            d = int(stimulus["d"], 2)
            done_counting = int(stimulus["done_counting"], 2)
            ack = int(stimulus["ack"], 2)
            state = int(stimulus["state"], 2)

            # Calculate outputs based on current state
            shift_ena = 1 if (state & 0b0011110000) else 0  # B0-B3 states
            counting = 1 if (state & 0b0100000000) else 0  # Count state
            done = 1 if (state & 0b1000000000) else 0  # Wait state

            # Calculate next states
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

            # Next state logic
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
            Count_next = 1 if ((B3) or (Count and not done_counting)) else 0
            Wait_next = 1 if ((Count and done_counting) or (Wait and not ack)) else 0

            # Format outputs as binary strings
            output_dict = {
                "B3_next": format(B3_next, "b"),
                "S_next": format(S_next, "b"),
                "S1_next": format(S1_next, "b"),
                "Count_next": format(Count_next, "b"),
                "Wait_next": format(Wait_next, "b"),
                "done": format(done, "b"),
                "counting": format(counting, "b"),
                "shift_ena": format(shift_ena, "b"),
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
