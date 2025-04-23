
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state registers
        '''
        # Define state encodings
        self.STATE_A = 0  # 000
        self.STATE_B = 1  # 001
        self.STATE_C = 2  # 010
        self.STATE_D = 3  # 011
        self.STATE_E = 4  # 100
        self.STATE_F = 5  # 101
        
        # Initialize current state to A
        self.state = self.STATE_A

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state and output based on inputs
        '''
        # Convert input binary strings to integers
        reset = int(stimulus_dict['reset'], 2)
        w = int(stimulus_dict['w'], 2)
        
        # Update state on rising edge
        if clk == 1:
            if reset:
                next_state = self.STATE_A
            else:
                # State transition logic
                if self.state == self.STATE_A:
                    next_state = self.STATE_B if w else self.STATE_A
                elif self.state == self.STATE_B:
                    next_state = self.STATE_C if w else self.STATE_D
                elif self.state == self.STATE_C:
                    next_state = self.STATE_E if w else self.STATE_D
                elif self.state == self.STATE_D:
                    next_state = self.STATE_F if w else self.STATE_A
                elif self.state == self.STATE_E:
                    next_state = self.STATE_E if w else self.STATE_D
                else:  # STATE_F
                    next_state = self.STATE_C if w else self.STATE_D
                    
            self.state = next_state

        # Output logic - z is 1 in states E and F
        z = 1 if self.state in [self.STATE_E, self.STATE_F] else 0
        
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


