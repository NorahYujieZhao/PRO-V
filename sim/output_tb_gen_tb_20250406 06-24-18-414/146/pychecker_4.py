import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # Initialize internal state registers
        self.prev_sensors = BinaryValue(value=0, n_bits=3)
        self.fr1_reg = BinaryValue(value=1, n_bits=1)
        self.fr2_reg = BinaryValue(value=1, n_bits=1)
        self.fr3_reg = BinaryValue(value=1, n_bits=1)
        self.dfr_reg = BinaryValue(value=1, n_bits=1)

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input signals to BinaryValue
            reset = BinaryValue(stimulus["reset"], n_bits=1)
            sensors = BinaryValue(stimulus["s"], n_bits=3)

            if reset.integer == 1:
                # Reset condition - all outputs active
                self.fr1_reg = BinaryValue(value=1, n_bits=1)
                self.fr2_reg = BinaryValue(value=1, n_bits=1)
                self.fr3_reg = BinaryValue(value=1, n_bits=1)
                self.dfr_reg = BinaryValue(value=1, n_bits=1)
                self.prev_sensors = BinaryValue(value=0, n_bits=3)
            else:
                # Check if water level is rising
                rising = sensors.integer > self.prev_sensors.integer

                # Update flow rates based on sensor readings
                if sensors.integer == 0b111:  # Above s[3]
                    self.fr1_reg = BinaryValue(value=0, n_bits=1)
                    self.fr2_reg = BinaryValue(value=0, n_bits=1)
                    self.fr3_reg = BinaryValue(value=0, n_bits=1)
                elif sensors.integer == 0b011:  # Between s[3] and s[2]
                    self.fr1_reg = BinaryValue(value=1, n_bits=1)
                    self.fr2_reg = BinaryValue(value=0, n_bits=1)
                    self.fr3_reg = BinaryValue(value=0, n_bits=1)
                elif sensors.integer == 0b001:  # Between s[2] and s[1]
                    self.fr1_reg = BinaryValue(value=1, n_bits=1)
                    self.fr2_reg = BinaryValue(value=1, n_bits=1)
                    self.fr3_reg = BinaryValue(value=0, n_bits=1)
                else:  # Below s[1]
                    self.fr1_reg = BinaryValue(value=1, n_bits=1)
                    self.fr2_reg = BinaryValue(value=1, n_bits=1)
                    self.fr3_reg = BinaryValue(value=1, n_bits=1)

                # Set supplemental flow if water level is rising
                self.dfr_reg = BinaryValue(value=1 if rising else 0, n_bits=1)

                # Update previous sensor state
                self.prev_sensors = sensors

            # Append current outputs to results
            output_dict = {
                "fr1": self.fr1_reg.binstr,
                "fr2": self.fr2_reg.binstr,
                "fr3": self.fr3_reg.binstr,
                "dfr": self.dfr_reg.binstr,
            }
            stimulus_outputs.append(output_dict)

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
