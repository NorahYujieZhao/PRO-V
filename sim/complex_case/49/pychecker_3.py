import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        """
        No internal state needed for this combinational logic
        """
        pass

    def count_ones(self, value: int) -> int:
        """
        Helper method to count number of 1s in a value
        """
        count = 0
        while value:
            count += value & 1
            value >>= 1
        return count

    def load(self, stimulus_dict: Dict[str, any]):
        """
        Process each input stimulus and return corresponding outputs
        """
        outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary string to integer
            in_value = int(stimulus["in"], 2)

            # Count number of 1s
            ones_count = self.count_ones(in_value)

            # Format result as 8-bit binary string
            out_value = format(ones_count, "08b")

            # Add to outputs
            outputs.append({"out": out_value})

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
