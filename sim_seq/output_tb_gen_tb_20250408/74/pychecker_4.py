
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the internal counter to 0
        '''
        self.counter = 0  # 10-bit counter initialized to 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Only process on rising edge of clock
        if clk == 1:
            # Convert input signals from binary strings to integers
            load_val = int(stimulus_dict['load'], 2)
            data_val = int(stimulus_dict['data'], 2)

            # If load is asserted, load the counter with input data
            if load_val == 1:
                self.counter = data_val
            # If load is not asserted and counter is not 0, decrement
            elif self.counter > 0:
                self.counter = self.counter - 1

        # tc is 1 when counter is 0
        tc_val = 1 if self.counter == 0 else 0

        # Return output dictionary with tc as binary string
        return {'tc': format(tc_val, 'b')}
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


