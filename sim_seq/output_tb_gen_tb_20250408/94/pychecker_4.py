
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize state machine to SEARCH state
        '''
        self.SEARCH = 0  # Looking for byte with in[3]=1
        self.BYTE2 = 1   # Receiving second byte
        self.BYTE3 = 2   # Receiving third byte
        self.state = self.SEARCH
        self.done = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update FSM state and outputs based on inputs
        '''
        if clk == 1:  # Only update on rising edge
            # Convert input signals from binary strings
            reset = int(stimulus_dict['reset'], 2)
            in_byte = int(stimulus_dict['in'], 2)
            
            # Reset takes precedence
            if reset:
                self.state = self.SEARCH
                self.done = 0
            else:
                # State machine transitions
                if self.state == self.SEARCH:
                    if (in_byte & 0x08):  # Check if in[3] is 1
                        self.state = self.BYTE2
                    self.done = 0
                elif self.state == self.BYTE2:
                    self.state = self.BYTE3
                    self.done = 0
                elif self.state == self.BYTE3:
                    self.state = self.SEARCH
                    self.done = 1

        # Return output signals as binary strings
        return {"done": format(self.done, '01b')}
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


