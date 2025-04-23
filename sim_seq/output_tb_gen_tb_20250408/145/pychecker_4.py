
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # FSM states
        self.SEARCH = 0
        self.LOAD_DELAY = 1
        self.COUNTING = 2
        self.DONE = 3
        
        # Initialize registers
        self.current_state = self.SEARCH
        self.pattern_buffer = 0
        self.delay_reg = 0
        self.counter = 0
        self.delay_bits_received = 0
        self.time_display = 0
        self.counting = 0
        self.done = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        if clk == 1:  # Process on rising edge
            # Convert inputs from binary strings
            reset = int(stimulus_dict['reset'], 2)
            data = int(stimulus_dict['data'], 2)
            ack = int(stimulus_dict['ack'], 2)

            # Synchronous reset
            if reset:
                self.current_state = self.SEARCH
                self.pattern_buffer = 0
                self.delay_reg = 0
                self.counter = 0
                self.delay_bits_received = 0
                self.time_display = 0
                self.counting = 0
                self.done = 0
            else:
                # FSM state transitions
                if self.current_state == self.SEARCH:
                    self.pattern_buffer = ((self.pattern_buffer << 1) | data) & 0xF
                    if self.pattern_buffer == 0xD:  # 1101 detected
                        self.current_state = self.LOAD_DELAY
                        self.delay_bits_received = 0

                elif self.current_state == self.LOAD_DELAY:
                    self.delay_reg = (self.delay_reg << 1) | data
                    self.delay_bits_received += 1
                    if self.delay_bits_received == 4:
                        self.current_state = self.COUNTING
                        self.counter = (self.delay_reg + 1) * 1000
                        self.time_display = self.delay_reg

                elif self.current_state == self.COUNTING:
                    self.counter -= 1
                    if self.counter % 1000 == 0:
                        self.time_display = (self.counter // 1000) - 1
                    if self.counter == 0:
                        self.current_state = self.DONE

                elif self.current_state == self.DONE:
                    if ack:
                        self.current_state = self.SEARCH
                        self.pattern_buffer = 0

            # Update outputs
            self.counting = 1 if self.current_state == self.COUNTING else 0
            self.done = 1 if self.current_state == self.DONE else 0

        # Prepare output dictionary with binary strings
        return {
            'count': format(self.time_display & 0xF, '04b'),
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


