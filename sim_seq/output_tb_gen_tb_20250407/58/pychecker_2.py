import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        pass

    def module_a(self, x: int, y: int) -> int:
        """Implement z = (x^y) & x"""
        return (x ^ y) & x

    def module_b(self, x: int, y: int) -> int:
        """Implement B module behavior: z=1 when x=y, z=0 otherwise"""
        return 1 if x == y else 0

    def load(self, stimulus_dict: Dict[str, any]):
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert binary string inputs to integers
            x = int(stimulus["x"], 2)
            y = int(stimulus["y"], 2)

            # Calculate outputs of all submodules
            a1_out = self.module_a(x, y)
            a2_out = self.module_a(x, y)
            b1_out = self.module_b(x, y)
            b2_out = self.module_b(x, y)

            # Combine outputs according to top-level logic
            or_out = a1_out | b1_out
            and_out = a2_out & b2_out
            z = or_out ^ and_out

            # Format output as binary string
            output_list.append({"z": format(z, "b")})

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
