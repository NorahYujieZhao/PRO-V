
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''Initialize internal state'''
        self.state = 0  # Single flip-flop state

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        # Convert input strings to integers
        a = int(stimulus_dict['a'], 2)
        b = int(stimulus_dict['b'], 2)
        
        # Update state on rising clock edge
        if clk == 1:
            if a == 1 and b == 1:
                self.state = 1 if self.state == 0 else 0
        
        # Combinational logic for q output
        q = 0
        if ((a == 0 and b == 1 and self.state == 0) or
            (a == 1 and b == 0 and self.state == 0) or
            (a == 0 and b == 0 and self.state == 1) or
            (a == 1 and b == 1 and self.state == 1)):
            q = 1
            
        # Return outputs as binary strings
        return {
            'q': format(q, 'b'),
            'state': format(self.state, 'b')
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


