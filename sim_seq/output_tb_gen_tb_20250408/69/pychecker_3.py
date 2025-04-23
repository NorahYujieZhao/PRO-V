
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state register to 000
        '''
        self.state = 0  # 3-bit state register

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state and outputs on clock edge
        '''
        # Convert input binary strings to integers
        x = int(stimulus_dict['x'], 2)
        y = int(stimulus_dict['y'], 2)
        
        # Only update on clock edge
        if clk == 1:
            self.state = y  # Update current state
            
            # Calculate next state based on current state and input x
            if self.state == 0b000:
                next_state = 0b000 if x == 0 else 0b001
            elif self.state == 0b001:
                next_state = 0b001 if x == 0 else 0b100
            elif self.state == 0b010:
                next_state = 0b010 if x == 0 else 0b001
            elif self.state == 0b011:
                next_state = 0b001 if x == 0 else 0b010
            elif self.state == 0b100:
                next_state = 0b011 if x == 0 else 0b100
            else:
                next_state = 0b000  # Default case
            
            # Set Y0 (LSB of next state)
            Y0 = next_state & 1
            
            # Set output z based on current state
            z = 1 if self.state in [0b011, 0b100] else 0
            
            # Convert outputs to binary strings
            return {
                'Y0': format(Y0, 'b'),
                'z': format(z, 'b')
            }
        
        # Return previous values when not clock edge
        return {
            'Y0': '0',
            'z': '0'
        }
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


