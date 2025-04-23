
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Define states
        self.IDLE = 0
        self.GOT1 = 1
        self.GOT11 = 2
        self.GOT110 = 3
        self.GOT1101 = 4
        self.SHIFTING = 5
        self.COUNTING = 6
        self.DONE = 7
        
        # Initialize state and outputs
        self.state = self.IDLE
        self.shift_count = 0
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
            # Handle reset
            if reset:
                self.state = self.IDLE
                self.shift_count = 0
                self.shift_ena = 0
                self.counting = 0
                self.done = 0
            else:
                # State machine transitions
                if self.state == self.IDLE:
                    if data == 1:
                        self.state = self.GOT1
                elif self.state == self.GOT1:
                    if data == 1:
                        self.state = self.GOT11
                    else:
                        self.state = self.IDLE
                elif self.state == self.GOT11:
                    if data == 0:
                        self.state = self.GOT110
                    else:
                        self.state = self.GOT11
                elif self.state == self.GOT110:
                    if data == 1:
                        self.state = self.GOT1101
                    else:
                        self.state = self.IDLE
                elif self.state == self.GOT1101:
                    self.state = self.SHIFTING
                    self.shift_count = 0
                elif self.state == self.SHIFTING:
                    self.shift_count += 1
                    if self.shift_count >= 4:
                        self.state = self.COUNTING
                elif self.state == self.COUNTING:
                    if done_counting:
                        self.state = self.DONE
                elif self.state == self.DONE:
                    if ack:
                        self.state = self.IDLE

            # Set outputs based on state
            self.shift_ena = 1 if self.state == self.SHIFTING else 0
            self.counting = 1 if self.state == self.COUNTING else 0
            self.done = 1 if self.state == self.DONE else 0

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


