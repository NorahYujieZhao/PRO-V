
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational circuit, so no state initialization needed.
        '''
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process input stimuli and compute sum and overflow for 8-bit signed addition
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert binary strings to integers
            a = int(stimulus['a'], 2)
            b = int(stimulus['b'], 2)
            
            # Convert to signed 8-bit values
            if a & 0x80:
                a = -(256 - a)
            if b & 0x80:
                b = -(256 - b)
            
            # Compute sum
            s = (a + b) & 0xFF
            
            # Detect overflow
            # Overflow occurs when:
            # 1. Both inputs positive but sum is negative
            # 2. Both inputs negative but sum is positive
            a_pos = a >= 0
            b_pos = b >= 0
            s_pos = (s & 0x80) == 0
            
            overflow = (a_pos and b_pos and not s_pos) or \
                      (not a_pos and not b_pos and s_pos)
            
            # Format output as binary strings
            s_bin = format(s, '08b')
            overflow_bin = '1' if overflow else '0'
            
            outputs.append({
                's': s_bin,
                'overflow': overflow_bin
            })
        
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

