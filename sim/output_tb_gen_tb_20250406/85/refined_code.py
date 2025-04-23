

import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state needed for combinational logic
        pass
    
    def load(self, clk, stimulus_dict):
        # Convert inputs to integers
        a = int(stimulus_dict['a'])
        b = int(stimulus_dict['b'])
        c = int(stimulus_dict['c'])
        d = int(stimulus_dict['d'])
        
        # Implement K-map logic
        if a == 0 and b == 0:  # ab = 00
            if c == 0 and d == 0:  # cd = 00
                out = 0
            elif c == 0 and d == 1:  # cd = 01
                out = 0
            else:  # cd = 10 or cd = 11
                out = 1
        elif a == 0 and b == 1:  # ab = 01
            # Choose 0 for don't care cases
            out = 0
        else:  # ab = 10 or ab = 11
            if c == 0 and d == 1:  # cd = 01
                # Choose 1 for don't care case
                out = 1
            else:
                out = 1
        
        return {'out': str(out)}




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




