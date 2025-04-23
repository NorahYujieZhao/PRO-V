import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        """Initialize internal state"""
        self.mux_in = 0

    def load(self, stimulus_dict: Dict[str, any]):
        """Process inputs and generate outputs"""
        outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to integers
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)

            # Calculate mux_in values based on K-map
            mux_in = [0] * 4

            # mux_in[0] (ab=00): 1 when cd=01,11,10
            mux_in[0] = 1 if (c == 0 and d == 1) or (c == 1) else 0

            # mux_in[1] (ab=01): always 0
            mux_in[1] = 0

            # mux_in[2] (ab=11): 1 when cd=11
            mux_in[2] = 1 if (c == 1 and d == 1) else 0

            # mux_in[3] (ab=10): 1 when cd=00,11,10
            mux_in[3] = (
                1
                if (c == 0 and d == 0) or (c == 1 and d == 1) or (c == 1 and d == 0)
                else 0
            )

            # Convert mux_in array to binary string
            mux_in_val = sum(bit << i for i, bit in enumerate(mux_in))
            mux_in_str = format(mux_in_val, "04b")

            outputs.append({"mux_in": mux_in_str})

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
