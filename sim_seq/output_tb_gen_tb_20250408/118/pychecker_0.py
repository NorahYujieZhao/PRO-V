
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''Initialize state variables'''
        self.state = 0  # State A=0, B1=1, B2=2, B3=3, B4=4
        self.count = 0  # Count of w=1s
        self.z = 0      # Output

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''Process inputs and update state'''
        if clk == 1:  # Only update on clock edge
            # Convert inputs from binary strings to integers
            reset = int(stimulus_dict['reset'], 2)
            s = int(stimulus_dict['s'], 2)
            w = int(stimulus_dict['w'], 2)

            # Synchronous reset
            if reset:
                self.state = 0
                self.count = 0
                self.z = 0
            else:
                # State machine logic
                if self.state == 0:  # State A
                    if s == 1:
                        self.state = 1
                        self.count = w  # Start counting w
                elif self.state == 1:  # State B1
                    self.state = 2
                    self.count += w
                elif self.state == 2:  # State B2
                    self.state = 3
                    self.count += w
                elif self.state == 3:  # State B3
                    self.state = 4
                    # No count update, just transition
                else:  # State B4
                    self.state = 1
                    self.z = 1 if self.count == 2 else 0
                    self.count = w  # Start new count

        # Return output as binary string
        return {'z': format(self.z, 'b')}
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


