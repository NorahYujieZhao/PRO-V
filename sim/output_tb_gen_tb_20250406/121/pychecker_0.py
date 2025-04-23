
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass
        
    def load(self, stimulus_dict: Dict[str, any]):
        # Get 4-bit input value
        in_bits = stimulus_dict['in']
        
        # Convert input to position
        if in_bits[0] == '1':    # MSB (in[3])
            pos = '11'           # Position 3
        elif in_bits[1] == '1':  # in[2]
            pos = '10'           # Position 2
        elif in_bits[2] == '1':  # in[1] 
            pos = '01'           # Position 1
        elif in_bits[3] == '1':  # LSB (in[0])
            pos = '00'           # Position 0
        else:                    # All zeros
            pos = '00'           # Default position 0
            
        return {'pos': pos}
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


