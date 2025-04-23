

import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Truth table based on Karnaugh map
        # Key = x[1]x[2]x[3]x[4], Value = f
        # Don't cares (d) optimized for logic minimization
        self._TRUTH_TABLE = {
            # Column 00 (x[1]x[2]=00)
            '0000': '0',  # d->0 (optimized)
            '0001': '0',  
            '0011': '1',
            '0010': '1',
            # Column 01 (x[1]x[2]=01)
            '0100': '0',
            '0101': '1',  # d->1 (optimized)
            '0111': '1',
            '0110': '1',
            # Column 11 (x[1]x[2]=11)
            '1100': '1',  # d->1 (optimized)
            '1101': '1',
            '1111': '1',  # d->1 (optimized)
            '1110': '0',
            # Column 10 (x[1]x[2]=10)
            '1000': '1',  # d->1 (optimized)
            '1001': '0',
            '1011': '0',  # d->0 (optimized)
            '1010': '1'   # d->1 (optimized)
        }

    def load(self, clk, stimulus_dict: Dict[str, any]):
        # Extract input bits
        x = stimulus_dict['x']
        if len(x) != 4:
            raise ValueError('Input x must be 4 bits')
        
        # Create key using Karnaugh map ordering
        # x[1]x[2]x[3]x[4] from input x[4]x[3]x[2]x[1]
        key = x[3] + x[2] + x[1] + x[0]
        
        # Lookup output value
        f_val = self._TRUTH_TABLE[key]
        
        return {'f': f_val}




def check_output(stimulus_list_scenario):

    dut = GoldenDUT()
    tb_outputs = []


    for stimulus_list in stimulus_list_scenario["input variable"]:


        clock_cycles = stimulus_list['clock cycles']
        clk = 1
        input_vars_list = {k: v for k, v in stimulus_list.items() if k != "clock cycles"}
        output_vars_list = {'clock cycles':clock_cycles}
        for k,v in input_vars_list.items():
            if len(v) < clock_cycles:
                v.extend([v[-1]] * (clock_cycles - len(v)))
                
        

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
    stimulus_file_name = "stimulus.json"
    with open(stimulus_file_name, "r") as f:
        stimulus_data = json.load(f)


    if isinstance(stimulus_data, dict):
        stimulus_list_scenarios = stimulus_data.get("input variable", [])
    else:
        stimulus_list_scenarios = stimulus_data

    outputs=[]
    for stimulus_list_scenario in stimulus_list_scenarios:
        outputs.append( check_output(stimulus_list_scenario))
    with open(stimulus_file_name, "w") as f:
        json.dump(stimulus_list_scenarios, f, indent=4)

    print(json.dumps(outputs, indent=2))




