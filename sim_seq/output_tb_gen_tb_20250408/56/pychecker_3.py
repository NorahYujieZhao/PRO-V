
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize registers for dual-edge triggered flip-flop
        '''
        self.pos_reg = 0  # Register for positive edge
        self.neg_reg = 0  # Register for negative edge
        self.prev_clk = 0  # Track previous clock value
        self.q_out = 0    # Output value

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update state on clock edges and return output
        '''
        # Convert input d from binary string to integer
        d_val = int(stimulus_dict['d'], 2)

        # Detect clock edges by comparing with previous clock
        if clk == 1 and self.prev_clk == 0:  # Positive edge
            self.pos_reg = d_val
            self.q_out = d_val
        elif clk == 0 and self.prev_clk == 1:  # Negative edge
            self.neg_reg = d_val
            self.q_out = d_val

        # Update previous clock value
        self.prev_clk = clk

        # Return output as binary string
        return {'q': format(self.q_out, 'b')}
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


