
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Initialize to 12:00:00 AM
        self.pm = 0
        self.hours = 0x12    # BCD 12
        self.minutes = 0x00   # BCD 00
        self.seconds = 0x00   # BCD 00

    def load(self, clk, stimulus_dict):
        if clk == 1:  # Process on clock edge
            reset = int(stimulus_dict['reset'], 2)
            ena = int(stimulus_dict['ena'], 2)

            if reset:  # Synchronous reset has priority
                self.pm = 0
                self.hours = 0x12    # BCD 12
                self.minutes = 0x00   # BCD 00
                self.seconds = 0x00   # BCD 00
            elif ena:  # Increment time when enabled
                # Increment seconds
                sec_lo = (self.seconds & 0x0F)
                sec_hi = (self.seconds >> 4) & 0x0F
                
                sec_lo += 1
                if sec_lo > 9:
                    sec_lo = 0
                    sec_hi += 1
                if sec_hi > 5:
                    sec_hi = 0
                    # Increment minutes
                    min_lo = (self.minutes & 0x0F)
                    min_hi = (self.minutes >> 4) & 0x0F
                    
                    min_lo += 1
                    if min_lo > 9:
                        min_lo = 0
                        min_hi += 1
                    if min_hi > 5:
                        min_hi = 0
                        # Increment hours
                        hr_lo = (self.hours & 0x0F)
                        hr_hi = (self.hours >> 4) & 0x0F
                        
                        hr_lo += 1
                        if hr_lo > 9:
                            hr_lo = 0
                            hr_hi += 1
                        if hr_hi == 1 and hr_lo == 3:  # 12->1
                            hr_hi = 0
                            hr_lo = 1
                            self.pm = not self.pm  # Toggle AM/PM
                            
                        self.hours = (hr_hi << 4) | hr_lo
                    self.minutes = (min_hi << 4) | min_lo
                self.seconds = (sec_hi << 4) | sec_lo

        # Convert values to binary strings
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


