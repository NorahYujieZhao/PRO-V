
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        self.q = 0  # 256-bit grid state

    def get_cell(self, state, x, y):
        pos = y * 16 + x
        return (state >> pos) & 1

    def count_neighbors(self, state, x, y):
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = (x + dx) % 16
                ny = (y + dy) % 16
                count += self.get_cell(state, nx, ny)
        return count

    def calculate_next_state(self):
        next_state = 0
        for y in range(16):
            for x in range(16):
                neighbors = self.count_neighbors(self.q, x, y)
                current = self.get_cell(self.q, x, y)
                pos = y * 16 + x
                
                if neighbors <= 1:
                    new_state = 0
                elif neighbors == 2:
                    new_state = current
                elif neighbors == 3:
                    new_state = 1
                else:  # neighbors >= 4
                    new_state = 0
                    
                next_state |= (new_state << pos)
        return next_state

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        if clk == 1:
            if int(stimulus_dict['load'], 2) == 1:
                self.q = int(stimulus_dict['data'], 2)
            else:
                self.q = self.calculate_next_state()
        
        return {'q': format(self.q, '0256b')}
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


