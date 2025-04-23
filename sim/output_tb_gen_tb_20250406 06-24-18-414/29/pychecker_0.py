
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        Each internal register/state variable must align with the module header.
        Explicitly initialize these states according to the RTL specification.
        '''
        # This is a combinational circuit, no state registers needed
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        stimulus_dict: a dictionary formatted as shown above.
        Parse each input variable and use it to perform RTL state updates.
        Returns a dictionary of the outputs aligned with the RTL module outputs.
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert binary string inputs to integers
            a = int(stimulus['a'], 2)
            b = int(stimulus['b'], 2)
            c = int(stimulus['c'], 2)
            d = int(stimulus['d'], 2)
            e = int(stimulus['e'], 2)
            
            # Implement multiplexer logic based on c value
            if c == 0:
                q = b
            elif c == 1:
                q = e
            elif c == 2:
                q = a
            elif c == 3:
                q = d
            else:
                q = 0xf  # All 1s for c >= 4
            
            # Format output as 4-bit binary string
            q_bin = format(q & 0xf, '04b')
            outputs.append({"q": q_bin})
        
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

