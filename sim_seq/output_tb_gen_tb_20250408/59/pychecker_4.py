
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 100-bit register to 0
        '''
        self.q = 0  # 100-bit register

    def rotate_right(self, value, width=100):
        '''
        Rotate right by 1 bit
        '''
        lsb = value & 1
        return (value >> 1) | (lsb << (width-1))

    def rotate_left(self, value, width=100):
        '''
        Rotate left by 1 bit
        '''
        msb = (value >> (width-1)) & 1
        return ((value << 1) & ((1 << width) - 1)) | msb

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Process inputs and update state on clock edge
        '''
        if clk == 1:  # Rising edge
            # Convert input strings to integers
            load_val = int(stimulus_dict.get('load', '0'), 2)
            ena_val = int(stimulus_dict.get('ena', '00'), 2)
            data_val = int(stimulus_dict.get('data', '0' * 100), 2)

            # Update logic
            if load_val:
                self.q = data_val
            elif ena_val == 0b01:  # Right rotation
                self.q = self.rotate_right(self.q)
            elif ena_val == 0b10:  # Left rotation
                self.q = self.rotate_left(self.q)
            # For ena_val == 0b00 or 0b11, maintain current value

        # Return output as 100-bit binary string
        return {'q': format(self.q, '0100b')}
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


