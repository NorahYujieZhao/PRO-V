
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass
        
    def load(self, stimulus_dict: Dict[str, any]):
        # Get 4-bit input value
        in_str = stimulus_dict['in']
        
        # Convert to dictionary mapping positions
        in_dict = {f'in[{3-i}]': int(b) for i, b in enumerate(in_str)}
        
        # Find position of leftmost 1 bit
        pos = '00'  # Default if no 1s found
        if in_dict['in[3]'] == 1:
            pos = '11'  # Position 3
        elif in_dict['in[2]'] == 1:
            pos = '10'  # Position 2
        elif in_dict['in[1]'] == 1:
            pos = '01'  # Position 1
        elif in_dict['in[0]'] == 1:
            pos = '00'  # Position 0
            
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


