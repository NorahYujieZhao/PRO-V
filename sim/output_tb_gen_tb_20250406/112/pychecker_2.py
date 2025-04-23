import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for a combinational multiplexer
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert all inputs to BinaryValue objects
            a = BinaryValue(stimulus["a"], n_bits=16, bigEndian=False)
            b = BinaryValue(stimulus["b"], n_bits=16, bigEndian=False)
            c = BinaryValue(stimulus["c"], n_bits=16, bigEndian=False)
            d = BinaryValue(stimulus["d"], n_bits=16, bigEndian=False)
            e = BinaryValue(stimulus["e"], n_bits=16, bigEndian=False)
            f = BinaryValue(stimulus["f"], n_bits=16, bigEndian=False)
            g = BinaryValue(stimulus["g"], n_bits=16, bigEndian=False)
            h = BinaryValue(stimulus["h"], n_bits=16, bigEndian=False)
            i = BinaryValue(stimulus["i"], n_bits=16, bigEndian=False)
            sel = BinaryValue(stimulus["sel"], n_bits=4, bigEndian=False)

            # Select output based on sel value
            if sel.integer == 0:
                out = a.integer
            elif sel.integer == 1:
                out = b.integer
            elif sel.integer == 2:
                out = c.integer
            elif sel.integer == 3:
                out = d.integer
            elif sel.integer == 4:
                out = e.integer
            elif sel.integer == 5:
                out = f.integer
            elif sel.integer == 6:
                out = g.integer
            elif sel.integer == 7:
                out = h.integer
            elif sel.integer == 8:
                out = i.integer
            else:  # sel 9-15
                out = 0xFFFF  # All bits set to 1

            # Convert output to 16-bit BinaryValue
            out_bv = BinaryValue(value=out, n_bits=16, bigEndian=False)
            stimulus_outputs.append({"out": out_bv.binstr})

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
