import json
from typing import Any, Dict, List, Union

from cocotb.binary import BinaryValue


class GoldenDUT:
    def __init__(self):
        # Initialize state registers
        self.prev_sensors = BinaryValue(value=0, n_bits=3)  # Previous sensor state
        self.fr3 = BinaryValue(value=1, n_bits=1)  # Initialize to reset state
        self.fr2 = BinaryValue(value=1, n_bits=1)
        self.fr1 = BinaryValue(value=1, n_bits=1)
        self.dfr = BinaryValue(value=1, n_bits=1)

    def load(self, stimulus_dict: Dict[str, any]):
        output_list = []

        for stimulus in stimulus_dict["input variable"]:
            # Convert input signals
            reset = int(stimulus["reset"], 2)
            sensors = BinaryValue(value=int(stimulus["s"], 2), n_bits=3)

            if reset:
                # Reset state - all outputs on (low water level)
                self.fr3 = BinaryValue(value=1, n_bits=1)
                self.fr2 = BinaryValue(value=1, n_bits=1)
                self.fr1 = BinaryValue(value=1, n_bits=1)
                self.dfr = BinaryValue(value=1, n_bits=1)
                self.prev_sensors = BinaryValue(value=0, n_bits=3)
            else:
                # Determine if water level is rising
                rising = sensors.integer > self.prev_sensors.integer

                # Update flow rates based on sensor readings
                if sensors.integer == 0b111:  # Above s[3]
                    self.fr3 = BinaryValue(value=0, n_bits=1)
                    self.fr2 = BinaryValue(value=0, n_bits=1)
                    self.fr1 = BinaryValue(value=0, n_bits=1)
                elif sensors.integer == 0b011:  # Between s[3] and s[2]
                    self.fr3 = BinaryValue(value=0, n_bits=1)
                    self.fr2 = BinaryValue(value=0, n_bits=1)
                    self.fr1 = BinaryValue(value=1, n_bits=1)
                elif sensors.integer == 0b001:  # Between s[2] and s[1]
                    self.fr3 = BinaryValue(value=0, n_bits=1)
                    self.fr2 = BinaryValue(value=1, n_bits=1)
                    self.fr1 = BinaryValue(value=1, n_bits=1)
                else:  # Below s[1]
                    self.fr3 = BinaryValue(value=1, n_bits=1)
                    self.fr2 = BinaryValue(value=1, n_bits=1)
                    self.fr1 = BinaryValue(value=1, n_bits=1)

                # Update dfr based on water level trend
                self.dfr = BinaryValue(value=1 if rising else 0, n_bits=1)

                # Update previous sensor state
                self.prev_sensors = sensors

            # Append current outputs to output list
            output_list.append(
                {
                    "fr3": self.fr3.binstr,
                    "fr2": self.fr2.binstr,
                    "fr1": self.fr1.binstr,
                    "dfr": self.dfr.binstr,
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
