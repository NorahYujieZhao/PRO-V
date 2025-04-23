
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state registers
        States: A=0, B=1
        Reset state is B
        '''
        self.current_state = 1  # Start in state B

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''
        Update state machine on clock edge
        '''
        # Convert input signals from binary strings to integers
        reset_val = int(stimulus_dict['reset'], 2)
        in_val = int(stimulus_dict['in'], 2)
        
        # Only update on clock edge
        if clk == 1:
            # Handle synchronous reset
            if reset_val == 1:
                self.current_state = 1  # Go to state B
            else:
                # State transition logic
                if self.current_state == 1:  # Currently in state B
                    if in_val == 0:
                        self.current_state = 0  # Go to state A
                else:  # Currently in state A
                    if in_val == 0:
                        self.current_state = 1  # Go to state B

        # Moore output depends only on current state
        out_val = 1 if self.current_state == 1 else 0
        
        # Return output as binary string
        return {'out': format(out_val, 'b')}
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


