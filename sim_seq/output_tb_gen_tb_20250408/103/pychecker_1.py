
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize FSM state to A (000)
        '''
        self.state = 0  # State A

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''
        Update FSM state and output based on inputs
        '''
        # Convert input signals from binary strings
        reset_val = int(stimulus_dict['reset'], 2)
        w_val = int(stimulus_dict['w'], 2)
        
        # Only update on rising clock edge
        if clk == 1:
            if reset_val == 1:
                next_state = 0  # Reset to state A
            else:
                # State transition logic
                if self.state == 0:    # State A
                    next_state = 1 if w_val == 1 else 0
                elif self.state == 1:  # State B
                    next_state = 2 if w_val == 1 else 3
                elif self.state == 2:  # State C
                    next_state = 4 if w_val == 1 else 3
                elif self.state == 3:  # State D
                    next_state = 5 if w_val == 1 else 0
                elif self.state == 4:  # State E
                    next_state = 4 if w_val == 1 else 3
                else:                  # State F
                    next_state = 2 if w_val == 1 else 3
                    
            self.state = next_state
        
        # Output logic: z is 1 in states E (4) and F (5)
        z_val = 1 if self.state in [4, 5] else 0
        
        return {'z': format(z_val, 'b')}
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


