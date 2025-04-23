import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state variables needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            cpu_overheated = BinaryValue(
                value=stimulus["cpu_overheated"], n_bits=1, bigEndian=False
            ).integer
            arrived = BinaryValue(
                value=stimulus["arrived"], n_bits=1, bigEndian=False
            ).integer
            gas_tank_empty = BinaryValue(
                value=stimulus["gas_tank_empty"], n_bits=1, bigEndian=False
            ).integer

            # Implement the corrected combinational logic
            shut_off_computer = 1 if cpu_overheated else 0
            keep_driving = 0 if arrived else (not gas_tank_empty)

            # Convert outputs to binary strings
            shut_off_computer_bv = BinaryValue(
                value=shut_off_computer, n_bits=1, bigEndian=False
            )
            keep_driving_bv = BinaryValue(value=keep_driving, n_bits=1, bigEndian=False)

            # Add outputs to result list
            stimulus_outputs.append(
                {
                    "shut_off_computer": shut_off_computer_bv.binstr,
                    "keep_driving": keep_driving_bv.binstr,
                }
            )

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
