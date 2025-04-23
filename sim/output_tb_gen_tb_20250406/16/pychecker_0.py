
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed - purely combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Extract inputs
        y_bits = stimulus_dict['y']  # 6-bit one-hot state
        w_bit = stimulus_dict['w']   # input bit
        
        # Convert to integers
        y = int(y_bits, 2)
        w = int(w_bit, 2)
        
        # Y1 logic: y[1] will be 1 when in state A (y[0]=1) and w=1
        Y1 = '1' if (y & 0b000001) and w else '0'
        
        # Y3 logic: y[3] will be 1 when in states B,C,E,F (y[1],y[2],y[4],y[5]=1) and w=0
        Y3 = '1' if (y & 0b110110) and not w else '0'
        
        return {
            'Y1': Y1,
            'Y3': Y3
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
        for cycle in stimulus:

            outputs = check_output(cycle)
            scenario_outputs.append(outputs)
        tb_outputs.append(scenario_outputs)


    

    print(json.dumps(tb_outputs, indent=2))


