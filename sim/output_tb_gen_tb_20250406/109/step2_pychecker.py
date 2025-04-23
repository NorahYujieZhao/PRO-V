
import json
from typing import Dict, List, Union

class GoldenDUT:
    def __init__(self):
        # No internal state needed - purely combinational logic
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        # Get input binary string
        in_str = stimulus_dict['in']
        assert len(in_str) == 100, 'Input must be 100 bits'
        
        # Create input dictionary
        in_dict = {f'in[{99 - i}]': int(b) for i, b in enumerate(in_str)}
        
        # Calculate out_both[98:0]
        out_both = []
        for i in range(98, -1, -1):  # 98 down to 0
            if in_dict[f'in[{i}]'] == 1 and in_dict[f'in[{i+1}]'] == 1:
                out_both.append('1')
            else:
                out_both.append('0')
                
        # Calculate out_any[99:1]
        out_any = []
        for i in range(99, 0, -1):  # 99 down to 1
            if in_dict[f'in[{i}]'] == 1 or in_dict[f'in[{i-1}]'] == 1:
                out_any.append('1')
            else:
                out_any.append('0')
                
        # Calculate out_different[99:0] with wrap-around
        out_different = []
        for i in range(99, -1, -1):  # 99 down to 0
            right_neighbor = i - 1 if i > 0 else 99  # Wrap around for first bit
            if in_dict[f'in[{i}]'] != in_dict[f'in[{right_neighbor}]']:
                out_different.append('1')
            else:
                out_different.append('0')
                
        return {
            'out_both': ''.join(out_both),
            'out_any': ''.join(out_any),
            'out_different': ''.join(out_different)
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


