
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize 4-bit shift register to 0
        '''
        self.shift_reg = 0  # 4-bit shift register

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert input binary strings to integers
        resetn = int(stimulus_dict['resetn'], 2)
        in_bit = int(stimulus_dict['in'], 2)

        # Process on rising edge of clock
        if clk == 1:
            if resetn == 0:
                # Synchronous reset (active low)
                self.shift_reg = 0
            else:
                # Shift operation: shift right and insert new bit at leftmost position
                self.shift_reg = ((self.shift_reg >> 1) | (in_bit << 3)) & 0xF

        # Output is the rightmost bit
        out_bit = self.shift_reg & 1
        
        # Return output as binary string
        return {'out': format(out_bit, 'b')}
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


