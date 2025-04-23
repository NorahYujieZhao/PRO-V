
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the flip-flop output to 0
        '''
        self.q = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update flip-flop state based on inputs
        '''
        # Convert input binary strings to integers
        d_val = int(stimulus_dict['d'], 2)
        ar_val = int(stimulus_dict['ar'], 2)

        # Handle asynchronous reset
        if ar_val == 1:
            self.q = 0
        # On positive clock edge, update q with d if not in reset
        elif clk == 1:
            self.q = d_val

        # Convert output to binary string
        q_str = format(self.q, 'b')

        # Return the output dictionary
        return {'q': q_str}

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


