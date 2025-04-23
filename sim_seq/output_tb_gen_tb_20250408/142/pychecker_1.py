
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize internal state register
        '''
        self.state = 0  # Internal state bit

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state and compute outputs based on inputs
        '''
        # Convert input strings to integers
        a = int(stimulus_dict['a'], 2)
        b = int(stimulus_dict['b'], 2)

        # Compute next state on rising clock edge
        if clk == 1:
            if a == 0 and b == 0:
                self.state = 0
            elif a == 1 and b == 1:
                self.state = not self.state

        # Compute output q based on current inputs and state
        if a == 0 and b == 0:
            q = self.state
        elif a == 1 and b == 1:
            q = self.state
        elif (a == 0 and b == 1) or (a == 1 and b == 0):
            q = not self.state
        else:
            q = self.state

        # Convert outputs to binary strings
        q_str = '1' if q else '0'
        state_str = '1' if self.state else '0'

        return {
            'q': q_str,
            'state': state_str
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


