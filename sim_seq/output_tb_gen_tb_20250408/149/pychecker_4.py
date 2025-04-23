
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        self.history = 0  # 7-bit global history register
        self.pht = [0] * 128  # 128 entries of 2-bit saturating counters

    def get_pht_index(self, pc, history):
        # XOR hash of PC and history for 7-bit index
        return (pc ^ history) & 0x7F

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        output_dict = {}
        
        # Convert inputs from binary strings
        areset = int(stimulus_dict.get('areset', '0'), 2)
        predict_valid = int(stimulus_dict.get('predict_valid', '0'), 2)
        predict_pc = int(stimulus_dict.get('predict_pc', '0'), 2)
        train_valid = int(stimulus_dict.get('train_valid', '0'), 2)
        train_taken = int(stimulus_dict.get('train_taken', '0'), 2)
        train_mispredicted = int(stimulus_dict.get('train_mispredicted', '0'), 2)
        train_history = int(stimulus_dict.get('train_history', '0'), 2)
        train_pc = int(stimulus_dict.get('train_pc', '0'), 2)

        # Asynchronous reset
        if areset:
            self.history = 0
            self.pht = [0] * 128
            output_dict['predict_taken'] = '0'
            output_dict['predict_history'] = format(0, '07b')
            return output_dict

        # Handle prediction
        if predict_valid:
            index = self.get_pht_index(predict_pc, self.history)
            # Predict taken if counter >= 2
            predict_taken = 1 if self.pht[index] >= 2 else 0
            output_dict['predict_taken'] = format(predict_taken, 'b')
            output_dict['predict_history'] = format(self.history, '07b')

        # Handle training at clock edge
        if clk == 1:
            if train_valid:
                # Update PHT
                train_index = self.get_pht_index(train_pc, train_history)
                if train_taken:
                    # Increment counter, saturate at 3
                    self.pht[train_index] = min(3, self.pht[train_index] + 1)
                else:
                    # Decrement counter, saturate at 0
                    self.pht[train_index] = max(0, self.pht[train_index] - 1)
                
                # Update history register on misprediction
                if train_mispredicted:
                    self.history = ((train_history << 1) | train_taken) & 0x7F
                
            # Update history for prediction if no training or no misprediction
            elif predict_valid and not (train_valid and train_mispredicted):
                predict_taken = 1 if self.pht[self.get_pht_index(predict_pc, self.history)] >= 2 else 0
                self.history = ((self.history << 1) | predict_taken) & 0x7F

        return output_dict
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


