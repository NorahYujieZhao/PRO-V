
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational logic
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        out_sop_list = []
        out_pos_list = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs to integers
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            c = int(stimulus['c'])
            d = int(stimulus['d'])
            
            # Convert inputs to decimal number
            input_val = (a << 3) | (b << 2) | (c << 1) | d
            
            # Check if input is valid (not 3,8,11,12)
            invalid_inputs = {3, 8, 11, 12}
            if input_val in invalid_inputs:
                out_sop = 'x'
                out_pos = 'x'
            else:
                # Output 1 for 2,7,15
                # Output 0 for 0,1,4,5,6,9,10,13,14
                out_sop = 1 if input_val in {2, 7, 15} else 0
                out_pos = out_sop  # Both forms will give same result
            
            out_sop_list.append(out_sop)
            out_pos_list.append(out_pos)
        
        output_dict = {
            "scenario": stimulus_dict['scenario'],
            "output variable": [
                {"out_sop": str(out_sop),
                 "out_pos": str(out_pos)}
                for out_sop, out_pos in zip(out_sop_list, out_pos_list)
            ]
        }
        
        return output_dict
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

