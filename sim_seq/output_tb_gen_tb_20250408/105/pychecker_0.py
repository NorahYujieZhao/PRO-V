
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize internal state registers
        '''
        self.prev_in = 0  # Previous input state, 8-bit
        self.pedge = 0    # Output register, 8-bit

    def load(self, clk, stimulus_dict: Dict[str, str]):
        '''
        Update state and compute outputs on clock edge
        '''
        # Convert input binary string to integer
        in_val = int(stimulus_dict['in'], 2)
        
        if clk == 1:
            # Detect positive edges: ~prev_in & in
            # This sets output bits where prev_in was 0 and in is 1
            self.pedge = (~self.prev_in & in_val) & 0xFF
            # Update previous input state
            self.prev_in = in_val

        # Convert output to 8-bit binary string
        pedge_str = format(self.pedge, '08b')
        
        return {'pedge': pedge_str}
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


