
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state registers and counters
        '''
        self.STATE_IDLE = 0
        self.STATE_DATA = 1
        self.STATE_STOP = 2
        self.current_state = self.STATE_IDLE
        self.bit_counter = 0
        self.done_flag = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update FSM state and outputs based on inputs
        '''
        # Convert input signals from binary strings
        in_bit = int(stimulus_dict['in'], 2)
        reset = int(stimulus_dict['reset'], 2)
        
        # Only process on clock edge
        if clk == 1:
            # Handle reset
            if reset:
                self.current_state = self.STATE_IDLE
                self.bit_counter = 0
                self.done_flag = 0
            else:
                # FSM state transitions
                if self.current_state == self.STATE_IDLE:
                    self.done_flag = 0
                    if in_bit == 0:  # Start bit detected
                        self.current_state = self.STATE_DATA
                        self.bit_counter = 0
                
                elif self.current_state == self.STATE_DATA:
                    self.bit_counter += 1
                    if self.bit_counter >= 8:  # 8 data bits received
                        self.current_state = self.STATE_STOP
                        self.bit_counter = 0
                
                elif self.current_state == self.STATE_STOP:
                    if in_bit == 1:  # Valid stop bit
                        self.current_state = self.STATE_IDLE
                        self.done_flag = 1

        # Format output signals as binary strings
        return {'done': format(self.done_flag, 'b')}
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


