
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        self.grid = 0  # 256-bit grid initialized to 0

    def get_cell(self, x, y):
        # Get cell value at (x,y) from 256-bit grid
        idx = y * 16 + x
        return (self.grid >> idx) & 1

    def count_neighbors(self, x, y):
        count = 0
        # Check all 8 neighboring cells with toroidal wrapping
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = (x + dx) % 16  # Wrap around horizontally
                ny = (y + dy) % 16  # Wrap around vertically
                count += self.get_cell(nx, ny)
        return count

    def next_state(self, x, y):
        neighbors = self.count_neighbors(x, y)
        current = self.get_cell(x, y)
        
        if neighbors <= 1:
            return 0  # Dies from loneliness
        elif neighbors == 2:
            return current  # Stays the same
        elif neighbors == 3:
            return 1  # Becomes/stays alive
        else:
            return 0  # Dies from overcrowding

    def load(self, clk, stimulus_dict):
        if clk == 1:
            load_signal = int(stimulus_dict.get('load', '0'), 2)
            if load_signal:
                # Load new state from data input
                self.grid = int(stimulus_dict['data'], 2)
            else:
                # Calculate next state for each cell
                new_grid = 0
                for y in range(16):
                    for x in range(16):
                        new_state = self.next_state(x, y)
                        if new_state:
                            idx = y * 16 + x
                            new_grid |= (1 << idx)
                self.grid = new_grid

        # Convert grid to 256-bit binary string
        q_str = format(self.grid, '0256b')
        return {'q': q_str}
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


