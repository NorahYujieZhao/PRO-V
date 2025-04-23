
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state register to OFF (0)
        '''
        self.state = 0  # 0=OFF, 1=ON
        self.out = 0    # Output register

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state and output based on inputs
        '''
        # Convert input binary strings to integers
        j = int(stimulus_dict['j'], 2)
        k = int(stimulus_dict['k'], 2)
        reset = int(stimulus_dict['reset'], 2)

        # Only update on rising clock edge
        if clk == 1:
            # Handle synchronous reset first
            if reset:
                self.state = 0
            else:
                # State transition logic
                if self.state == 0:  # OFF state
                    if j == 1:
                        self.state = 1  # transition to ON
                else:  # ON state
                    if k == 1:
                        self.state = 0  # transition to OFF
            
            # Moore output logic - depends only on state
            self.out = self.state

        # Return output as binary string
        return {'out': format(self.out, 'b')}
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


