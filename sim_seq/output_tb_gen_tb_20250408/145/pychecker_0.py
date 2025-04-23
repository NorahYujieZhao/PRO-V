
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # States
        self.SEARCH = 0
        self.COLLECT = 1
        self.COUNT = 2
        self.DONE = 3
        
        # Initialize registers
        self.state = self.SEARCH
        self.pattern_reg = 0
        self.delay_reg = 0
        self.bits_collected = 0
        self.cycle_counter = 0
        self.period_counter = 0
        self.time_remaining = 0
        self.counting = 0
        self.done = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        if clk != 1:  # Only update on rising edge
            return {"count": format(self.time_remaining, '04b'),
                    "counting": str(self.counting),
                    "done": str(self.done)}

        # Convert inputs
        reset = int(stimulus_dict["reset"], 2)
        data = int(stimulus_dict["data"], 2)
        ack = int(stimulus_dict["ack"], 2)

        # Handle reset
        if reset:
            self.state = self.SEARCH
            self.pattern_reg = 0
            self.delay_reg = 0
            self.bits_collected = 0
            self.cycle_counter = 0
            self.period_counter = 0
            self.time_remaining = 0
            self.counting = 0
            self.done = 0
        else:
            # State machine logic
            if self.state == self.SEARCH:
                self.pattern_reg = ((self.pattern_reg << 1) | data) & 0xF
                if self.pattern_reg == 0xD:  # 1101
                    self.state = self.COLLECT
                    self.bits_collected = 0
                    self.delay_reg = 0

            elif self.state == self.COLLECT:
                self.delay_reg = (self.delay_reg << 1) | data
                self.bits_collected += 1
                if self.bits_collected == 4:
                    self.state = self.COUNT
                    self.cycle_counter = 0
                    self.period_counter = 0
                    self.time_remaining = self.delay_reg
                    self.counting = 1

            elif self.state == self.COUNT:
                self.cycle_counter += 1
                if self.cycle_counter == 1000:
                    self.cycle_counter = 0
                    if self.period_counter == self.delay_reg:
                        self.state = self.DONE
                        self.counting = 0
                        self.done = 1
                    else:
                        self.period_counter += 1
                        self.time_remaining = self.delay_reg - self.period_counter

            elif self.state == self.DONE:
                if ack:
                    self.state = self.SEARCH
                    self.pattern_reg = 0
                    self.done = 0

        return {"count": format(self.time_remaining, '04b'),
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


