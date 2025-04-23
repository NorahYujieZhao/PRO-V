import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary strings to integers
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)

            # Calculate mux_in outputs
            mux_in0 = 1 if (c or d) else 0  # c + d
            mux_in1 = 0  # Always 0
            mux_in2 = 1 if (c and d) else 0  # c·d
            mux_in3 = 1 if ((not c and not d) or (c and d) or (c and not d)) else 0

            # Combine into 4-bit result
            mux_in = (mux_in3 << 3) | (mux_in2 << 2) | (mux_in1 << 1) | mux_in0

            # Format as 4-bit binary string
            mux_in_str = format(mux_in, "04b")

            # Add to output list
            stimulus_outputs.append({"mux_in": mux_in_str})

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
