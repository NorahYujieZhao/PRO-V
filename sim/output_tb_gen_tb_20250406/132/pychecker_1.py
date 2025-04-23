import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        """
        Initialize outputs. Though not strictly needed for combinational logic,
        good practice to define them.
        """
        self.shut_off_computer = 0
        self.keep_driving = 0

    def load(self, stimulus_dict: Dict[str, Any]):
        """
        Process inputs and generate outputs according to RTL logic
        """
        output_list = []

        # Process each stimulus in the input list
        for stimulus in stimulus_dict["input variable"]:
            # Convert inputs to BinaryValue
            cpu_overheated = BinaryValue(
                value=stimulus["cpu_overheated"], n_bits=1, bigEndian=False
            )
            arrived = BinaryValue(value=stimulus["arrived"], n_bits=1, bigEndian=False)
            gas_tank_empty = BinaryValue(
                value=stimulus["gas_tank_empty"], n_bits=1, bigEndian=False
            )

            # Implement combinational logic
            if cpu_overheated.integer == 1:
                shut_off_computer = 1
            else:
                shut_off_computer = 0

            if arrived.integer == 0:
                keep_driving = 1 if gas_tank_empty.integer == 0 else 0
            else:
                keep_driving = 0

            # Convert outputs to BinaryValue
            shut_off_computer_bv = BinaryValue(
                value=shut_off_computer, n_bits=1, bigEndian=False
            )
            keep_driving_bv = BinaryValue(value=keep_driving, n_bits=1, bigEndian=False)

            # Add outputs to result list
            output_list.append(
                {
                    "shut_off_computer": shut_off_computer_bv.binstr,
                    "keep_driving": keep_driving_bv.binstr,
                }
            )

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
