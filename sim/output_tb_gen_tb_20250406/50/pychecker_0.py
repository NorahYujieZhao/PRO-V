
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
        Process input stimuli and generate outputs according to the specification.
        '''
        stimulus_outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input string to integer
            in_val = int(stimulus['in'], 2)
            
            # Calculate out_both[2:0]
            # Check if current bit and left neighbor are both 1
            out_both = 0
            for i in range(3):
                if ((in_val >> i) & 1) and ((in_val >> (i+1)) & 1):
                    out_both |= (1 << i)
            
            # Calculate out_any[3:1]
            # Check if current bit or right neighbor are 1
            out_any = 0
            for i in range(1, 4):
                if ((in_val >> i) & 1) or ((in_val >> (i-1)) & 1):
                    out_any |= (1 << i)
            
            # Calculate out_different[3:0]
            # Check if current bit differs from left neighbor (wrapping)
            out_different = 0
            for i in range(4):
                left_neighbor = (in_val >> ((i+1) % 4)) & 1
                current_bit = (in_val >> i) & 1
                if current_bit != left_neighbor:
                    out_different |= (1 << i)
            
            # Format outputs as binary strings
            out_both_str = format(out_both, '03b')
            out_any_str = format(out_any >> 1, '03b')
            out_different_str = format(out_different, '04b')
            
            # Add to output list
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

