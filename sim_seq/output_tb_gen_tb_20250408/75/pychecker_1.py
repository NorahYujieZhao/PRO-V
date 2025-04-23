
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize FSM state and output
        '''
        self.IDLE = 0
        self.GOT_1 = 1
        self.GOT_11 = 2
        self.GOT_110 = 3
        self.FOUND = 4
        self.current_state = self.IDLE
        self.start_shifting = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''
        Update FSM state and output based on inputs
        '''
        if clk != 1:  # Only update on rising edge
            return {"start_shifting": format(self.start_shifting, 'b')}

        # Convert input signals from binary strings to integers
        reset_val = int(stimulus_dict["reset"], 2)
        data_val = int(stimulus_dict["data"], 2)

        # Handle reset
        if reset_val == 1:
            self.current_state = self.IDLE
            self.start_shifting = 0
            return {"start_shifting": format(self.start_shifting, 'b')}

        # State machine transitions
        if self.current_state == self.IDLE:
            if data_val == 1:
                self.current_state = self.GOT_1
        elif self.current_state == self.GOT_1:
            if data_val == 1:
                self.current_state = self.GOT_11
            elif data_val == 0:
                self.current_state = self.IDLE
        elif self.current_state == self.GOT_11:
            if data_val == 0:
                self.current_state = self.GOT_110
            elif data_val == 1:
                self.current_state = self.GOT_11
        elif self.current_state == self.GOT_110:
            if data_val == 1:
                self.current_state = self.FOUND
            else:
                self.current_state = self.IDLE
        # FOUND state: stay in this state forever

        # Update output
        self.start_shifting = 1 if self.current_state == self.FOUND else 0

        return {"start_shifting": format(self.start_shifting, 'b')}
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


