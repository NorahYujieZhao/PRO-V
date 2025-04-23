
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize branch predictor state
        '''
        self.history = 0  # 7-bit global history register
        self.pht = [0] * 128  # 128 entries of 2-bit saturating counters

    def get_index(self, pc, history):
        '''
        Generate 7-bit index by XORing PC and history
        '''
        return (pc ^ history) & 0x7F

    def predict(self, pc, history):
        '''
        Make prediction based on PHT entry
        '''
        index = self.get_index(pc, history)
        return self.pht[index] >= 2  # Predict taken if counter >= 2

    def update_counter(self, index, taken):
        '''
        Update 2-bit saturating counter
        '''
        if taken:
            if self.pht[index] < 3:
                self.pht[index] += 1
        else:
            if self.pht[index] > 0:
                self.pht[index] -= 1

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Handle prediction and training interfaces
        '''
        # Convert inputs from binary strings to integers
        areset = int(stimulus_dict.get('areset', '0'), 2)
        predict_valid = int(stimulus_dict.get('predict_valid', '0'), 2)
        predict_pc = int(stimulus_dict.get('predict_pc', '0'), 2)
        train_valid = int(stimulus_dict.get('train_valid', '0'), 2)
        train_taken = int(stimulus_dict.get('train_taken', '0'), 2)
        train_mispredicted = int(stimulus_dict.get('train_mispredicted', '0'), 2)
        train_history = int(stimulus_dict.get('train_history', '0'), 2)
        train_pc = int(stimulus_dict.get('train_pc', '0'), 2)

        # Handle asynchronous reset
        if areset:
            self.history = 0
            self.pht = [0] * 128
            return {'predict_taken': '0', 'predict_history': format(0, '07b')}

        predict_taken = 0
        next_history = self.history

        # Handle training (takes precedence)
        if train_valid and clk == 1:
            train_index = self.get_index(train_pc, train_history)
            self.update_counter(train_index, train_taken)
            if train_mispredicted:
                next_history = train_history

        # Handle prediction
        if predict_valid and not (train_valid and train_mispredicted):
            predict_taken = 1 if self.predict(predict_pc, self.history) else 0
            next_history = ((self.history << 1) | predict_taken) & 0x7F

        # Update history on clock edge
        if clk == 1:
            self.history = next_history

        # Return outputs as binary strings
        return {
            'predict_taken': format(predict_taken, 'b'),
            'predict_history': format(self.history, '07b')
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


