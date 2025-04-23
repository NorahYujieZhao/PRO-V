
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed - purely combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Get input values
        c = stimulus_dict['c']
        d = stimulus_dict['d']
        
        # Create 4-bit output based on c,d inputs
        # mux_in[0] (ab=00): cd=00->0, cd=01->1, cd=11->1, cd=10->1
        mux_in0 = '1' if (c == '0' and d == '1') or (c == '1') else '0'
        
        # mux_in[1] (ab=01): cd=00->0, cd=01->0, cd=11->0, cd=10->0
        mux_in1 = '0'
        
        # mux_in[2] (ab=11): cd=00->0, cd=01->0, cd=11->1, cd=10->0
        mux_in2 = '1' if (c == '1' and d == '1') else '0'
        
        # mux_in[3] (ab=10): cd=00->1, cd=01->0, cd=11->1, cd=10->1
        mux_in3 = '1' if (c == '0' and d == '0') or (c == '1' and d == '1') or (c == '1' and d == '0') else '0'
        
        # Combine outputs into 4-bit vector
        mux_in = mux_in3 + mux_in2 + mux_in1 + mux_in0
        
        return {'mux_in': mux_in}
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


