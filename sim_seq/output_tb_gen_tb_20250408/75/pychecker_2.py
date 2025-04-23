
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize FSM state and output
        '''
        self.state = 0  # Initial state
        self.start_shifting = 0  # Output signal

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''
        Update FSM state and output on clock edge
        '''
        # Convert input signals from binary strings to integers
        reset = int(stimulus_dict['reset'], 2)
        data = int(stimulus_dict['data'], 2)
        
        # Only update on clock edge
        if clk == 1:
            # Handle reset first
            if reset:
                self.state = 0
                self.start_shifting = 0
            else:
                # State machine transitions
                if self.state == 0:
                    if data == 1:
                        self.state = 1
                elif self.state == 1:
                    if data == 1:
                        self.state = 2
                    else:
                        self.state = 0
                elif self.state == 2:
                    if data == 0:
                        self.state = 3
                    else:
                        self.state = 2
                elif self.state == 3:
                    if data == 1:
                        self.state = 4
                    else:
                        self.state = 0
                elif self.state == 4:
                    self.state = 4  # Stay in this state
                
                # Update output based on state
                self.start_shifting = 1 if self.state == 4 else 0

        # Return output as binary string
        return {'start_shifting': format(self.start_shifting, 'b')}
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


