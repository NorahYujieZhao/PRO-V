
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 8-bit shift register to 0
        '''
        self.shift_reg = 0  # 8-bit shift register Q[7:0]

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Process inputs and update state on clock edge
        '''
        # Convert input binary strings to integers
        enable = int(stimulus_dict['enable'], 2)
        S = int(stimulus_dict['S'], 2)
        A = int(stimulus_dict['A'], 2)
        B = int(stimulus_dict['B'], 2)
        C = int(stimulus_dict['C'], 2)

        # On rising clock edge
        if clk == 1:
            if enable:
                # Shift S into MSB (Q[0]), shift others right
                self.shift_reg = ((self.shift_reg >> 1) | (S << 7)) & 0xFF

        # Select output Z based on ABC
        sel = (A << 2) | (B << 1) | C  # Combine ABC into 3-bit selector
        Z = (self.shift_reg >> (7 - sel)) & 1  # Extract selected bit

        # Return output as binary string
        return {'Z': format(Z, 'b')}
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


