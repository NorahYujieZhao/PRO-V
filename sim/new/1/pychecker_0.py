
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational circuit, so no state registers are needed.
        '''
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Implements 2-1 multiplexer functionality
        Returns output based on selector value
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert binary string inputs to integers
            a = int(stimulus['a'], 2)
            b = int(stimulus['b'], 2)
            sel = int(stimulus['sel'])
            
            # Implement multiplexer logic
            out = a if sel == 0 else b
            
            # Convert output back to 100-bit binary string
            out_bin = format(out, '0100b')
            
            # Add to outputs list
            outputs.append({"out": out_bin})
        
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

