
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational logic circuit, so no state registers needed.
        '''
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process input stimuli and compute pairwise comparisons.
        Returns dictionary with 25-bit output vector.
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs to integers
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            c = int(stimulus['c'])
            d = int(stimulus['d'])
            e = int(stimulus['e'])
            
            # Initialize output vector
            out = 0
            
            # Compute all 25 comparisons
            inputs = [a, b, c, d, e]
            bit_pos = 24
            
            # Compare each input with all inputs (including itself)
            for i in range(5):
                for j in range(5):
                    # XNOR operation: ~(inputs[i] ^ inputs[j])
                    comparison = ~(inputs[i] ^ inputs[j]) & 1
                    # Set the corresponding bit in output
                    out |= (comparison << bit_pos)
                    bit_pos -= 1
            
            # Format output as 25-bit binary string
            out_str = format(out, '025b')
            outputs.append({'out': out_str})
        
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

