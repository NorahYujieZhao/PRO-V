
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed - combinational logic only
        pass
        
    def load(self, stimulus_dict: Dict[str, any]):
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Parse inputs
            d = int(stimulus['d'])
            done_counting = int(stimulus['done_counting']) 
            ack = int(stimulus['ack'])
            state = int(stimulus['state'], 2)  # Convert binary string to int
            
            # Extract individual state bits
            S = (state & 0b0000000001) != 0
            S1 = (state & 0b0000000010) != 0  
            S11 = (state & 0b0000000100) != 0
            S110 = (state & 0b0000001000) != 0
            B0 = (state & 0b0000010000) != 0
            B1 = (state & 0b0000100000) != 0
            B2 = (state & 0b0001000000) != 0
            B3 = (state & 0b0010000000) != 0
            Count = (state & 0b0100000000) != 0
            Wait = (state & 0b1000000000) != 0
            
            # Calculate next states
            B3_next = B2
            S_next = (S and not d) or (S1 and not d) or (S110 and not d) or (Wait and ack)
            S1_next = S and d
            Count_next = B3 or (Count and not done_counting)
            Wait_next = (Count and done_counting) or (Wait and not ack)
            
            # Calculate outputs
            shift_ena = B0 or B1 or B2 or B3
            counting = Count
            done = Wait
            
            # Convert to binary strings
            output = {
                'B3_next': '1' if B3_next else '0',
                'S_next': '1' if S_next else '0',
                'S1_next': '1' if S1_next else '0', 
                'Count_next': '1' if Count_next else '0',
                'Wait_next': '1' if Wait_next else '0',
                'done': '1' if done else '0',
                'counting': '1' if counting else '0',
                'shift_ena': '1' if shift_ena else '0'
            }
            
            outputs.append(output)
            
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

