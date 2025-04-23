
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''Initialize FSM state and outputs'''
        self.state = 0  # Current state (0-7)
        self.disc_out = 0
        self.flag_out = 0
        self.err_out = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''Process inputs and update state on clock edge'''
        if clk == 1:  # Rising edge
            # Convert input signals
            reset = int(stimulus_dict['reset'], 2)
            in_bit = int(stimulus_dict['in'], 2)

            # Handle reset
            if reset:
                next_state = 0
            else:
                # State machine logic
                if in_bit == 1:
                    if self.state < 7:
                        next_state = self.state + 1
                    else:
                        next_state = 7  # Stay in error state
                else:  # in_bit == 0
                    if self.state == 6:
                        next_state = 0  # Complete flag sequence
                    elif self.state == 7:
                        next_state = 7  # Stay in error state
                    else:
                        next_state = 0  # Reset count

            # Update state
            self.state = next_state

            # Moore outputs based on state
            self.disc_out = 1 if self.state == 5 and in_bit == 0 else 0
            self.flag_out = 1 if self.state == 6 and in_bit == 0 else 0
            self.err_out = 1 if self.state == 7 else 0

        # Return outputs as binary strings
        return {
            'disc': format(self.disc_out, 'b'),
            'flag': format(self.flag_out, 'b'),
            'err': format(self.err_out, 'b')
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


