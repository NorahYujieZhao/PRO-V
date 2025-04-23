
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Define state constants
        self.STATE_A = 0
        self.STATE_F = 1
        self.STATE_X1 = 2
        self.STATE_X0 = 3
        self.STATE_X1_2 = 4
        self.STATE_G1 = 5
        self.STATE_G1_WAIT = 6
        self.STATE_G1_PERM = 7
        self.STATE_G0_PERM = 8
        
        # Initialize current state
        self.current_state = self.STATE_A

    def load(self, clk, stimulus_dict):
        if clk == 1:  # Only update on rising edge
            # Convert input strings to integers
            resetn = int(stimulus_dict['resetn'], 2)
            x = int(stimulus_dict['x'], 2)
            y = int(stimulus_dict['y'], 2)
            
            # Next state logic
            next_state = self.current_state
            
            if resetn == 0:
                next_state = self.STATE_A
            else:
                if self.current_state == self.STATE_A:
                    next_state = self.STATE_F
                elif self.current_state == self.STATE_F:
                    next_state = self.STATE_X1
                elif self.current_state == self.STATE_X1:
                    if x == 1:
                        next_state = self.STATE_X0
                elif self.current_state == self.STATE_X0:
                    if x == 0:
                        next_state = self.STATE_X1_2
                elif self.current_state == self.STATE_X1_2:
                    if x == 1:
                        next_state = self.STATE_G1
                elif self.current_state == self.STATE_G1:
                    if y == 1:
                        next_state = self.STATE_G1_PERM
                    else:
                        next_state = self.STATE_G1_WAIT
                elif self.current_state == self.STATE_G1_WAIT:
                    if y == 1:
                        next_state = self.STATE_G1_PERM
                    else:
                        next_state = self.STATE_G0_PERM
            
            # Update state
            self.current_state = next_state
        
        # Output logic
        f = '1' if self.current_state == self.STATE_F else '0'
        g = '1' if self.current_state in [self.STATE_G1, self.STATE_G1_WAIT, self.STATE_G1_PERM] else '0'
        
        return {'f': f, 'g': g}
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


