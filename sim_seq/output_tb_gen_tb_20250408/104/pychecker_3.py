
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        '''
        self.q = 0  # 16-bit register initialized to 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update register state based on inputs
        '''
        # Convert input binary strings to integers
        d = int(stimulus_dict['d'], 2)
        byteena = int(stimulus_dict['byteena'], 2)
        resetn = int(stimulus_dict['resetn'], 2)

        # Only update on positive clock edge
        if clk == 1:
            if resetn == 0:
                # Synchronous reset
                self.q = 0
            else:
                # Handle upper byte (byteena[1])
                if byteena & 0b10:
                    upper_byte = (d & 0xFF00)
                else:
                    upper_byte = (self.q & 0xFF00)
                
                # Handle lower byte (byteena[0])
                if byteena & 0b01:
                    lower_byte = (d & 0x00FF)
                else:
                    lower_byte = (self.q & 0x00FF)
                
                # Combine bytes
                self.q = upper_byte | lower_byte

        # Convert output to 16-bit binary string
        q_str = format(self.q, '016b')
        
        return {'q': q_str}
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


