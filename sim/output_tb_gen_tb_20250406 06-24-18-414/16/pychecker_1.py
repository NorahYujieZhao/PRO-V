
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        No state initialization needed as this is combinational logic
        '''
        pass

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Implements the FSM combinational logic for Y1 and Y3
        '''
        # Convert inputs to integers
        y_str = stimulus_dict['y']
        w_str = stimulus_dict['w']
        
        y_val = int(y_str, 2)
        w_val = int(w_str, 2)
        
        # Calculate Y1 (next state for bit 1 - state B)
        # Y1 is 1 only when in state A (000001) and w=1
        Y1 = 1 if (y_val == 0b000001 and w_val == 1) else 0
        
        # Calculate Y3 (next state for bit 3 - state D)
        # Y3 is 1 when in states B,C,E,F with w=0
        Y3 = 1 if ((y_val == 0b000010 or    # State B
                    y_val == 0b000100 or    # State C
                    y_val == 0b010000 or    # State E
                    y_val == 0b100000) and  # State F
                   w_val == 0) else 0
        
        # Convert outputs to binary strings
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


