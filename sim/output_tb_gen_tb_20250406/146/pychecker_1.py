import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # Initialize internal state registers
        self.prev_sensors = 0  # Previous sensor state
        self.fr3 = 0
        self.fr2 = 0
        self.fr1 = 0
        self.dfr = 0

    def load(self, stimulus_dict: Dict[str, Any]):
        stimulus_outputs = []

        for stimulus in stimulus_dict["input variable"]:
            reset = int(stimulus["reset"], 2)
            sensors = int(stimulus["s"], 2)

            # Handle reset
            if reset:
                self.fr3 = 1
                self.fr2 = 1
                self.fr1 = 1
                self.dfr = 1
                self.prev_sensors = 0
            else:
                # Check if water level is rising
                rising = sensors > self.prev_sensors

                # Update flow rates based on sensor readings
                if sensors & 0b100:  # s[3] is high - water level above s[3]
                    self.fr3 = 0
                    self.fr2 = 0
                    self.fr1 = 0
                elif sensors & 0b010:  # s[2] is high - water between s[3] and s[2]
                    self.fr3 = 0
                    self.fr2 = 0
                    self.fr1 = 1
                elif sensors & 0b001:  # s[1] is high - water between s[2] and s[1]
                    self.fr3 = 0
                    self.fr2 = 1
                    self.fr1 = 1
                else:  # No sensors - water below s[1]
                    self.fr3 = 1
                    self.fr2 = 1
                    self.fr1 = 1

                # Update supplemental flow rate
                self.dfr = 1 if rising else 0

                # Update previous sensor state
                self.prev_sensors = sensors

            # Convert outputs to binary strings
            out_fr3 = BinaryValue(value=self.fr3, n_bits=1).binstr
            out_fr2 = BinaryValue(value=self.fr2, n_bits=1).binstr
            out_fr1 = BinaryValue(value=self.fr1, n_bits=1).binstr
            out_dfr = BinaryValue(value=self.dfr, n_bits=1).binstr

            stimulus_outputs.append(
                {"fr3": out_fr3, "fr2": out_fr2, "fr1": out_fr1, "dfr": out_dfr}
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
