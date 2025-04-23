
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''Initialize the 32-bit history register to 0'''
        self.history_reg = 0  # 32-bit history register

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''Process inputs and update state'''
        # Convert input binary strings to integers
        areset = int(stimulus_dict.get('areset', '0'), 2)
        predict_valid = int(stimulus_dict.get('predict_valid', '0'), 2)
        predict_taken = int(stimulus_dict.get('predict_taken', '0'), 2)
        train_mispredicted = int(stimulus_dict.get('train_mispredicted', '0'), 2)
        train_taken = int(stimulus_dict.get('train_taken', '0'), 2)
        train_history = int(stimulus_dict.get('train_history', '0' * 32), 2)

        if areset == 1:
            # Asynchronous reset - clear history
            self.history_reg = 0
        elif clk == 1:
            if train_mispredicted == 1:
                # Handle misprediction - concatenate train_history with train_taken
                self.history_reg = ((train_history << 1) | train_taken) & 0xFFFFFFFF
            elif predict_valid == 1:
                # Normal prediction - shift in predict_taken from LSB
                self.history_reg = ((self.history_reg << 1) | predict_taken) & 0xFFFFFFFF

        # Convert output to 32-bit binary string
        predict_history = format(self.history_reg, '032b')
        
        return {'predict_history': predict_history}
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


