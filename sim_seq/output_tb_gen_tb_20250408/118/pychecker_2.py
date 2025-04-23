
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state registers and counters
        '''
        self.state = 0  # State A=0, B1=1, B2=2, B3=3, B4=4
        self.ones_count = 0  # Count of 1s seen in w
        self.z = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''
        Update FSM state and outputs on clock edge
        '''
        if clk != 1:  # Only update on rising clock edge
            return {"z": format(self.z, 'b')}

        # Convert inputs from binary strings to integers
        reset = int(stimulus_dict["reset"], 2)
        s = int(stimulus_dict["s"], 2)
        w = int(stimulus_dict["w"], 2)

        # Handle reset
        if reset:
            self.state = 0
            self.ones_count = 0
            self.z = 0
            return {"z": "0"}

        # State machine logic
        if self.state == 0:  # State A
            if s == 1:
                self.state = 1  # Move to B1
                self.ones_count = (1 if w == 1 else 0)
            self.z = 0

        elif self.state == 1:  # State B1
            self.state = 2  # Move to B2
            self.ones_count += (1 if w == 1 else 0)
            self.z = 0

        elif self.state == 2:  # State B2
            self.state = 3  # Move to B3
            self.ones_count += (1 if w == 1 else 0)
            self.z = 0

        elif self.state == 3:  # State B3
            self.state = 4  # Move to B4
            self.z = 0

        elif self.state == 4:  # State B4
            self.state = 1  # Move back to B1
            self.z = 1 if self.ones_count == 2 else 0
            self.ones_count = (1 if w == 1 else 0)  # Start counting for next cycle

        return {"z": format(self.z, 'b')}
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


