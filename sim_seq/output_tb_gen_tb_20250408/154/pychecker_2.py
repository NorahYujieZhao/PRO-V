
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Initialize to 12:00:00 AM
        self.pm = 0  # 0=AM, 1=PM
        self.hh = 0x12  # BCD 12
        self.mm = 0x00  # BCD 00 
        self.ss = 0x00  # BCD 00

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert input signals from binary strings
        reset = int(stimulus_dict['reset'], 2)
        ena = int(stimulus_dict['ena'], 2)
        
        output = {}
        
        if clk == 1:  # Rising edge
            if reset == 1:
                # Reset to 12:00:00 AM
                self.pm = 0
                self.hh = 0x12
                self.mm = 0x00
                self.ss = 0x00
            elif ena == 1:
                # Increment seconds
                ss_ones = self.ss & 0x0F
                ss_tens = (self.ss >> 4) & 0x0F
                
                ss_ones += 1
                if ss_ones > 9:
                    ss_ones = 0
                    ss_tens += 1
                if ss_tens > 5:
                    ss_tens = 0
                    # Increment minutes
                    mm_ones = self.mm & 0x0F
                    mm_tens = (self.mm >> 4) & 0x0F
                    
                    mm_ones += 1
                    if mm_ones > 9:
                        mm_ones = 0
                        mm_tens += 1
                    if mm_tens > 5:
                        mm_tens = 0
                        # Increment hours
                        hh_ones = self.hh & 0x0F
                        hh_tens = (self.hh >> 4) & 0x0F
                        
                        hh_ones += 1
                        if hh_ones > 9:
                            hh_ones = 0
                            hh_tens += 1
                        if hh_tens == 1 and hh_ones > 2:
                            hh_tens = 0
                            hh_ones = 1
                            # Toggle AM/PM when rolling over from 11:59:59 to 12:00:00
                            if self.hh == 0x11:
                                self.pm = not self.pm
                                
                        self.hh = (hh_tens << 4) | hh_ones
                    self.mm = (mm_tens << 4) | mm_ones
                self.ss = (ss_tens << 4) | ss_ones

        # Convert outputs to binary strings
        output['pm'] = format(self.pm, '01b')
        output['hh'] = format(self.hh, '08b')
        output['mm'] = format(self.mm, '08b')
        output['ss'] = format(self.ss, '08b')
        
        return output
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


