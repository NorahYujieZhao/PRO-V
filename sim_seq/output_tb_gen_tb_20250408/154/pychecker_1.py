
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Initialize to 12:00:00 AM
        self.pm = 0  # 0 = AM, 1 = PM
        self.hh = int('12', 10)  # Hours in decimal
        self.mm = 0   # Minutes
        self.ss = 0   # Seconds

    def _increment_bcd(self, value):
        # Handle BCD increment with rollover
        ones = value & 0x0F
        tens = (value >> 4) & 0x0F
        ones += 1
        if ones > 9:
            ones = 0
            tens += 1
        return (tens << 4) | ones

    def _format_bcd(self, value):
        # Convert decimal to BCD
        ones = value % 10
        tens = (value // 10) % 10
        return (tens << 4) | ones

    def load(self, clk, stimulus_dict):
        reset = int(stimulus_dict['reset'], 2)
        ena = int(stimulus_dict['ena'], 2)

        if clk == 1:  # Rising edge
            if reset:  # Synchronous reset
                self.pm = 0
                self.hh = 12
                self.mm = 0
                self.ss = 0
            elif ena:  # Clock enable
                # Increment seconds
                self.ss = (self.ss + 1) % 60
                if self.ss == 0:
                    # Increment minutes
                    self.mm = (self.mm + 1) % 60
                    if self.mm == 0:
                        # Increment hours
                        if self.hh == 11:
                            self.hh = 12
                            # Toggle AM/PM at 11:59:59->12:00:00
                            self.pm = not self.pm
                        elif self.hh == 12:
                            self.hh = 1
                        else:
                            self.hh = self.hh + 1

        # Convert outputs to binary strings
        return {
            'pm': format(self.pm, '01b'),
            'hh': format(self._format_bcd(self.hh), '08b'),
            'mm': format(self._format_bcd(self.mm), '08b'),
            'ss': format(self._format_bcd(self.ss), '08b')
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


