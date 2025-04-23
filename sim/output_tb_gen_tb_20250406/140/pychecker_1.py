import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Get input values
            c = int(stimulus["c"], 2)
            d = int(stimulus["d"], 2)

            # Calculate mux_in bits based on K-map
            mux_in0 = 1 if (c == 0 and d == 1) or (c == 1) else 0
            mux_in1 = 0  # Always 0
            mux_in2 = 1 if (c == 1 and d == 1) or (c == 1 and d == 0) else 0
            mux_in3 = 1 if (c == 0 and d == 0) or (c == 1) else 0

            # Combine bits into 4-bit value
            mux_in = (mux_in3 << 3) | (mux_in2 << 2) | (mux_in1 << 1) | mux_in0

            # Convert to BinaryValue
            mux_in_bv = BinaryValue(value=mux_in, n_bits=4, bigEndian=False)

            # Add to output list as binary string
            stimulus_outputs.append({"mux_in": mux_in_bv.binstr})

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
