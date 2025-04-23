
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational logic
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs to integers
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            c = int(stimulus['c'])
            d = int(stimulus['d'])
            
            # Implement the logic function based on the truth table
            # This is derived from analyzing the waveform patterns
            q = ((not a and not b and not c and not d) or
                 (not a and not b and c and d) or
                 (not a and b and not c and d) or
                 (not a and b and c and not d) or
                 (a and not b and not c and d) or
                 (a and not b and c and not d) or
                 (a and b and not c and not d) or
                 (a and b and c and d))
            
            # Convert boolean result to integer
            q_int = 1 if q else 0
            
            # Add to output list
            stimulus_outputs.append({"q": str(q_int)})
        
        output_dict = {
            "scenario": stimulus_dict['scenario'],
            "output variable": stimulus_outputs
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

