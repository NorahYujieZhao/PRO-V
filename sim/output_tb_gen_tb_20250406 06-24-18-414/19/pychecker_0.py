
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
        Process input stimuli and generate corresponding outputs.
        Args:
            stimulus_dict: Dictionary containing input stimuli
        Returns:
            Dictionary containing output values
        '''
        output_list = []

        # Process each input stimulus
        for stimulus in stimulus_dict['input variable']:
            # Convert binary string input to integer
            in_val = int(stimulus['in'], 2)
            
            # Extract upper and lower bytes
            out_hi = (in_val >> 8) & 0xFF  # Bits [15:8]
            out_lo = in_val & 0xFF         # Bits [7:0]
            
            # Format outputs as 8-bit binary strings
            out_hi_bin = format(out_hi, '08b')
            out_lo_bin = format(out_lo, '08b')
            
            # Add to output list
            output_list.append({
                'out_hi': out_hi_bin,
                'out_lo': out_lo_bin
            })

        # Return formatted output dictionary
        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': output_list
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

