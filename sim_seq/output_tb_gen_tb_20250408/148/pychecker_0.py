
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize FSM state and registers
        '''
        self.state = 0  # 0=IDLE, 1=DATA, 2=STOP
        self.bit_counter = 0  # Counts data bits received
        self.shift_reg = 0    # Collects incoming data bits
        self.out_byte = 0     # Output byte register
        self.done = 0         # Done signal

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update FSM state and outputs on clock edge
        '''
        # Convert inputs from binary strings
        in_bit = int(stimulus_dict['in'], 2)
        reset = int(stimulus_dict['reset'], 2)

        # Only process on clock edge
        if clk == 1:
            # Handle reset
            if reset:
                self.state = 0
                self.bit_counter = 0
                self.shift_reg = 0
                self.out_byte = 0
                self.done = 0
            else:
                # FSM state machine
                if self.state == 0:  # IDLE
                    self.done = 0
                    if in_bit == 0:  # Start bit detected
                        self.state = 1
                        self.bit_counter = 0
                        self.shift_reg = 0

                elif self.state == 1:  # DATA
                    # Shift in new bit (LSB first)
                    self.shift_reg = (self.shift_reg >> 1) | (in_bit << 7)
                    self.bit_counter += 1
                    
                    if self.bit_counter == 8:
                        self.state = 2  # Move to STOP state

                elif self.state == 2:  # STOP
                    if in_bit == 1:  # Valid stop bit
                        self.out_byte = self.shift_reg
                        self.done = 1
                        self.state = 0  # Ready for next byte
                    # If invalid stop bit, stay in STOP state until we see a 1

        # Return outputs as binary strings
        return {
            'out_byte': format(self.out_byte, '08b'),
            'done': format(self.done, '01b')
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


