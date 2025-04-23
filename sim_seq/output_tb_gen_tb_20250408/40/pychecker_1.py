
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 32-bit history register to 0
        '''
        self.history = 0  # 32-bit history register

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        '''
        Update history register based on inputs
        '''
        # Convert input binary strings to integers
        areset = int(stimulus_dict.get('areset', '0'), 2)
        predict_valid = int(stimulus_dict.get('predict_valid', '0'), 2)
        predict_taken = int(stimulus_dict.get('predict_taken', '0'), 2)
        train_mispredicted = int(stimulus_dict.get('train_mispredicted', '0'), 2)
        train_taken = int(stimulus_dict.get('train_taken', '0'), 2)
        train_history = int(stimulus_dict.get('train_history', '0' * 32), 2)

        if clk == 1:
            # Handle asynchronous reset
            if areset:
                self.history = 0
            # Handle misprediction (takes precedence)
            elif train_mispredicted:
                # Concatenate train_history with train_taken
                self.history = ((train_history << 1) | train_taken) & 0xFFFFFFFF
            # Handle prediction
            elif predict_valid:
                # Shift in predict_taken from LSB
                self.history = ((self.history << 1) | predict_taken) & 0xFFFFFFFF

        # Return current history as 32-bit binary string
        return {'predict_history': format(self.history, '032b')}
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


