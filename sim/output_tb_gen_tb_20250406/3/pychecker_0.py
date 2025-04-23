
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational circuit, so no state registers are needed.
        '''
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process inputs and generate outputs according to the phone ringer/motor control logic.
        '''
        output_list = []

        for stimulus in stimulus_dict['input variable']:
            # Convert input strings to integers
            ring = int(stimulus['ring'])
            vibrate_mode = int(stimulus['vibrate_mode'])

            # Implement the control logic
            # If ring=1, either ringer or motor should be on (based on vibrate_mode)
            # If ring=0, both should be off
            ringer = 1 if (ring and not vibrate_mode) else 0
            motor = 1 if (ring and vibrate_mode) else 0

            # Add outputs to list
            output_list.append({
                'ringer': str(ringer),
                'motor': str(motor)
            })

        # Format the output dictionary
        output_dict = {
            'scenario': stimulus_dict['scenario'],
            'output variable': output_list
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

