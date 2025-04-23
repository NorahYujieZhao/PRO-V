
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Truth table based on Karnaugh map
        # Key = x[3]x[4]x[1]x[2], Value = f
        _TRUTH_TABLE = {
            '0000': '0',  # d->0
            '0001': '0',
            '0011': '0',  # d->0
            '0010': '0',  # d->0
            '0100': '0',
            '0101': '0',  # d->0
            '0111': '1',
            '0110': '0',
            '1100': '1',
            '1101': '1',
            '1111': '0',  # d->0
            '1110': '0',  # d->0
            '1000': '1',
            '1001': '1',
            '1011': '0',
            '1010': '0',  # d->0
        }

        # Extract bits and create lookup key
        x = stimulus_dict['x']
        x_dict = {f"x[{4-i}]": int(b) for i, b in enumerate(x)}
        
        # Create key in correct order: x[3]x[4]x[1]x[2]
        key = str(x_dict['x[3]']) + str(x_dict['x[4]']) + \
              str(x_dict['x[1]']) + str(x_dict['x[2]'])
        
        # Lookup output value
        f_val = _TRUTH_TABLE[key]

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


