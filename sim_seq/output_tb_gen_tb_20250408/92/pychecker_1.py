
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state registers
        '''
        self.state = 0  # State A=0, B=1, C=2, D=3

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        # Convert input signals from binary strings to integers
        resetn = int(stimulus_dict['resetn'], 2)
        r = int(stimulus_dict['r'], 2)
        
        # Extract individual request signals
        r1 = (r >> 2) & 1  # r[3]
        r2 = (r >> 1) & 1  # r[2]
        r3 = r & 1         # r[1]
        
        if clk == 1:  # Rising edge
            if resetn == 0:  # Synchronous reset
                self.state = 0  # Go to state A
            else:
                # State transition logic
                if self.state == 0:  # State A
                    if r1:
                        self.state = 1  # Go to B
                    elif r2:
                        self.state = 2  # Go to C
                    elif r3:
                        self.state = 3  # Go to D
                elif self.state == 1:  # State B
                    if not r1:
                        self.state = 0  # Go to A
                elif self.state == 2:  # State C
                    if not r2:
                        self.state = 0  # Go to A
                elif self.state == 3:  # State D
                    if not r3:
                        self.state = 0  # Go to A
        
        # Generate output grants
        g1 = 1 if self.state == 1 else 0
        g2 = 1 if self.state == 2 else 0
        g3 = 1 if self.state == 3 else 0
        
        # Combine grants into 3-bit output
        g = (g1 << 2) | (g2 << 1) | g3
        
        # Return output dictionary with binary string
        return {'g': format(g, '03b')}
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


