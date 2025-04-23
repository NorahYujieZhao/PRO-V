
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This module has both combinational and sequential logic.
        '''
        # Initialize internal registers
        self.out_always = 0
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process inputs and generate outputs according to 2-to-1 mux logic
        '''
        out_assign_list = []
        out_always_list = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs from strings to integers
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            sel_b1 = int(stimulus['sel_b1'])
            sel_b2 = int(stimulus['sel_b2'])
            
            # Combinational logic for out_assign
            # Select b only when both sel_b1 and sel_b2 are 1
            out_assign = b if (sel_b1 and sel_b2) else a
            
            # Procedural logic for out_always
            if sel_b1 and sel_b2:
                self.out_always = b
            else:
                self.out_always = a
            
            # Append results to output lists
            out_assign_list.append(out_assign)
            out_always_list.append(self.out_always)
        
        # Format output dictionary
        output_dict = {
            "scenario": stimulus_dict['scenario'],
            "output variable": [
                {"out_assign": str(val),
                 "out_always": str(val2)} 
                for val, val2 in zip(out_assign_list, out_always_list)
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

