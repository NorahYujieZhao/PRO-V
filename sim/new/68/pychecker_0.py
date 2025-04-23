
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
        Process input stimuli and generate outputs according to 7458 chip logic.
        '''
        output_list = []

        for stimulus in stimulus_dict['input variable']:
            # Convert string inputs to integers
            p1a = int(stimulus['p1a'])
            p1b = int(stimulus['p1b'])
            p1c = int(stimulus['p1c'])
            p1d = int(stimulus['p1d'])
            p1e = int(stimulus['p1e'])
            p1f = int(stimulus['p1f'])
            p2a = int(stimulus['p2a'])
            p2b = int(stimulus['p2b'])
            p2c = int(stimulus['p2c'])
            p2d = int(stimulus['p2d'])

            # Calculate p1y: OR of two 3-input AND gates
            and1 = p1a and p1b and p1c
            and2 = p1d and p1e and p1f
            p1y = and1 or and2

            # Calculate p2y: OR of two 2-input AND gates
            and3 = p2a and p2b
            and4 = p2c and p2d
            p2y = and3 or and4

            # Convert boolean results to integers
            output_list.append({
                'p1y': '1' if p1y else '0',
                'p2y': '1' if p2y else '0'
            })

        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': output_list
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

