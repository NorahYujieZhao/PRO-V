
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 512-bit register to 0
        '''
        self.q = 0  # 512-bit register

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Process one clock cycle of the Rule 90 cellular automaton
        '''
        # Convert input signals from binary strings to integers
        load_val = int(stimulus_dict['load'], 2)
        data_val = int(stimulus_dict['data'], 2)
        
        if clk == 1:  # Rising edge
            if load_val == 1:
                # Load new data
                self.q = data_val
            else:
                # Apply Rule 90
                next_q = 0
                current_q = self.q
                
                # Process each cell
                for i in range(512):
                    # Get left neighbor (0 for leftmost cell)
                    left = (current_q >> (i+1)) & 1 if i < 511 else 0
                    # Get right neighbor (0 for rightmost cell)
                    right = (current_q >> (i-1)) & 1 if i > 0 else 0
                    # Rule 90: next state is XOR of neighbors
                    next_bit = left ^ right
                    # Set the bit in the next state
                    next_q |= (next_bit << i)
                
                self.q = next_q

        # Convert output to 512-bit binary string
        q_str = format(self.q, '0512b')
        
        return {'q': q_str}
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


