
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed - purely combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Truth table for computing Y2 (bit 2 of next state)
        # Key = current state (y3y2y1) + input w
        # Value = Y2 of next state
        _TRUTH_TABLE = {
            '0000': '0',  # A + w=0 -> B
            '0001': '0',  # A + w=1 -> A
            '0010': '0',  # B + w=0 -> C
            '0011': '0',  # B + w=1 -> D
            '0100': '1',  # C + w=0 -> E
            '0101': '0',  # C + w=1 -> D
            '0110': '1',  # D + w=0 -> F
            '0111': '0',  # D + w=1 -> A
            '1000': '1',  # E + w=0 -> E
            '1001': '0',  # E + w=1 -> D
            '1010': '0',  # F + w=0 -> C
            '1011': '0'   # F + w=1 -> D
        }

        y_bits = stimulus_dict['y']  # e.g., '010'
        w_bit = stimulus_dict['w']   # e.g., '1'
        
        key = y_bits + w_bit
        Y2 = _TRUTH_TABLE[key]

        return {'Y2': Y2}
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


