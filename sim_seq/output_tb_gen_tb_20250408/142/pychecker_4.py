
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the state flip-flop to 0
        '''
        self.state = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state and outputs based on inputs
        '''
        # Convert input strings to integers
        a_val = int(stimulus_dict['a'], 2)
        b_val = int(stimulus_dict['b'], 2)
        
        # State update on rising clock edge
        if clk == 1:
            if a_val == 1 and b_val == 1:
                # Toggle state when a=1 and b=1
                self.state = 1 if self.state == 0 else 0
        
        # Combinational output logic for q
        # q is 1 when:
        # - state is 0 and ((a=0 and b=1) or (a=1 and b=0))
        # - state is 1 and (a=0 or b=0)
        if self.state == 0:
            q = (not a_val and b_val) or (a_val and not b_val)
        else:
            q = not (a_val and b_val)
            
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


