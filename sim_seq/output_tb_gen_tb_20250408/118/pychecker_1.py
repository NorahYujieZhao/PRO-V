
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state registers
        '''
        self.state = 0  # State A=0, B=1, C=2, D=3, E=4
        self.count = 0  # Count of w=1s
        self.z = 0      # Output register

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update FSM state and outputs
        '''
        if clk == 1:  # Rising edge
            # Convert inputs to integers
            reset_val = int(stimulus_dict['reset'], 2)
            s_val = int(stimulus_dict['s'], 2)
            w_val = int(stimulus_dict['w'], 2)

            # Synchronous reset
            if reset_val == 1:
                self.state = 0
                self.count = 0
                self.z = 0
            else:
                # State machine transitions
                if self.state == 0:  # State A
                    if s_val == 1:
                        self.state = 1  # Go to B
                        self.count = w_val  # Start counting
                elif self.state == 1:  # State B
                    self.state = 2
                    self.count += w_val
                elif self.state == 2:  # State C
                    self.state = 3
                    self.count += w_val
                elif self.state == 3:  # State D
                    self.state = 4
                    # Set z for next cycle
                    self.z = 1 if self.count == 2 else 0
                else:  # State E
                    self.state = 1
                    self.count = w_val  # Start new count

        # Return output dictionary
        return {'z': format(self.z, 'b')}
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


