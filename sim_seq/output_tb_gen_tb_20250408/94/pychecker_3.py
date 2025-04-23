
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state variables
        '''
        self.state = 0  # 0=IDLE, 1=BYTE2, 2=BYTE3
        self.done_reg = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state machine on clock edge
        '''
        # Convert inputs from binary strings
        in_val = int(stimulus_dict['in'], 2)
        reset = int(stimulus_dict['reset'], 2)
        
        # Only update on clock edge
        if clk == 1:
            # Handle synchronous reset
            if reset == 1:
                self.state = 0
                self.done_reg = 0
            else:
                # State machine logic
                if self.state == 0:  # IDLE
                    if (in_val & 0x08) != 0:  # Check in[3]==1
                        self.state = 1
                    self.done_reg = 0
                elif self.state == 1:  # BYTE2
                    self.state = 2
                    self.done_reg = 0
                elif self.state == 2:  # BYTE3
                    self.state = 0
                    self.done_reg = 1

        # Convert output to binary string
        return {'done': format(self.done_reg, 'b')}
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


