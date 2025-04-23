
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state register to state A (one-hot encoding)
        State A = 2'b01
        State B = 2'b10
        '''
        self.state = 0b01  # Initialize to state A

    def load(self, clk, stimulus_dict: Dict[str, str]):
        '''
        Update state and output based on inputs
        '''
        # Convert input strings to integers
        x = int(stimulus_dict['x'], 2)
        areset = int(stimulus_dict['areset'], 2)

        # Asynchronous reset
        if areset:
            self.state = 0b01  # Reset to state A
            z = 0
        else:
            # Current state decode
            state_a = (self.state == 0b01)
            state_b = (self.state == 0b10)

            # State transitions and output logic
            if clk:
                if state_a:
                    if x:
                        self.state = 0b10  # Go to state B
                    else:
                        self.state = 0b01  # Stay in state A

                elif state_b:
                    self.state = 0b10  # Stay in state B

            # Mealy output logic
            if state_a:
                z = 1 if x else 0
            else:  # state_b
                z = 1 if not x else 0

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


