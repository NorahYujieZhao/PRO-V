
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # State encoding
        self.SEARCH = 0
        self.COLLECT = 1
        self.COUNT = 2
        self.DONE = 3
        
        # Initialize registers
        self.state = self.SEARCH
        self.pattern_reg = 0
        self.delay_reg = 0
        self.counter = 0
        self.bits_collected = 0
        self.time_display = 0
        self.counting = 0
        self.done = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        if clk != 1:  # Only process on rising edge
            return {"count": format(self.time_display, '04b'),
                    "counting": str(self.counting),
                    "done": str(self.done)}

        # Convert inputs to integers
        reset = int(stimulus_dict["reset"], 2)
        data = int(stimulus_dict["data"], 2)
        ack = int(stimulus_dict["ack"], 2)

        # Handle synchronous reset
        if reset:
            self.state = self.SEARCH
            self.pattern_reg = 0
            self.delay_reg = 0
            self.counter = 0
            self.bits_collected = 0
            self.time_display = 0
            self.counting = 0
            self.done = 0
        else:
            # State machine logic
            if self.state == self.SEARCH:
                self.pattern_reg = ((self.pattern_reg << 1) | data) & 0xF
                if self.pattern_reg == 0xD:  # 1101
                    self.state = self.COLLECT
                    self.bits_collected = 0

            elif self.state == self.COLLECT:
                self.delay_reg = (self.delay_reg << 1) | data
                self.bits_collected += 1
                if self.bits_collected == 4:
                    self.state = self.COUNT
                    self.counter = (self.delay_reg + 1) * 1000
                    self.time_display = self.delay_reg
                    self.counting = 1

            elif self.state == self.COUNT:
                self.counter -= 1
                if self.counter % 1000 == 0:
                    self.time_display = (self.counter // 1000)
                if self.counter == 0:
                    self.state = self.DONE
                    self.counting = 0
                    self.done = 1

            elif self.state == self.DONE:
                if ack:
                    self.state = self.SEARCH
                    self.pattern_reg = 0
                    self.done = 0

        return {"count": format(self.time_display, '04b'),
                "counting": str(self.counting),
                "done": str(self.done)}
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


