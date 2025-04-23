
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
        # Initialize output lists
        out_list = []
        out_n_list = []
        
        # Process each input stimulus
        for stimulus in stimulus_dict['input variable']:
            # Convert input strings to integers
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            c = int(stimulus['c'])
            d = int(stimulus['d'])
            
            # Implement the logic
            and1 = a & b  # First AND gate
            and2 = c & d  # Second AND gate
            out = and1 | and2  # OR gate
            out_n = not out  # NOT gate
            
            # Convert boolean to integer
            out_list.append(1 if out else 0)
            out_n_list.append(1 if out_n else 0)
        
        # Create output dictionary
        output_dict = {
            "scenario": stimulus_dict['scenario'],
            "output variable": [
                {"out": str(out_val),
                 "out_n": str(out_n_val)}
                for out_val, out_n_val in zip(out_list, out_n_list)
            ]
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

