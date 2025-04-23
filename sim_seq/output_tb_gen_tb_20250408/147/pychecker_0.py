
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # States
        self.IDLE = 0
        self.DATA = 1
        self.STOP = 2
        
        # Initialize state variables
        self.state = self.IDLE
        self.bit_counter = 0
        self.data = 0
        self.done = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert inputs from binary strings
        in_bit = int(stimulus_dict['in'], 2)
        reset = int(stimulus_dict['reset'], 2)
        
        # Only update on clock edge
        if clk == 1:
            # Handle reset
            if reset:
                self.state = self.IDLE
                self.bit_counter = 0
                self.data = 0
                self.done = 0
            else:
                # State machine logic
                if self.state == self.IDLE:
                    self.done = 0
                    if in_bit == 0:  # Start bit detected
                        self.state = self.DATA
                        self.bit_counter = 0
                        self.data = 0
                
                elif self.state == self.DATA:
                    # Shift in data LSB first
                    self.data = (self.data >> 1) | (in_bit << 7)
                    self.bit_counter += 1
                    if self.bit_counter == 8:
                        self.state = self.STOP
                
                elif self.state == self.STOP:
                    if in_bit == 1:  # Valid stop bit
                        self.done = 1
                        self.state = self.IDLE
                    else:  # Invalid stop bit
                        self.done = 0
                        # Wait for line to return to idle (1)
                        if in_bit == 1:
                            self.state = self.IDLE
        
        # Return output as binary string
        return {'done': format(self.done, 'b')}
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


