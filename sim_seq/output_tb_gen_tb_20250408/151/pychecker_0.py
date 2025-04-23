
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # State encoding
        self.STATE_PATTERN = 0  # Looking for pattern 1101
        self.STATE_SHIFT = 1   # Shifting in 4 bits
        self.STATE_COUNT = 2    # Waiting for counting to complete
        self.STATE_DONE = 3     # Timer done, waiting for ack
        
        # Initialize state variables
        self.current_state = self.STATE_PATTERN
        self.pattern_reg = 0    # Stores last 4 bits for pattern detection
        self.shift_counter = 0  # Counts shift cycles
        
        # Initialize outputs
        self.shift_ena = 0
        self.counting = 0
        self.done = 0
    
    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert inputs from binary strings to integers
        reset = int(stimulus_dict['reset'], 2)
        data = int(stimulus_dict['data'], 2)
        done_counting = int(stimulus_dict['done_counting'], 2)
        ack = int(stimulus_dict['ack'], 2)
        
        # Only update on clock edge
        if clk == 1:
            # Handle synchronous reset
            if reset == 1:
                self.current_state = self.STATE_PATTERN
                self.pattern_reg = 0
                self.shift_counter = 0
                self.shift_ena = 0
                self.counting = 0
                self.done = 0
            else:
                # State machine logic
                if self.current_state == self.STATE_PATTERN:
                    # Shift in new bit and check for pattern
                    self.pattern_reg = ((self.pattern_reg << 1) | data) & 0xF
                    if self.pattern_reg == 0xD:  # 1101 pattern
                        self.current_state = self.STATE_SHIFT
                        self.shift_counter = 0
                        self.shift_ena = 1
                
                elif self.current_state == self.STATE_SHIFT:
                    self.shift_counter += 1
                    if self.shift_counter >= 4:
                        self.current_state = self.STATE_COUNT
                        self.shift_ena = 0
                        self.counting = 1
                
                elif self.current_state == self.STATE_COUNT:
                    if done_counting == 1:
                        self.current_state = self.STATE_DONE
                        self.counting = 0
                        self.done = 1
                
                elif self.current_state == self.STATE_DONE:
                    if ack == 1:
                        self.current_state = self.STATE_PATTERN
                        self.pattern_reg = 0
                        self.done = 0
        
        # Convert outputs to binary strings
        return {
            'shift_ena': format(self.shift_ena, 'b'),
            'counting': format(self.counting, 'b'),
            'done': format(self.done, 'b')
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


