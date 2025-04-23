
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state variables
        '''
        self.state = 0  # 0=searching, 1=got first byte, 2=got second byte
        self.done_reg = 0

    def load(self, clk, stimulus_dict: Dict[str, str]):
        '''
        Process one clock cycle of input
        '''
        if clk == 1:  # Only update on rising edge
            # Convert inputs from binary strings
            reset = int(stimulus_dict['reset'], 2)
            in_byte = int(stimulus_dict['in'], 2)
            
            # Handle reset
            if reset:
                self.state = 0
                self.done_reg = 0
            else:
                # State machine logic
                if self.state == 0:
                    # Looking for first byte (in[3] must be 1)
                    if (in_byte & 0x08) != 0:  # Check if in[3] is 1
                        self.state = 1
                        self.done_reg = 0
                elif self.state == 1:
                    # Got second byte
                    self.state = 2
                    self.done_reg = 0
                elif self.state == 2:
                    # Got third byte, signal done next cycle
                    self.state = 0
                    self.done_reg = 1

        # Return output dictionary with done signal
        return {'done': format(self.done_reg, 'b')}
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


