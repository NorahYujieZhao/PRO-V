import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert binary string inputs to integers
            a = int(stimulus["a"], 2)
            b = int(stimulus["b"], 2)
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)

            # Implement the combinational logic function
            q = (
                1
                if (
                    (a == 0 and b == 0 and c == 0 and d == 0)  # 0000
                    or (a == 0 and b == 0 and c == 1 and d == 1)  # 0011
                    or (a == 0 and b == 1 and c == 0 and d == 1)  # 0101
                    or (a == 0 and b == 1 and c == 1 and d == 0)  # 0110
                    or (a == 1 and b == 0 and c == 0 and d == 1)  # 1001
                    or (a == 1 and b == 0 and c == 1 and d == 0)  # 1010
                    or (a == 1 and b == 1 and c == 0 and d == 0)  # 1100
                    or (a == 1 and b == 1 and c == 1 and d == 1)  # 1111
                )
                else 0
            )

            # Convert output to binary string
            stimulus_outputs.append({"q": format(q, "b")})

        output_dict = {
            "scenario": stimulus_dict["scenario"],
            "output variable": stimulus_outputs,
        }

        return output_dict


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
