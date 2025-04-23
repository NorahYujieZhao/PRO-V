
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Initialize output q to 0
        self.q = 0

    def load(self, stimulus_dict: Dict[str, any]):
        # Get input values
        d = int(stimulus_dict['d'])
        ena = int(stimulus_dict['ena'])
        
        # Update q only when ena is 1
        if ena:
            self.q = d
            
        # Return output as dictionary with binary string
        return {'q': str(self.q)}
def check_output(stimulus):

    dut = GoldenDUT()


        

    return dut.load(stimulus)

if __name__ == "__main__":

    with open("stimulus.json", "r") as f:
        stimulus_data = json.load(f)

    stimulus_list = []
    for stimulus in stimulus_data:
        stimulus_list.append(stimulus['input variable'])

    tb_outputs = []
    for stimulus in stimulus_list:
        scenario_outputs=[]
        for cycle in stimulus:

            outputs = check_output(cycle)
            scenario_outputs.append(outputs)
        tb_outputs.append(scenario_outputs)


    

    print(json.dumps(tb_outputs, indent=2))


