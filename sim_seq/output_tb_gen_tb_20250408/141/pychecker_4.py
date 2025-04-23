
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state registers using one-hot encoding:
        state_a = 1, state_b = 0 (initial state A)
        '''
        self.state_a = 1  # State A (initial state)
        self.state_b = 0  # State B

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state and calculate output based on inputs
        '''
        # Convert input signals from binary strings
        areset = int(stimulus_dict['areset'], 2)
        x = int(stimulus_dict['x'], 2)

        # Handle asynchronous reset
        if areset:
            self.state_a = 1
            self.state_b = 0
            z = 0
        else:
            # Calculate output z based on current state and input x
            z = 0
            if self.state_a and x:  # A->B transition
                z = 1
            elif self.state_b and not x:  # In state B, x=0
                z = 1

            # Update state on clock edge
            if clk == 1:
                if self.state_a and x:  # A->B transition
                    self.state_a = 0
                    self.state_b = 1
                # State B stays in B for both x=0 and x=1

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


