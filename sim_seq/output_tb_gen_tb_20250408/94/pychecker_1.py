
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize FSM state
        '''
        self.SEARCH = 0
        self.BYTE2 = 1
        self.BYTE3 = 2
        self.state = self.SEARCH
        self.done_flag = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update FSM state and outputs on clock edge
        '''
        if clk == 1:  # Only update on clock edge
            # Convert inputs from binary strings
            reset = int(stimulus_dict['reset'], 2)
            in_byte = int(stimulus_dict['in'], 2)
            
            # Handle reset
            if reset:
                self.state = self.SEARCH
                self.done_flag = 0
            else:
                # FSM state transitions
                if self.state == self.SEARCH:
                    if (in_byte & 0x08):  # Check in[3]=1
                        self.state = self.BYTE2
                    self.done_flag = 0
                elif self.state == self.BYTE2:
                    self.state = self.BYTE3
                    self.done_flag = 0
                elif self.state == self.BYTE3:
                    self.state = self.SEARCH
                    self.done_flag = 1  # Signal message complete
                    
        # Return output dictionary
        return {'done': format(self.done_flag, '01b')}
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


