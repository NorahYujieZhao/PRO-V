
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state registers needed as this is combinational logic
        pass
    
    def module_a(self, x, y):
        # z = (x^y) & x
        return (x ^ y) & x
    
    def module_b(self, x, y):
        # Implementing the waveform behavior
        if x == 0 and y == 0:
            return 1
        elif x == 1 and y == 1:
            return 1
        else:
            return 0
    
    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Extract inputs
            x = int(stimulus['x'])
            y = int(stimulus['y'])
            
            # Calculate outputs of A modules
            a1_out = self.module_a(x, y)
            a2_out = self.module_a(x, y)
            
            # Calculate outputs of B modules
            b1_out = self.module_b(x, y)
            b2_out = self.module_b(x, y)
            
            # OR gate between A1 and B1
            or_out = a1_out | b1_out
            
            # AND gate between A2 and B2
            and_out = a2_out & b2_out
            
            # Final XOR
            z = or_out ^ and_out
            
            stimulus_outputs.append({"z": str(z)})
        
        return {
            "scenario": stimulus_dict['scenario'],
            "output variable": stimulus_outputs
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

