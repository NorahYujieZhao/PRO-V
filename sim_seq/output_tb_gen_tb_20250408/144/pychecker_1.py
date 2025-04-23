
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize FSM state and output registers
        '''
        self.state = 0  # Start in ZERO state
        self.disc_reg = 0
        self.flag_reg = 0
        self.err_reg = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update FSM state and outputs on clock edge
        '''
        # Convert input signals from binary strings
        reset = int(stimulus_dict['reset'], 2)
        in_bit = int(stimulus_dict['in'], 2)
        
        # Only update on clock edge
        if clk == 1:
            # Handle synchronous reset
            if reset:
                self.state = 0
                self.disc_reg = 0
                self.flag_reg = 0
                self.err_reg = 0
            else:
                # Default all outputs to 0
                next_disc = 0
                next_flag = 0
                next_err = 0
                
                # State machine transitions
                if in_bit == 0:
                    # Input is 0, reset consecutive 1s count
                    next_state = 0
                else:
                    # Input is 1, increment state
                    next_state = self.state + 1
                    if next_state == 5:
                        # After 5 ones, signal bit discard
                        next_disc = 1
                    elif next_state == 6:
                        # After 6 ones, signal flag
                        next_flag = 1
                    elif next_state >= 7:
                        # 7 or more ones is error
                        next_err = 1
                        next_state = 7  # Stay in error state
                
                # Update state and output registers
                self.state = next_state
                self.disc_reg = next_disc
                self.flag_reg = next_flag
                self.err_reg = next_err

        # Convert outputs to binary strings
        return {
            'disc': format(self.disc_reg, 'b'),
            'flag': format(self.flag_reg, 'b'),
            'err': format(self.err_reg, 'b')
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


