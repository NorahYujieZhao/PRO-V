import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # Initialize internal state registers
        self.prev_sensors = BinaryValue(value=0, n_bits=3)  # Previous sensor state
        self.fr1_reg = 0
        self.fr2_reg = 0
        self.fr3_reg = 0
        self.dfr_reg = 0

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input strings to BinaryValue
            reset = int(stimulus["reset"], 2)
            sensors = BinaryValue(value=stimulus["s"], n_bits=3)

            if reset:
                # Reset condition - as if water was low for long time
                self.fr1_reg = 1
                self.fr2_reg = 1
                self.fr3_reg = 1
                self.dfr_reg = 1
                self.prev_sensors = BinaryValue(value=0, n_bits=3)
            else:
                # Determine if water level is rising
                rising = sensors.integer > self.prev_sensors.integer

                # Update flow rates based on sensor readings
                if sensors.integer == 0b111:  # Above s[3]
                    self.fr1_reg = 0
                    self.fr2_reg = 0
                    self.fr3_reg = 0
                elif sensors.integer == 0b011:  # Between s[3] and s[2]
                    self.fr1_reg = 1
                    self.fr2_reg = 0
                    self.fr3_reg = 0
                elif sensors.integer == 0b001:  # Between s[2] and s[1]
                    self.fr1_reg = 1
                    self.fr2_reg = 1
                    self.fr3_reg = 0
                else:  # Below s[1]
                    self.fr1_reg = 1
                    self.fr2_reg = 1
                    self.fr3_reg = 1

                # Update supplemental flow rate
                self.dfr_reg = 1 if rising else 0

                # Update previous sensor state
                self.prev_sensors = sensors

            # Create output dictionary for this stimulus
            output = {
                "fr3": format(self.fr3_reg, "b"),
                "fr2": format(self.fr2_reg, "b"),
                "fr1": format(self.fr1_reg, "b"),
                "dfr": format(self.dfr_reg, "b"),
            }
            stimulus_outputs.append(output)

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
