
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        Each internal register/state variable must align with the module header.
        Explicitly initialize these states according to the RTL specification.
        '''
        # This is a combinational circuit, no state initialization needed
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        '''
        stimulus_dict: a dictionary formatted as shown above.
        Parse each input variable and use it to perform RTL state updates.
        Returns a dictionary of the outputs aligned with the RTL module outputs.
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert inputs from binary strings to integers
            do_sub = int(stimulus['do_sub'])
            a = int(stimulus['a'], 2)
            b = int(stimulus['b'], 2)
            
            # Perform addition or subtraction
            if do_sub == 0:
                out = (a + b) & 0xFF  # 8-bit addition with overflow handling
            else:
                out = (a - b) & 0xFF  # 8-bit subtraction with overflow handling
            
            # Set zero flag
            result_is_zero = 1 if out == 0 else 0
            
            # Format output as binary strings
            out_bin = format(out, '08b')
            
            # Add to outputs list
            outputs.append({
                'out': out_bin,
                'result_is_zero': str(result_is_zero)
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

