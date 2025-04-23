
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Define states as constants
        self.STATE_A = 0
        self.STATE_B = 1
        self.STATE_C = 2
        self.STATE_D = 3
        self.STATE_E = 4
        
        # Initialize state variables
        self.current_state = self.STATE_A
        self.w_count = 0
        self.z_out = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert input signals from binary strings
        reset_val = int(stimulus_dict['reset'], 2)
        s_val = int(stimulus_dict['s'], 2)
        w_val = int(stimulus_dict['w'], 2)
        
        # Only process on clock edge
        if clk == 1:
            # Handle synchronous reset
            if reset_val == 1:
                self.current_state = self.STATE_A
                self.w_count = 0
                self.z_out = 0
            else:
                # State machine transitions
                if self.current_state == self.STATE_A:
                    if s_val == 1:
                        self.current_state = self.STATE_B
                        self.w_count = (1 if w_val == 1 else 0)
                elif self.current_state == self.STATE_B:
                    self.current_state = self.STATE_C
                    self.w_count += (1 if w_val == 1 else 0)
                elif self.current_state == self.STATE_C:
                    self.current_state = self.STATE_D
                    self.w_count += (1 if w_val == 1 else 0)
                elif self.current_state == self.STATE_D:
                    self.current_state = self.STATE_E
                    # Set z output for next cycle based on w_count
                    self.z_out = 1 if self.w_count == 2 else 0
                else:  # STATE_E
                    self.current_state = self.STATE_B
                    self.w_count = (1 if w_val == 1 else 0)
        
        # Return output dictionary with z as binary string
        return {'z': format(self.z_out, 'b')}
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


