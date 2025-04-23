
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state registers for one-hot encoding
        State A: state_a = 1, state_b = 0
        State B: state_a = 0, state_b = 1
        '''
        self.state_a = 1  # Initialize in state A
        self.state_b = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state and compute output based on inputs
        '''
        # Convert input binary strings to integers
        areset = int(stimulus_dict['areset'], 2)
        x = int(stimulus_dict['x'], 2)

        # Handle asynchronous reset
        if areset:
            self.state_a = 1
            self.state_b = 0
        # Handle state transitions on clock edge
        elif clk == 1:
            next_state_a = self.state_a and not x
            next_state_b = (self.state_a and x) or self.state_b
            
            self.state_a = next_state_a
            self.state_b = next_state_b

        # Compute Mealy output based on current state and input
        z = (self.state_a and x) or (self.state_b and not x)

        # Return output as binary string
        return {'z': format(z, 'b')}
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


