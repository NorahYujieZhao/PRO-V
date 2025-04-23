
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational circuit, so no state registers are needed.
        '''
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process input stimuli and generate outputs according to AND gate logic.
        Args:
            stimulus_dict: Dictionary containing input stimuli
        Returns:
            Dictionary containing output values
        '''
        # Initialize output list
        output_q = []
        
        # Process each input stimulus
        for stimulus in stimulus_dict['input variable']:
            # Convert input strings to integers
            a = int(stimulus['a'])
            b = int(stimulus['b'])
            
            # Implement AND gate logic
            q = 1 if (a == 1 and b == 1) else 0
            
            # Add result to output list
            output_q.append({'q': str(q)})
        
        # Format output dictionary
        output_dict = {
            'scenario': stimulus_dict['scenario'],
            'output variable': output_q
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

