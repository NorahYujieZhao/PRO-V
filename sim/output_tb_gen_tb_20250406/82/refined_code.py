

import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Truth table based on Karnaugh map
        # Key = x[1]x[2]x[3]x[4], Value = f
        # Columns (x[1]x[2]): 00,01,11,10
        # Rows (x[3]x[4]): 00,01,11,10
        self._TRUTH_TABLE = {
            '0000': '0',  # d->0 (optimized)
            '0001': '0',  # fixed
            '0011': '1',  # fixed
            '0010': '0',  # d->0 (optimized)
            '0100': '0',  # fixed
            '0101': '0',  # d->0 (optimized)
            '0111': '1',  # fixed
            '0110': '0',  # fixed
            '1100': '1',  # fixed
            '1101': '1',  # fixed
            '1111': '0',  # d->0 (optimized)
            '1110': '0',  # d->0 (optimized)
            '1000': '1',  # fixed
            '1001': '1',  # fixed
            '1011': '0',  # fixed
            '1010': '0'   # d->0 (optimized)
        }

    def load(self, clk, stimulus_dict):
        # Extract input x from stimulus and ensure it's a string
        x = str(stimulus_dict['x'])
        
        # Validate input format
        if len(x) != 4 or not all(bit in '01' for bit in x):
            raise ValueError(f'Invalid input format: {x}')
        
        # Look up output value in truth table
        f_val = self._TRUTH_TABLE[x]
        
        # Return output dictionary
        return {'f': f_val}


def check_output(stimulus):

    dut = GoldenDUT()


        

    return dut.load(stimulus)

if __name__ == "__main__":

    with open("stimulus.json", "r") as f:
        stimulus_data = json.load(f)

    stimulus_list = []
    for stimulus in stimulus_data:
        stimulus_list.append(stimulus['input variable'])

    tb_outputs = []
    for stimulus in stimulus_list:
        scenario_outputs=[]
        for cycle in stimulus:

            outputs = check_output(cycle)
            scenario_outputs.append(outputs)
        tb_outputs.append(scenario_outputs)


    

    print(json.dumps(tb_outputs, indent=2))


