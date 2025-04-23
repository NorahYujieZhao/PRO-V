
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        self.hours = int('12', 16)  # Start at 12 (BCD)
        self.minutes = 0x00         # Start at 00 (BCD)
        self.seconds = 0x00         # Start at 00 (BCD)
        self.pm = 0                 # Start at AM

    def increment_bcd(self, value, max_tens, max_ones):
        ones = value & 0x0F
        tens = (value >> 4) & 0x0F
        
        ones += 1
        if ones > max_ones:
            ones = 0
            tens += 1
            if tens > max_tens:
                tens = 0
                return 0, True
        return (tens << 4) | ones, False

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert input signals from binary strings to integers
        reset = int(stimulus_dict['reset'], 2)
        ena = int(stimulus_dict['ena'], 2)

        if clk == 1:  # Rising edge
            if reset:
                self.hours = int('12', 16)  # Reset to 12 (BCD)
                self.minutes = 0x00
                self.seconds = 0x00
                self.pm = 0
            elif ena:
                # Update seconds
                self.seconds, rollover = self.increment_bcd(self.seconds, 5, 9)
                
                # Update minutes if seconds rolled over
                if rollover:
                    self.minutes, rollover = self.increment_bcd(self.minutes, 5, 9)
                    
                    # Update hours if minutes rolled over
                    if rollover:
                        if self.hours == 0x12:  # 12 -> 1
                            self.hours = 0x01
                            self.pm = not self.pm
                        else:
                            self.hours, _ = self.increment_bcd(self.hours, 1, 9)

        # Format outputs as binary strings
        return {
            'pm': format(self.pm, '01b'),
            'hh': format(self.hours, '08b'),
            'mm': format(self.minutes, '08b'),
            'ss': format(self.seconds, '08b')
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


