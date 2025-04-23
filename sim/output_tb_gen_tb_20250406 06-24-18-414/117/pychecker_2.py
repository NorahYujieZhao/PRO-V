import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        output_values = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            a = BinaryValue(stimulus["a"], n_bits=1, bigEndian=False).integer
            b = BinaryValue(stimulus["b"], n_bits=1, bigEndian=False).integer
            c = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False).integer
            d = BinaryValue(stimulus["d"], n_bits=1, bigEndian=False).integer

            # Implement K-map logic
            out = 0
            if (
                (c == 0 and d == 0 and (a == 0 or b == 0))
                or (c == 0 and d == 1 and a == 0 and b == 0)
                or (c == 0 and d == 1 and a == 1 and b == 0)
                or (c == 1 and d == 1 and (a == 0 or b == 1))
                or (c == 1 and d == 0 and (a == 0 or a == 1))
            ):
                out = 1

            # Convert output to binary string
            out_bv = BinaryValue(value=out, n_bits=1, bigEndian=False)
            output_values.append({"out": out_bv.binstr})

        return {"scenario": stimulus_dict["scenario"], "output variable": output_values}


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
