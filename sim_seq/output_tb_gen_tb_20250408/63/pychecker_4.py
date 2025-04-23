
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize Q to 0
        '''
        self.Q = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Implement JK flip-flop logic
        '''
        # Convert input binary strings to integers
        j_val = int(stimulus_dict['j'], 2)
        k_val = int(stimulus_dict['k'], 2)

        # Only update on rising clock edge
        if clk == 1:
            if j_val == 0 and k_val == 0:
                # Hold state
                pass
            elif j_val == 0 and k_val == 1:
                # Reset
                self.Q = 0
            elif j_val == 1 and k_val == 0:
                # Set
                self.Q = 1
            else:  # j_val == 1 and k_val == 1
                # Toggle
                self.Q = 1 if self.Q == 0 else 0

        # Return output as binary string
        return {'Q': format(self.Q, 'b')}
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


