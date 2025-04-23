
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # State encoding
        self.STATE_IDLE = 0
        self.STATE_GOT1 = 1
        self.STATE_GOT11 = 2
        self.STATE_GOT110 = 3
        self.STATE_SHIFT1 = 4
        self.STATE_SHIFT2 = 5
        self.STATE_SHIFT3 = 6
        self.STATE_SHIFT4 = 7
        self.STATE_COUNTING = 8
        self.STATE_DONE = 9
        
        # Initialize state registers
        self.current_state = self.STATE_IDLE
        self.shift_ena = 0
        self.counting = 0
        self.done = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        if clk == 1:  # Only update on rising edge
            # Convert inputs from binary strings
            reset = int(stimulus_dict['reset'], 2)
            data = int(stimulus_dict['data'], 2)
            done_counting = int(stimulus_dict['done_counting'], 2)
            ack = int(stimulus_dict['ack'], 2)

            # Synchronous reset
            if reset:
                self.current_state = self.STATE_IDLE
                self.shift_ena = 0
                self.counting = 0
                self.done = 0
            else:
                # State machine transitions
                if self.current_state == self.STATE_IDLE:
                    if data == 1:
                        self.current_state = self.STATE_GOT1
                elif self.current_state == self.STATE_GOT1:
                    if data == 1:
                        self.current_state = self.STATE_GOT11
                    else:
                        self.current_state = self.STATE_IDLE
                elif self.current_state == self.STATE_GOT11:
                    if data == 0:
                        self.current_state = self.STATE_GOT110
                    else:
                        self.current_state = self.STATE_GOT11
                elif self.current_state == self.STATE_GOT110:
                    if data == 1:
                        self.current_state = self.STATE_SHIFT1
                    else:
                        self.current_state = self.STATE_IDLE
                elif self.current_state == self.STATE_SHIFT1:
                    self.current_state = self.STATE_SHIFT2
                elif self.current_state == self.STATE_SHIFT2:
                    self.current_state = self.STATE_SHIFT3
                elif self.current_state == self.STATE_SHIFT3:
                    self.current_state = self.STATE_SHIFT4
                elif self.current_state == self.STATE_SHIFT4:
                    self.current_state = self.STATE_COUNTING
                elif self.current_state == self.STATE_COUNTING:
                    if done_counting:
                        self.current_state = self.STATE_DONE
                elif self.current_state == self.STATE_DONE:
                    if ack:
                        self.current_state = self.STATE_IDLE

                # Output logic
                self.shift_ena = (self.current_state >= self.STATE_SHIFT1 and 
                                 self.current_state <= self.STATE_SHIFT4)
                self.counting = (self.current_state == self.STATE_COUNTING)
                self.done = (self.current_state == self.STATE_DONE)

        # Return outputs as binary strings
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


