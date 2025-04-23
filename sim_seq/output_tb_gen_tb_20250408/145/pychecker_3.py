
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # States
        self.SEARCH = 0
        self.READ_DELAY = 1
        self.COUNTING = 2
        self.DONE = 3
        
        # Initialize registers
        self.state = self.SEARCH
        self.pattern_reg = 0
        self.delay_reg = 0
        self.counter = 0
        self.bits_read = 0
        
    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        if clk != 1:
            return {"count": format(self.counter // 1000, '04b'),
                    "counting": str(int(self.state == self.COUNTING)),
                    "done": str(int(self.state == self.DONE))}
        
        # Convert inputs
        reset = int(stimulus_dict["reset"], 2)
        data = int(stimulus_dict["data"], 2)
        ack = int(stimulus_dict["ack"], 2)
        
        # Synchronous reset
        if reset:
            self.state = self.SEARCH
            self.pattern_reg = 0
            self.delay_reg = 0
            self.counter = 0
            self.bits_read = 0
        else:
            # State machine logic
            if self.state == self.SEARCH:
                self.pattern_reg = ((self.pattern_reg << 1) | data) & 0xF
                if self.pattern_reg == 0xD:  # 1101
                    self.state = self.READ_DELAY
                    self.bits_read = 0
                    
            elif self.state == self.READ_DELAY:
                self.delay_reg = (self.delay_reg << 1) | data
                self.bits_read += 1
                if self.bits_read == 4:
                    self.state = self.COUNTING
                    self.counter = (self.delay_reg + 1) * 1000
                    
            elif self.state == self.COUNTING:
                if self.counter > 0:
                    self.counter -= 1
                if self.counter == 0:
                    self.state = self.DONE
                    
            elif self.state == self.DONE:
                if ack:
                    self.state = self.SEARCH
                    self.pattern_reg = 0
        
        # Prepare outputs
        count_val = self.counter // 1000 if self.state == self.COUNTING else 0
        counting = self.state == self.COUNTING
        done = self.state == self.DONE
        
        return {"count": format(count_val, '04b'),
                "counting": str(int(counting)),
                "done": str(int(done))}
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


