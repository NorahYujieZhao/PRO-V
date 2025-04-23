import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state storage needed for combinational logic
        pass

    def evaluate_kmap(self, a: int, b: int, c: int, d: int) -> int:
        # Implement K-map logic directly
        if a == 0 and b == 0:
            return 1 if (c == 0 or d == 0) else 0
        elif a == 0 and b == 1:
            return 1 if (c == 0 and d == 0) or (c == 1 and d == 1) else 0
        elif a == 1 and b == 1:
            return 1 if (c == 1) else 0
        else:  # a == 1 and b == 0
            return 1 if (c == 0 or (c == 1 and d == 1)) else 0

    def load(self, stimulus_dict: Dict[str, Any]) -> Dict[str, Any]:
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue objects
            a_bv = BinaryValue(value=stimulus["a"], n_bits=1, bigEndian=False)
            b_bv = BinaryValue(value=stimulus["b"], n_bits=1, bigEndian=False)
            c_bv = BinaryValue(value=stimulus["c"], n_bits=1, bigEndian=False)
            d_bv = BinaryValue(value=stimulus["d"], n_bits=1, bigEndian=False)

            # Convert to integers for logic evaluation
            a = a_bv.integer
            b = b_bv.integer
            c = c_bv.integer
            d = d_bv.integer

            # Evaluate output based on K-map
            out = self.evaluate_kmap(a, b, c, d)

            # Convert output to BinaryValue and then to string
            out_bv = BinaryValue(value=out, n_bits=1, bigEndian=False)
            output_list.append({"out": out_bv.binstr})

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
