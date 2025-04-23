
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''Initialize branch predictor state'''
        self.branch_history = 0  # 7-bit history register
        self.pht = [2] * 128     # 128 entries, initialized to weakly taken (2)
    
    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        # Convert inputs from binary strings
        predict_valid = int(stimulus_dict.get('predict_valid', '0'), 2)
        predict_pc = int(stimulus_dict.get('predict_pc', '0'), 2)
        train_valid = int(stimulus_dict.get('train_valid', '0'), 2)
        train_taken = int(stimulus_dict.get('train_taken', '0'), 2)
        train_mispredicted = int(stimulus_dict.get('train_mispredicted', '0'), 2)
        train_history = int(stimulus_dict.get('train_history', '0'), 2)
        train_pc = int(stimulus_dict.get('train_pc', '0'), 2)
        areset = int(stimulus_dict.get('areset', '0'), 2)

        # Handle reset
        if areset:
            self.branch_history = 0
            self.pht = [2] * 128
            return {
                'predict_taken': '0',
                'predict_history': format(0, '07b')
            }

        # Calculate prediction
        predict_index = predict_pc ^ self.branch_history
        predict_taken = '1' if self.pht[predict_index] >= 2 else '0'
        current_history = format(self.branch_history, '07b')
        
        # Handle training
        if train_valid and clk == 1:
            train_index = train_pc ^ train_history
            if train_taken:
                self.pht[train_index] = min(3, self.pht[train_index] + 1)
            else:
                self.pht[train_index] = max(0, self.pht[train_index] - 1)
                
            # Restore history on misprediction
            if train_mispredicted:
                self.branch_history = train_history
                # Shift in actual outcome
                self.branch_history = ((self.branch_history << 1) | train_taken) & 0x7F
                
        # Update history for prediction if no training this cycle
        elif predict_valid and clk == 1 and not train_valid:
            predicted_outcome = 1 if predict_taken == '1' else 0
            self.branch_history = ((self.branch_history << 1) | predicted_outcome) & 0x7F

        return {
            'predict_taken': predict_taken,
            'predict_history': current_history
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


