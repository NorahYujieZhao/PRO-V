import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state needed for combinational logic
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
            # Based on the truth table derived from waveforms
            q = int(
                (
                    (not a and not b and not c and not d)
                    or (not a and not b and c and d)
                    or (not a and b and not c and d)
                    or (not a and b and c and not d)
                    or (a and not b and not c and d)
                    or (a and not b and c and not d)
                    or (a and b and not c and not d)
                    or (a and b and c and d)
                )
            )

            # Convert output to binary string
            q_str = format(q, "b")

            # Add to outputs
            stimulus_outputs.append({"q": q_str})

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
