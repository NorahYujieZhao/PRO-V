import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # No internal state needed for this combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, Any]) -> Dict[str, Any]:
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input binary strings to BinaryValue
            cpu_overheated = BinaryValue(
                stimulus["cpu_overheated"], n_bits=1, bigEndian=False
            ).integer
            arrived = BinaryValue(
                stimulus["arrived"], n_bits=1, bigEndian=False
            ).integer
            gas_tank_empty = BinaryValue(
                stimulus["gas_tank_empty"], n_bits=1, bigEndian=False
            ).integer

            # Implement combinational logic
            shut_off_computer = 1 if cpu_overheated else 0
            keep_driving = 0 if arrived else (0 if gas_tank_empty else 1)

            # Convert outputs back to binary strings
            output_shut_off = BinaryValue(
                value=shut_off_computer, n_bits=1, bigEndian=False
            ).binstr
            output_keep_driving = BinaryValue(
                value=keep_driving, n_bits=1, bigEndian=False
            ).binstr

            # Add outputs to result list
            stimulus_outputs.append(
                {
                    "shut_off_computer": output_shut_off,
                    "keep_driving": output_keep_driving,
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
