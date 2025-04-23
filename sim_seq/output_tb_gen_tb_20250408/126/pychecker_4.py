
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the flip-flop output to 0
        '''
        self.out_reg = 0  # flip-flop output initialized to 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Get input signal from stimulus dictionary
        in_val = int(stimulus_dict['in'], 2)

        # On positive clock edge, update the flip-flop
        if clk == 1:
            # Calculate XOR of input and current output
            next_out = in_val ^ self.out_reg
            # Update the flip-flop state
            self.out_reg = next_out

        # Convert output to binary string
        out_str = format(self.out_reg, 'b')

        # Return the output dictionary
        return {'out': out_str}
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


