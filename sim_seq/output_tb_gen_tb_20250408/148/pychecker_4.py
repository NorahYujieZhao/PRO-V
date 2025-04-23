
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # FSM states
        self.IDLE = 0
        self.DATA = 1
        self.STOP = 2
        
        # Initialize state variables
        self.current_state = self.IDLE
        self.bit_counter = 0
        self.shift_reg = 0
        self.done_flag = 0
        self.out_byte_reg = 0

    def load(self, clk, stimulus_dict):
        if clk == 1:  # Process on rising edge
            # Convert inputs to integers
            reset = int(stimulus_dict['reset'], 2)
            in_bit = int(stimulus_dict['in'], 2)
            
            # Handle reset
            if reset:
                self.current_state = self.IDLE
                self.bit_counter = 0
                self.shift_reg = 0
                self.done_flag = 0
                self.out_byte_reg = 0
            else:
                # FSM state machine
                if self.current_state == self.IDLE:
                    if in_bit == 0:  # Start bit detected
                        self.current_state = self.DATA
                        self.bit_counter = 0
                        self.shift_reg = 0
                        self.done_flag = 0
                
                elif self.current_state == self.DATA:
                    # Shift in new bit (LSB first)
                    self.shift_reg = (self.shift_reg >> 1) | (in_bit << 7)
                    self.bit_counter += 1
                    
                    if self.bit_counter == 8:
                        self.current_state = self.STOP
                
                elif self.current_state == self.STOP:
                    if in_bit == 1:  # Valid stop bit
                        self.done_flag = 1
                        self.out_byte_reg = self.shift_reg
                        self.current_state = self.IDLE
                    else:  # Invalid stop bit
                        self.done_flag = 0
                        # Stay in STOP state until we see a 1

        # Format outputs as binary strings
        out_byte = format(self.out_byte_reg, '08b')
        done = format(self.done_flag, 'b')
        
        return {
            'out_byte': out_byte,
            'done': done
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


