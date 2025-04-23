
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational circuit, so no state registers needed.
        '''
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Implements a 16-bit 9-to-1 multiplexer functionality
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert binary string inputs to integers
            a = int(stimulus['a'], 2)
            b = int(stimulus['b'], 2)
            c = int(stimulus['c'], 2)
            d = int(stimulus['d'], 2)
            e = int(stimulus['e'], 2)
            f = int(stimulus['f'], 2)
            g = int(stimulus['g'], 2)
            h = int(stimulus['h'], 2)
            i = int(stimulus['i'], 2)
            sel = int(stimulus['sel'], 2)
            
            # Implement multiplexer logic
            if sel == 0:
                out = a
            elif sel == 1:
                out = b
            elif sel == 2:
                out = c
            elif sel == 3:
                out = d
            elif sel == 4:
                out = e
            elif sel == 5:
                out = f
            elif sel == 6:
                out = g
            elif sel == 7:
                out = h
            elif sel == 8:
                out = i
            else:  # sel = 9 to 15
                out = 0xFFFF
            
            # Convert output to 16-bit binary string
            out_binary = format(out & 0xFFFF, '016b')
            outputs.append({'out': out_binary})
        
        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': outputs
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

