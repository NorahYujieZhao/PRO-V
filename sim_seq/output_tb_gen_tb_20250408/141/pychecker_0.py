
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state registers for one-hot encoding
        state_a = 1, state_b = 0 after reset
        '''
        self.state_a = 1  # Initial state A
        self.state_b = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state and compute output based on Mealy machine logic
        '''
        # Convert input signals from binary strings
        areset = int(stimulus_dict['areset'], 2)
        x = int(stimulus_dict['x'], 2)

        # Handle asynchronous reset
        if areset:
            self.state_a = 1
            self.state_b = 0
        # State update on clock edge
        elif clk == 1:
            # Compute next state
            if self.state_a and x:  # A->B transition
                self.state_a = 0
                self.state_b = 1
            elif self.state_a and not x:  # A->A transition
                self.state_a = 1
                self.state_b = 0
            elif self.state_b:  # B->B transition
                self.state_a = 0
                self.state_b = 1

        # Compute Mealy output based on current state and input
        z = 0
        if self.state_a and x:  # In A, x=1
            z = 1
        elif self.state_b and not x:  # In B, x=0
            z = 1

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


