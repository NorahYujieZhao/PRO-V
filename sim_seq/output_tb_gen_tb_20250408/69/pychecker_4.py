
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state register y to 000
        '''
        self.y = 0  # 3-bit state register

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state and outputs based on inputs
        '''
        # Convert input strings to integers
        x = int(stimulus_dict['x'], 2)
        y_in = int(stimulus_dict['y'], 2)

        # Calculate next state Y based on current state and input x
        if clk == 1:
            if y_in == 0b000:
                self.y = 0b001 if x else 0b000
            elif y_in == 0b001:
                self.y = 0b100 if x else 0b001
            elif y_in == 0b010:
                self.y = 0b001 if x else 0b010
            elif y_in == 0b011:
                self.y = 0b010 if x else 0b001
            elif y_in == 0b100:
                self.y = 0b100 if x else 0b011

        # Calculate Y0 (LSB of next state)
        Y0 = self.y & 0b001

        # Calculate output z based on current state
        z = 1 if (y_in == 0b011 or y_in == 0b100) else 0

        # Return outputs as binary strings
        return {
            'Y0': format(Y0, 'b'),
            'z': format(z, 'b')
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


