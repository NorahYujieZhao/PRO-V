

import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No internal state needed - purely combinational logic
        pass

    def load(self, clk, stimulus_dict: Dict[str, str]):
        # Get inputs
        y_str = stimulus_dict['y']
        w = stimulus_dict['w']
        
        # Convert y to dict with indices [6:1]
        y_dict = {f'[{6-i}]': int(b) for i, b in enumerate(y_str)}
        
        # Initialize outputs
        Y2 = '0'
        Y4 = '0'
        
        # Validate one-hot encoding (exactly one 1)
        if sum(y_dict.values()) != 1:
            return {'Y2': '0', 'Y4': '0'}
        
        # State A (y[1]): Y2=1 when w=0
        if y_dict['[1]'] == 1 and w == '0':
            Y2 = '1'
            
        # State C (y[3]): Y4=1 when w=0
        if y_dict['[3]'] == 1 and w == '0':
            Y4 = '1'
            
        return {
            'Y2': Y2,
            'Y4': Y4
        }




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




