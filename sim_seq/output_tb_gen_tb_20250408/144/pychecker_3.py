
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize FSM state to 0 (equivalent to seeing a 0)
        Initialize all output signals to 0
        '''
        self.state = 0  # Number of consecutive 1s seen (0-7)
        self.disc = 0
        self.flag = 0
        self.err = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''
        Update FSM state and outputs based on input signals
        '''
        # Only process on rising edge of clock
        if clk == 1:
            # Get input signals
            reset = int(stimulus_dict['reset'], 2)
            in_bit = int(stimulus_dict['in'], 2)

            # Handle synchronous reset
            if reset:
                self.state = 0
                self.disc = 0
                self.flag = 0
                self.err = 0
            else:
                # Calculate next state based on input
                if in_bit == 1:
                    # Input is 1, increment consecutive 1s count
                    if self.state < 7:
                        self.state += 1
                else:
                    # Input is 0, check for special conditions
                    if self.state == 5:
                        self.disc = 1  # Signal bit discard
                    elif self.state == 6:
                        self.flag = 1  # Signal frame boundary
                    else:
                        self.disc = 0
                        self.flag = 0
                    self.state = 0

                # Check for error condition (7 or more 1s)
                if self.state == 7:
                    self.err = 1
                else:
                    self.err = 0

        # Return output signals as binary strings
        return {
            'disc': format(self.disc, 'b'),
            'flag': format(self.flag, 'b'),
            'err': format(self.err, 'b')
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


