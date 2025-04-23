
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
        stimulus_outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input binary string to integer
            in_val = int(stimulus['in'], 2)
            
            # Extract bytes using masks and shifts
            byte3 = (in_val >> 24) & 0xFF  # bits 31:24
            byte2 = (in_val >> 16) & 0xFF  # bits 23:16
            byte1 = (in_val >> 8) & 0xFF   # bits 15:8
            byte0 = in_val & 0xFF          # bits 7:0
            
            # Reconstruct output with reversed byte order
            out_val = (byte0 << 24) | (byte1 << 16) | (byte2 << 8) | byte3
            
            # Convert to 32-bit binary string
            out_bin = format(out_val, '032b')
            
            # Add to output list
            stimulus_outputs.append({'out': out_bin})
        
        output_dict = {
            'scenario': stimulus_dict['scenario'],
            'output variable': stimulus_outputs
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

