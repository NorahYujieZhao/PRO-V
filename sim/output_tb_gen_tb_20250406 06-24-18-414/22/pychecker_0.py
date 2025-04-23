
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed - purely combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Get inputs
        y_str = stimulus_dict['y']
        w = stimulus_dict['w']
        
        # Convert y to dict with indices [6:1]
        y_dict = {f"[{6-i}]": int(b) for i, b in enumerate(y_str)}
        
        # Y2 (next state B) = 1 when in state A and w=0
        Y2 = '1' if y_dict['[1]'] == 1 and w == '0' else '0'
        
        # Y4 (next state E) = 1 when:
        # - in state C and w=0, OR
        # - in state E and w=0
        Y4 = '1' if ((y_dict['[3]'] == 1 or y_dict['[5]'] == 1) and w == '0') else '0'
        
        return {
            'Y2': Y2,
            'Y4': Y4
        }
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
        for input_vars in stimulus:

            outputs = check_output(input_vars)
            scenario_outputs.append(outputs)
        tb_outputs.append(scenario_outputs)


    

    print(json.dumps(tb_outputs, indent=2))


