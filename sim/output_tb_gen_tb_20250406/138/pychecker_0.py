
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
        sum_outputs = []
        cout_outputs = []
        
        # Process each input stimulus
        for stimulus in stimulus_dict['input variable']:
            # Convert binary string inputs to integers
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            cin = int(stimulus['cin'])
            
            # Calculate sum using XOR operations
            sum_out = a ^ b ^ cin
            
            # Calculate carry-out
            cout = (a & b) | (cin & (a ^ b))
            
            # Append results to output lists
            sum_outputs.append(str(sum_out))
            cout_outputs.append(str(cout))
        
        # Format output dictionary
        output_dict = {
            'scenario': stimulus_dict['scenario'],
            'output variable': [
                {'sum': sum_out, 'cout': cout_out}
                for sum_out, cout_out in zip(sum_outputs, cout_outputs)
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

