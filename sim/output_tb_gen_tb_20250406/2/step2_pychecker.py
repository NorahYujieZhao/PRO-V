
import json
from typing import Dict, List, Union

class GoldenDUT:
    def __init__(self):
        # No internal state needed - purely combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Truth table for computing Y2 (middle bit of next state)
        # Key = current state (y3y2y1) + input w
        # Value = y2 of next state
        _TRUTH_TABLE = {
            # State A (000)
            '0000': '0',  # A + w=0 → B (001)
            '0001': '0',  # A + w=1 → A (000)
            
            # State B (001)
            '0010': '1',  # B + w=0 → C (010)
            '0011': '1',  # B + w=1 → D (011)
            
            # State C (010)
            '0100': '0',  # C + w=0 → E (100)
            '0101': '1',  # C + w=1 → D (011)
            
            # State D (011)
            '0110': '0',  # D + w=0 → F (101)
            '0111': '0',  # D + w=1 → A (000)
            
            # State E (100)
            '1000': '0',  # E + w=0 → E (100)
            '1001': '1',  # E + w=1 → D (011)
            
            # State F (101)
            '1010': '1',  # F + w=0 → C (010)
            '1011': '1',  # F + w=1 → D (011)
        }

        y_bits = stimulus_dict['y']  # Get 3 state bits
        w_bit = stimulus_dict['w']   # Get input bit
        
        # Combine state and input bits to form lookup key
        key = y_bits + w_bit
        
        # Look up Y2 (next state y[2]) in truth table
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


