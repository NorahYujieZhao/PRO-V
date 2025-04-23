import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Process each input stimulus and generate corresponding output
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert binary string inputs to integers
            in1 = int(stimulus["in1"], 2)
            in2 = int(stimulus["in2"], 2)

            # Implement NAND logic (AND with inverted in2)
            out = in1 & (~in2 & 1)

            # Convert result back to binary string
            output_list.append({"out": format(out, "b")})

        # Return formatted output dictionary
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
