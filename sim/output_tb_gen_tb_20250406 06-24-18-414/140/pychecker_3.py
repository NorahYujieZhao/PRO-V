import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state registers needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            c_bv = BinaryValue(stimulus["c"], n_bits=1, bigEndian=False)
            d_bv = BinaryValue(stimulus["d"], n_bits=1, bigEndian=False)

            # Convert to integers for easier processing
            c = c_bv.integer
            d = d_bv.integer

            # Calculate mux_in values based on K-map
            mux_in = [0] * 4

            # mux_in[0] (ab=00): 1 when cd=01,11,10
            mux_in[0] = 1 if (c == 0 and d == 1) or (c == 1) else 0

            # mux_in[1] (ab=01): Always 0
            mux_in[1] = 0

            # mux_in[2] (ab=10): 1 when cd=00,11,10
            mux_in[2] = 1 if (c == 0 and d == 0) or (c == 1) else 0

            # mux_in[3] (ab=11): 1 when cd=11
            mux_in[3] = 1 if (c == 1 and d == 1) else 0

            # Convert to binary string
            mux_in_bv = BinaryValue(
                value=sum(bit << i for i, bit in enumerate(mux_in)),
                n_bits=4,
                bigEndian=False,
            )

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
