import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            c = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False).integer
            d = BinaryValue(stimulus["d"], n_bits=1, bigEndian=False).integer

            # Calculate mux_in values based on K-map
            mux_in = 0

            # mux_in[0]: 1 when (c,d) is (0,1), (1,1), or (1,0)
            if (not c and d) or (c and d) or (c and not d):
                mux_in |= 1

            # mux_in[1]: Always 0
            # No action needed

            # mux_in[2]: 1 only when c=1 and d=1
            if c and d:
                mux_in |= 1 << 2

            # mux_in[3]: 1 when (c,d) is (0,0), (1,1), or (1,0)
            if (not c and not d) or (c and d) or (c and not d):
                mux_in |= 1 << 3

            # Convert output to BinaryValue
            mux_in_bv = BinaryValue(value=mux_in, n_bits=4, bigEndian=False)

            # Add to outputs
            stimulus_outputs.append({"mux_in": mux_in_bv.binstr})

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
