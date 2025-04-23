
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
        Process inputs and generate outputs according to 256-to-1 4-bit multiplexer logic
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input binary string to integer
            in_val = int(stimulus['in'], 2)
            sel = int(stimulus['sel'], 2)
            
            # Calculate starting bit position
            start_pos = sel * 4
            
            # Extract 4 bits from the input
            # Shift right to remove lower bits, then mask with 0xF to get only 4 bits
            out_val = (in_val >> start_pos) & 0xF
            
            # Convert to 4-bit binary string
            out_str = format(out_val, '04b')
            
            # Add to outputs
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

