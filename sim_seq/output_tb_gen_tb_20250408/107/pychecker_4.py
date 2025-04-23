
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 512-bit state register to 0
        '''
        self.q = 0  # 512-bit state register

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''
        Update state based on Rule 90 cellular automaton rules
        '''
        if clk == 1:  # Only update on clock edge
            load_val = int(stimulus_dict.get('load', '0'), 2)
            data_val = int(stimulus_dict.get('data', '0' * 512), 2)
            
            if load_val:
                # Load new data
                self.q = data_val
            else:
                # Apply Rule 90
                current_q = format(self.q, '0512b')
                next_q = ['0'] * 512
                
                # First cell (left neighbor is 0)
                next_q[0] = '1' if current_q[1] == '1' else '0'
                
                # Middle cells
                for i in range(1, 511):
                    next_q[i] = '1' if int(current_q[i-1]) ^ int(current_q[i+1]) else '0'
                
                # Last cell (right neighbor is 0)
                next_q[511] = '1' if current_q[510] == '1' else '0'
                
                # Convert back to integer
                self.q = int(''.join(next_q), 2)
        
        # Return current state as binary string
        return {'q': format(self.q, '0512b')}
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


