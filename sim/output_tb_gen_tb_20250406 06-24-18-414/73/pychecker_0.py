
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        This is a combinational circuit, so no state initialization needed.
        '''
        pass

    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process inputs and generate outputs according to 6-to-1 multiplexer logic
        '''
        outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert all inputs from binary strings to integers
            sel = int(stimulus['sel'], 2)
            data0 = int(stimulus['data0'], 2)
            data1 = int(stimulus['data1'], 2)
            data2 = int(stimulus['data2'], 2)
            data3 = int(stimulus['data3'], 2)
            data4 = int(stimulus['data4'], 2)
            data5 = int(stimulus['data5'], 2)
            
            # Implement multiplexer logic
            if sel == 0:
                out = data0
            elif sel == 1:
                out = data1
            elif sel == 2:
                out = data2
            elif sel == 3:
                out = data3
            elif sel == 4:
                out = data4
            elif sel == 5:
                out = data5
            else:
                out = 0
            
            # Format output as 4-bit binary string
            out_str = format(out & 0xF, '04b')
            outputs.append({"out": out_str})
        
        return {
            "scenario": stimulus_dict['scenario'],
            "output variable": outputs
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

