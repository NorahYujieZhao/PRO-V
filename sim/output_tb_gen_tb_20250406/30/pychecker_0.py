
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed for combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Extract input signals
        sel = int(stimulus_dict['sel'])
        a = stimulus_dict['a']  # 8-bit input
        b = stimulus_dict['b']  # 8-bit input
        
        # Convert input strings to integers
        a_val = int(a, 2)
        b_val = int(b, 2)
        
        # Implement 2-to-1 mux logic
        # When sel=0, choose a; when sel=1, choose b
        result = b_val if sel else a_val
        
        # Convert result back to 8-bit binary string
        out = format(result, '08b')
        
        return {'out': out}

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


