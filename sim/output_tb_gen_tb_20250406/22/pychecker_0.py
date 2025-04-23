
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed - purely combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Truth table for Y2 and Y4 outputs based on one-hot encoded current state and input w
        # Key format: y[6:1] + w
        # Values: Y2,Y4 outputs
        _TRUTH_TABLE = {
            '000001' + '0': ('1','0'),  # A->B when w=0
            '000001' + '1': ('0','0'),  # A->A when w=1
            '000010' + '0': ('0','0'),  # B->C when w=0
            '000010' + '1': ('0','1'),  # B->D when w=1
            '000100' + '0': ('0','0'),  # C->E when w=0
            '000100' + '1': ('0','1'),  # C->D when w=1
            '001000' + '0': ('0','0'),  # D->F when w=0
            '001000' + '1': ('0','0'),  # D->A when w=1
            '010000' + '0': ('0','0'),  # E->E when w=0
            '010000' + '1': ('0','1'),  # E->D when w=1
            '100000' + '0': ('0','0'),  # F->C when w=0
            '100000' + '1': ('0','1')   # F->D when w=1
        }

        # Get current state and input
        y_bits = stimulus_dict['y']  # 6 bits
        w_bit = stimulus_dict['w']   # 1 bit

        # Lookup outputs
        key = y_bits + w_bit
        Y2, Y4 = _TRUTH_TABLE[key]

        return {'Y2': Y2, 'Y4': Y4}
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


