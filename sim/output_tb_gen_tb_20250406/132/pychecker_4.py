import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No state variables needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            cpu_overheated = BinaryValue(
                stimulus["cpu_overheated"], n_bits=1, bigEndian=False
            )
            arrived = BinaryValue(stimulus["arrived"], n_bits=1, bigEndian=False)
            gas_tank_empty = BinaryValue(
                stimulus["gas_tank_empty"], n_bits=1, bigEndian=False
            )

            # Implement fixed logic for shut_off_computer
            if cpu_overheated.integer == 1:
                shut_off_computer = 1
            else:
                shut_off_computer = 0

            # Implement fixed logic for keep_driving
            if arrived.integer == 0:
                keep_driving = 1 if gas_tank_empty.integer == 0 else 0
            else:
                keep_driving = 0

            # Convert outputs to binary strings
            out_shut_off = BinaryValue(
                value=shut_off_computer, n_bits=1, bigEndian=False
            )
            out_keep_driving = BinaryValue(
                value=keep_driving, n_bits=1, bigEndian=False
            )

            # Add outputs to list
            stimulus_outputs.append(
                {
                    "shut_off_computer": out_shut_off.binstr,
                    "keep_driving": out_keep_driving.binstr,
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
