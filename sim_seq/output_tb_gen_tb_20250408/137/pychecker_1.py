
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state to B (reset state)
        '''
        self.STATE_A = 0
        self.STATE_B = 1
        self.current_state = self.STATE_B

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state machine and generate output
        '''
        # Convert input signals from binary strings to integers
        reset_val = int(stimulus_dict['reset'], 2)
        in_val = int(stimulus_dict['in'], 2)

        # Only update on clock edge
        if clk == 1:
            # Handle reset (synchronous)
            if reset_val == 1:
                self.current_state = self.STATE_B
            else:
                # State transition logic
                if self.current_state == self.STATE_B:
                    if in_val == 0:
                        self.current_state = self.STATE_A
                else:  # current_state == STATE_A
                    if in_val == 0:
                        self.current_state = self.STATE_B

        # Moore output logic - depends only on current state
        out_val = 1 if self.current_state == self.STATE_B else 0

        # Return output as binary string
        return {'out': format(out_val, 'b')}
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


