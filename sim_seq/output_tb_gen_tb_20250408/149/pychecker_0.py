
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize branch predictor state:
        - 7-bit global history register (GHR)
        - 128-entry pattern history table (PHT) of 2-bit saturating counters
        '''
        self.ghr = 0  # Global History Register
        self.pht = [1] * 128  # Initialize all counters to Weakly Not Taken (1)

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Handle prediction and training logic
        '''
        # Convert inputs from binary strings
        predict_valid = int(stimulus_dict.get('predict_valid', '0'), 2)
        predict_pc = int(stimulus_dict.get('predict_pc', '0'), 2)
        train_valid = int(stimulus_dict.get('train_valid', '0'), 2)
        train_taken = int(stimulus_dict.get('train_taken', '0'), 2)
        train_mispredicted = int(stimulus_dict.get('train_mispredicted', '0'), 2)
        train_history = int(stimulus_dict.get('train_history', '0'), 2)
        train_pc = int(stimulus_dict.get('train_pc', '0'), 2)
        areset = int(stimulus_dict.get('areset', '0'), 2)

        # Initialize output dictionary
        output = {}

        # Handle reset
        if areset:
            self.ghr = 0
            self.pht = [1] * 128
            output['predict_taken'] = '0'
            output['predict_history'] = format(0, '07b')
            return output

        # Get current GHR state for prediction output
        output['predict_history'] = format(self.ghr, '07b')

        # Handle prediction
        if predict_valid:
            # Calculate PHT index by XORing PC with GHR
            pred_idx = (predict_pc ^ self.ghr) & 0x7F
            # Get prediction from PHT
            pred_taken = self.pht[pred_idx] >= 2
            output['predict_taken'] = '1' if pred_taken else '0'

        # Handle training
        if clk and train_valid:
            # Calculate PHT index for training
            train_idx = (train_pc ^ train_history) & 0x7F
            # Update PHT entry (saturating counter)
            if train_taken:
                self.pht[train_idx] = min(3, self.pht[train_idx] + 1)
            else:
                self.pht[train_idx] = max(0, self.pht[train_idx] - 1)
            # Update GHR if mispredicted
            if train_mispredicted:
                self.ghr = ((train_history << 1) | train_taken) & 0x7F
        # Update GHR for prediction if no training this cycle
        elif clk and predict_valid and not train_valid:
            pred_taken = (self.pht[(predict_pc ^ self.ghr) & 0x7F] >= 2)
            self.ghr = ((self.ghr << 1) | (1 if pred_taken else 0)) & 0x7F

        return output
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


