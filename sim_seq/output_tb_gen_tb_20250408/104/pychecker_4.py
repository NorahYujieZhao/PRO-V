
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize 16-bit register q to 0
        '''
        self.q = 0  # 16-bit register

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Handle clock-edge triggered updates with byte enables
        '''
        # Convert input binary strings to integers
        resetn = int(stimulus_dict['resetn'], 2)
        byteena = int(stimulus_dict['byteena'], 2)
        d = int(stimulus_dict['d'], 2)
        
        # Only update on positive clock edge
        if clk == 1:
            if resetn == 0:
                # Synchronous reset - clear all bits
                self.q = 0
            else:
                # Handle byte enables
                new_q = self.q
                if byteena & 0x1:  # byteena[0] - lower byte
                    new_q = (new_q & 0xFF00) | (d & 0x00FF)
                if byteena & 0x2:  # byteena[1] - upper byte
                    new_q = (new_q & 0x00FF) | (d & 0xFF00)
                self.q = new_q

        # Return current value as 16-bit binary string
        return {'q': format(self.q, '016b')}
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


