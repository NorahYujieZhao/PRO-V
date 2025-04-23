
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Define states
        self.IDLE = 0
        self.DATA = 1
        self.STOP = 2
        
        # Initialize state variables
        self.current_state = self.IDLE
        self.bit_count = 0
        self.data_reg = 0
        self.done_reg = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert input signals from binary strings to integers
        in_val = int(stimulus_dict['in'], 2)
        reset_val = int(stimulus_dict['reset'], 2)
        
        # Only update on clock edge
        if clk == 1:
            # Handle reset
            if reset_val == 1:
                self.current_state = self.IDLE
                self.bit_count = 0
                self.data_reg = 0
                self.done_reg = 0
            else:
                # State machine logic
                if self.current_state == self.IDLE:
                    self.done_reg = 0
                    if in_val == 0:  # Start bit detected
                        self.current_state = self.DATA
                        self.bit_count = 0
                        self.data_reg = 0
                
                elif self.current_state == self.DATA:
                    # Shift in new data bit (LSB first)
                    self.data_reg = (in_val << self.bit_count) | self.data_reg
                    self.bit_count += 1
                    
                    if self.bit_count == 8:  # Received all 8 bits
                        self.current_state = self.STOP
                
                elif self.current_state == self.STOP:
                    if in_val == 1:  # Valid stop bit
                        self.done_reg = 1
                    self.current_state = self.IDLE

        # Convert output to binary string
        done_str = format(self.done_reg, 'b')
        
        return {'done': done_str}
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


