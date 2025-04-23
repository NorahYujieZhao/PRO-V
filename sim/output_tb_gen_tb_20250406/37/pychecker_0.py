
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        No state registers needed for this combinational logic.
        '''
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process input stimuli and generate corresponding outputs
        for the 8-bit priority encoder.
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input binary string to integer
            in_val = int(stimulus['in'], 2)
            
            # Find position of least significant 1
            pos = 0
            if in_val != 0:
                for i in range(8):
                    if in_val & (1 << i):
                        pos = i
                        break
            
            # Add output to results list
            outputs.append({"pos": format(pos, '03b')})
        
        return {
            "scenario": stimulus_dict['scenario'],
            "output variable": outputs
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

