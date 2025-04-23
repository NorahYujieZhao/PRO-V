
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Define state encoding
        self.STATE_A = 0
        self.STATE_B = 1
        self.STATE_C = 2
        self.STATE_D = 3
        
        # Initialize current state
        self.current_state = self.STATE_A
        
    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert input signals from binary strings
        resetn = int(stimulus_dict['resetn'], 2)
        r1 = int(stimulus_dict['r'][2])
        r2 = int(stimulus_dict['r'][1])
        r3 = int(stimulus_dict['r'][0])
        
        if clk == 1:  # Rising edge
            # Synchronous reset
            if resetn == 0:
                self.current_state = self.STATE_A
            else:
                # State transition logic
                if self.current_state == self.STATE_A:
                    if r1 == 1:
                        self.current_state = self.STATE_B
                    elif r2 == 1:
                        self.current_state = self.STATE_C
                    elif r3 == 1:
                        self.current_state = self.STATE_D
                elif self.current_state == self.STATE_B:
                    if r1 == 0:
                        self.current_state = self.STATE_A
                elif self.current_state == self.STATE_C:
                    if r2 == 0:
                        self.current_state = self.STATE_A
                elif self.current_state == self.STATE_D:
                    self.current_state = self.STATE_A
        
        # Output logic
        g1 = 1 if self.current_state == self.STATE_B else 0
        g2 = 1 if self.current_state == self.STATE_C else 0
        g3 = 1 if self.current_state == self.STATE_D else 0
        
        # Format output as 3-bit binary string
        g_out = format((g1 << 2) | (g2 << 1) | g3, '03b')
        
        return {'g': g_out}
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


