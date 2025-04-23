import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state registers needed as this is combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        outputs = []
        for stimulus in stimulus_dict["input variable"]:
            # Extract inputs
            d = int(stimulus["d"], 2)
            done_counting = int(stimulus["done_counting"], 2)
            ack = int(stimulus["ack"], 2)
            state = int(stimulus["state"], 2)

            # Extract individual state bits
            S = (state >> 0) & 1
            S1 = (state >> 1) & 1
            S11 = (state >> 2) & 1
            S110 = (state >> 3) & 1
            B0 = (state >> 4) & 1
            B1 = (state >> 5) & 1
            B2 = (state >> 6) & 1
            B3 = (state >> 7) & 1
            Count = (state >> 8) & 1
            Wait = (state >> 9) & 1

            # Calculate next states
            S_next = (S & ~d) | (S1 & ~d) | (S110 & ~d) | (Wait & ack)
            S1_next = S & d
            B3_next = B2
            Count_next = Count & ~done_counting
            Wait_next = (Count & done_counting) | (Wait & ~ack)

            # Calculate outputs
            shift_ena = B0 | B1 | B2 | B3
            counting = Count
            done = Wait

            # Convert outputs to binary strings
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
