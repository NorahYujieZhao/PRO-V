
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state to OFF (0)
        '''
        self.state = 0  # 0=OFF, 1=ON

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Handle state transitions and output generation
        '''
        # Convert input signals from binary strings to integers
        j_val = int(stimulus_dict['j'], 2)
        k_val = int(stimulus_dict['k'], 2)
        areset_val = int(stimulus_dict['areset'], 2)

        # Handle asynchronous reset
        if areset_val == 1:
            self.state = 0  # Reset to OFF state
        # Handle state transitions on rising clock edge
        elif clk == 1:
            if self.state == 0:  # OFF state
                if j_val == 1:
                    self.state = 1  # Move to ON state
            else:  # ON state
                if k_val == 1:
                    self.state = 0  # Move to OFF state

        # Output depends only on current state (Moore machine)
        out_val = '1' if self.state == 1 else '0'

        return {'out': out_val}

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


