
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state to B (1) as per reset condition
        '''
        self.state = 1  # 1=B, 0=A

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state machine based on inputs
        '''
        # Convert inputs from binary strings
        areset = int(stimulus_dict['areset'], 2)
        in_val = int(stimulus_dict['in'], 2)
        
        # Handle async reset
        if areset:
            self.state = 1  # Go to state B
        # State transitions on clock edge
        elif clk == 1:
            if self.state == 0:  # Currently in state A
                self.state = 1 if in_val == 0 else 0
            else:  # Currently in state B
                self.state = 0 if in_val == 0 else 1
        
        # Moore output depends only on current state
        return {'out': format(self.state, 'b')}
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


