import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert inputs to BinaryValue
            c_bv = BinaryValue(value=stimulus["c"], n_bits=1, bigEndian=False)
            d_bv = BinaryValue(value=stimulus["d"], n_bits=1, bigEndian=False)

            # Convert to integers for easier processing
            c = c_bv.integer
            d = d_bv.integer

            # Calculate mux_in values
            mux_in = [0] * 4

            # mux_in[0] (ab=00): Pattern 0011
            mux_in[0] = 1 if ((c == 0 and d == 1) or (c == 1)) else 0

            # mux_in[1] (ab=01): Always 0
            mux_in[1] = 0

            # mux_in[2] (ab=10): Pattern 1011
            mux_in[2] = (
                1
                if ((c == 0 and d == 0) or (c == 1 and d == 1) or (c == 1 and d == 0))
                else 0
            )

            # mux_in[3] (ab=11): Pattern 0010
            mux_in[3] = 1 if (c == 1 and d == 1) else 0

            # Convert to BinaryValue for output
            mux_in_bv = BinaryValue(
                value=sum(b << i for i, b in enumerate(mux_in)),
                n_bits=4,
                bigEndian=False,
            )

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
