import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Create lookup table based on K-map
        # Format: {(x3x4, x1x2): output}
        self.lookup_table = {
            ("00", "00"): 0,  # d -> 0
            ("00", "01"): 0,
            ("00", "11"): 0,  # d -> 0
            ("00", "10"): 0,  # d -> 0
            ("01", "00"): 0,
            ("01", "01"): 0,  # d -> 0
            ("01", "11"): 1,
            ("01", "10"): 0,
            ("11", "00"): 1,
            ("11", "01"): 1,
            ("11", "11"): 0,  # d -> 0
            ("11", "10"): 0,  # d -> 0
            ("10", "00"): 1,
            ("10", "01"): 1,
            ("10", "11"): 0,
            ("10", "10"): 0,  # d -> 0
        }

    def load(self, stimulus_dict: Dict[str, any]):
        outputs = []
        for stimulus in stimulus_dict["input variable"]:
            x = stimulus["x"]
            # Convert binary string to pairs for lookup
            x3x4 = x[0:2]  # First two bits (x[4:3])
            x1x2 = x[2:4]  # Last two bits (x[2:1])

            # Lookup result in truth table
            f = self.lookup_table[(x3x4, x1x2)]

            # Convert to binary string
            outputs.append({"f": format(f, "b")})

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
