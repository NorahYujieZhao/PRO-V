
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''Initialize state registers'''
        self.state = 0  # Number of consecutive 1s seen
        self.disc_reg = 0  # Registered disc output
        self.flag_reg = 0  # Registered flag output 
        self.err_reg = 0   # Registered error output

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''Process inputs and update state'''
        # Only process on clock edge
        if clk != 1:
            return {"disc": format(self.disc_reg, 'b'),
                    "flag": format(self.flag_reg, 'b'),
                    "err": format(self.err_reg, 'b')}

        # Get input signals
        reset = int(stimulus_dict["reset"], 2)
        in_bit = int(stimulus_dict["in"], 2)

        # Handle reset
        if reset:
            next_state = 0
        else:
            # Update state based on input
            if in_bit == 0:
                next_state = 0
            else:
                next_state = self.state + 1

        # Calculate next outputs (registered)
        if self.state == 5 and in_bit == 0:
            next_disc = 1
        else:
            next_disc = 0

        if self.state == 6 and in_bit == 0:
            next_flag = 1
        else:
            next_flag = 0

        if self.state >= 7 or (self.state == 6 and in_bit == 1):
            next_err = 1
        else:
            next_err = 0

        # Update registers
        self.state = next_state
        self.disc_reg = next_disc
        self.flag_reg = next_flag
        self.err_reg = next_err

        # Return current outputs
        return {"disc": format(self.disc_reg, 'b'),
                "flag": format(self.flag_reg, 'b'),
                "err": format(self.err_reg, 'b')}
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


