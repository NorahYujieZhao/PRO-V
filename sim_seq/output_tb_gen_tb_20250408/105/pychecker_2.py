
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize internal state registers.
        prev_in: stores previous input value for edge detection
        '''
        self.prev_in = 0  # 8-bit register for previous input

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Detect positive edges (0->1 transitions) on each bit
        '''
        # Convert input binary string to integer
        in_val = int(stimulus_dict['in'], 2)
        
        # Only update on clock edge
        if clk == 1:
            # Detect positive edges by finding bits that were 0 and are now 1
            pedge_val = (in_val & (~self.prev_in)) & 0xFF
            
            # Update previous input value for next cycle
            self.prev_in = in_val
            
            # Convert output to 8-bit binary string
            pedge_str = format(pedge_val, '08b')
            
            return {'pedge': pedge_str}
        
        # On non-clock cycles, maintain previous output
        pedge_str = format(0, '08b')
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


