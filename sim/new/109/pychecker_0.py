
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for this combinational logic
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input binary string to list of bits
            in_bits = [int(b) for b in stimulus['in']]
            
            # Calculate out_both[98:0]
            # Check if current bit and left neighbor are both 1
            out_both = [(in_bits[i] & in_bits[i+1]) for i in range(99)]
            
            # Calculate out_any[99:1]
            # Check if current bit or right neighbor are 1
            out_any = [(in_bits[i] | in_bits[i-1]) for i in range(1, 100)]
            
            # Calculate out_different[99:0]
            # Check if current bit differs from left neighbor (with wrap)
            out_different = []
            for i in range(100):
                left_neighbor = in_bits[0] if i == 99 else in_bits[i+1]
                out_different.append(in_bits[i] ^ left_neighbor)
            
            # Convert results to binary strings
            out_both_str = ''.join(str(b) for b in out_both)
            out_any_str = ''.join(str(b) for b in out_any)
            out_different_str = ''.join(str(b) for b in out_different)
            
            stimulus_outputs.append({
                'out_both': out_both_str,
                'out_any': out_any_str,
                'out_different': out_different_str
            })
        
        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': stimulus_outputs
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

