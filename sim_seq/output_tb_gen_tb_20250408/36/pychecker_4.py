
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 2-bit counter state to weakly not-taken (01)
        '''
        self.state = 1  # Initialize to 0b01

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update counter state based on inputs and generate outputs
        '''
        # Convert input signals from binary strings
        areset = int(stimulus_dict['areset'], 2)
        train_valid = int(stimulus_dict['train_valid'], 2)
        train_taken = int(stimulus_dict['train_taken'], 2)

        # Handle asynchronous reset
        if areset:
            self.state = 1  # Reset to weakly not-taken (01)
        # Update counter on clock edge when train_valid is high
        elif clk == 1 and train_valid:
            if train_taken:
                # Increment with saturation at 3
                self.state = min(self.state + 1, 3)
            else:
                # Decrement with saturation at 0
                self.state = max(self.state - 1, 0)

        # Format output as 2-bit binary string
        state_str = format(self.state, '02b')
        return {'state': state_str}
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


