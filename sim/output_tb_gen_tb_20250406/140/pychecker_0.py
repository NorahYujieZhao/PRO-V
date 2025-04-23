
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed - purely combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Truth table mapping cd inputs to mux_in outputs
        _TRUTH_TABLE = {
            '00': '0001',  # cd=00 -> mux_in for ab=00,01,11,10
            '01': '1000',  # cd=01 -> mux_in for ab=00,01,11,10
            '11': '1011',  # cd=11 -> mux_in for ab=00,01,11,10
            '10': '1001'   # cd=10 -> mux_in for ab=00,01,11,10
        }

        # Get input values
        c = stimulus_dict['c']
        d = stimulus_dict['d']
        
        # Combine inputs to form lookup key
        key = c + d
        
        # Get mux_in value from truth table
        mux_in = _TRUTH_TABLE[key]

        return {'mux_in': mux_in}
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


