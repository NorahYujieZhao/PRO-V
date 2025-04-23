
import json
from typing import Dict, List, Union


class GoldenDUT:
    # State constants
    SEARCH = 0
    READ_DELAY = 1
    COUNTING = 2
    DONE = 3

    def __init__(self):
        self.state = self.SEARCH
        self.pattern_bits = 0
        self.bits_seen = 0
        self.delay = 0
        self.delay_bits = 0
        self.delay_bits_count = 0
        self.cycle_counter = 0
        self.remaining_time = 0
        self.counting = 0
        self.done = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        if clk != 1:  # Only process on rising edge
            return {"count": format(self.remaining_time, '04b'),
                    "counting": str(self.counting),
                    "done": str(self.done)}

        # Convert inputs to integers
        reset = int(stimulus_dict.get("reset", "0"), 2)
        data = int(stimulus_dict.get("data", "0"), 2)
        ack = int(stimulus_dict.get("ack", "0"), 2)

        # Handle reset
        if reset:
            self.state = self.SEARCH
            self.pattern_bits = 0
            self.bits_seen = 0
            self.delay = 0
            self.delay_bits = 0
            self.delay_bits_count = 0
            self.cycle_counter = 0
            self.counting = 0
            self.done = 0
            self.remaining_time = 0
            return {"count": "0000", "counting": "0", "done": "0"}

        # State machine
        if self.state == self.SEARCH:
            self.pattern_bits = ((self.pattern_bits << 1) | data) & 0xF
            if self.pattern_bits == 0xD:  # 1101
                self.state = self.READ_DELAY
                self.delay_bits = 0
                self.delay_bits_count = 0

        elif self.state == self.READ_DELAY:
            self.delay_bits = (self.delay_bits << 1) | data
            self.delay_bits_count += 1
            if self.delay_bits_count == 4:
                self.delay = self.delay_bits
                self.remaining_time = self.delay
                self.cycle_counter = 0
                self.state = self.COUNTING
                self.counting = 1

        elif self.state == self.COUNTING:
            self.cycle_counter += 1
            if self.cycle_counter >= 1000:
                self.cycle_counter = 0
                if self.remaining_time > 0:
                    self.remaining_time -= 1
                else:
                    self.state = self.DONE
                    self.counting = 0
                    self.done = 1

        elif self.state == self.DONE:
            if ack:
                self.state = self.SEARCH
                self.pattern_bits = 0
                self.done = 0

        return {"count": format(self.remaining_time, '04b'),
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


