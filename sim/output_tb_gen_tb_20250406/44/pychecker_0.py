
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational circuit, so no state registers needed.
        '''
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process inputs and generate outputs according to thermostat logic
        '''
        # Initialize output lists
        heater_list = []
        aircon_list = []
        fan_list = []

        # Process each input stimulus
        for stimulus in stimulus_dict['input variable']:
            # Convert input strings to integers
            mode = int(stimulus['mode'])
            too_cold = int(stimulus['too_cold'])
            too_hot = int(stimulus['too_hot'])
            fan_on = int(stimulus['fan_on'])

            # Calculate outputs based on thermostat logic
            heater = 1 if (mode and too_cold) else 0
            aircon = 1 if (not mode and too_hot) else 0
            fan = 1 if (heater or aircon or fan_on) else 0

            # Append results to output lists
            heater_list.append(heater)
            aircon_list.append(aircon)
            fan_list.append(fan)

        # Format output dictionary
        output_dict = {
            "scenario": stimulus_dict['scenario'],
            "output variable": [
                {"heater": str(h), "aircon": str(a), "fan": str(f)}
                for h, a, f in zip(heater_list, aircon_list, fan_list)
            ]
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

