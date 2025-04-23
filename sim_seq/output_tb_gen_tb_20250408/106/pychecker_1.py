
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers
        '''
        self.prev_p = 0  # Track previous p value
        self.p_out = 0   # Current p output
        self.q_out = 0   # Current q output

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''
        Update state and outputs based on inputs
        '''
        # Convert input binary string to integer
        a_val = int(stimulus_dict['a'], 2)
        
        # Store previous p value
        self.prev_p = self.p_out
        
        # Update p - follows a when clock is high
        if clk == 1:
            self.p_out = a_val
            
        # Update q based on p transitions
        if self.prev_p == 1 and self.p_out == 0:
            self.q_out = 1  # Set q when p goes from 1 to 0
        elif self.prev_p == 0 and self.p_out == 1:
            self.q_out = 0  # Reset q when p goes from 0 to 1
            
        # Convert outputs to binary strings
        return {
            'p': format(self.p_out, 'b'),
            'q': format(self.q_out, 'b')
        }
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


