
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state variables
        '''
        pass

    def load(self, clk, stimulus_dict: Dict[str, str]):
        '''
        Implement FSM logic for Y1 and Y3
        '''
        # Get current state and input
        y = int(stimulus_dict['y'], 2)
        w = int(stimulus_dict['w'], 2)

        # One-hot state definitions
        STATE_A = 0b000001
        STATE_B = 0b000010
        STATE_C = 0b000100
        STATE_D = 0b001000
        STATE_E = 0b010000
        STATE_F = 0b100000

        # Y1 logic: Y1 is 1 only when in state A and w=1
        Y1 = 1 if (y == STATE_A and w == 1) else 0

        # Y3 logic: Y3 is 1 when in states B,C,E,F and w=0
        Y3 = 1 if ((y == STATE_B or y == STATE_C or y == STATE_E or y == STATE_F) and w == 0) else 0

        # Return outputs as binary strings
        return {
            'Y1': format(Y1, 'b'),
            'Y3': format(Y3, 'b')
        }
def check_output(stimulus_list_scenario):

    dut = GoldenDUT()
    tb_outputs = []


    for stimulus_list in stimulus_list_scenario["input variable"]:


        clock_cycles = stimulus_list['clock cycles']
        clk = 1
        input_vars_list = {k: v for k, v in stimulus_list.items() if k != "clock cycles"}
        output_vars_list = {'clock cycles':clock_cycles}

        for i in range(clock_cycles):
            input_vars = {k:v[i] for k,v in input_vars_list.items()}

            output_vars = dut.load(clk,input_vars)
            for k,v in output_vars.items():
                if k not in output_vars_list:
                    output_vars_list[k] = []
                output_vars_list[k].append(v)
            


        tb_outputs.append(output_vars_list)

    return tb_outputs

if __name__ == "__main__":

    with open("stimulus.json", "r") as f:
        stimulus_data = json.load(f)


    if isinstance(stimulus_data, dict):
        stimulus_list_scenarios = stimulus_data.get("input variable", [])
    else:
        stimulus_list_scenarios = stimulus_data

    outputs=[]
    for stimulus_list_scenario in stimulus_list_scenarios:
        outputs.append( check_output(stimulus_list_scenario))

    print(json.dumps(outputs, indent=2))


