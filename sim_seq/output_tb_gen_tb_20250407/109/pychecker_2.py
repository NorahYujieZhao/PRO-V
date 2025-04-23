import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary string to integer
            in_val = int(stimulus["in"], 2)

            # Calculate out_both[98:0]
            out_both = 0
            for i in range(99):
                if ((in_val >> i) & 1) and ((in_val >> (i + 1)) & 1):
                    out_both |= 1 << i

            # Calculate out_any[99:1]
            out_any = 0
            for i in range(1, 100):
                if ((in_val >> i) & 1) or ((in_val >> (i - 1)) & 1):
                    out_any |= 1 << i

            # Calculate out_different[99:0]
            out_different = 0
            for i in range(100):
                left_neighbor = (i + 1) % 100
                if ((in_val >> i) & 1) != ((in_val >> left_neighbor) & 1):
                    out_different |= 1 << i

            # Format outputs as binary strings with correct width
            result = {
                "out_both": format(out_both, "099b"),
                "out_any": format(out_any >> 1, "099b"),
                "out_different": format(out_different, "0100b"),
            }
            stimulus_outputs.append(result)

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
