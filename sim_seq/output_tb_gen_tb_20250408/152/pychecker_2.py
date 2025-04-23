
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        self.grid = [[0 for _ in range(16)] for _ in range(16)]

    def _vector_to_grid(self, vector):
        for row in range(16):
            for col in range(16):
                bit_pos = row * 16 + col
                self.grid[row][col] = (vector >> bit_pos) & 1

    def _grid_to_vector(self):
        vector = 0
        for row in range(16):
            for col in range(16):
                bit_pos = row * 16 + col
                vector |= (self.grid[row][col] << bit_pos)
        return vector

    def _count_neighbors(self, row, col):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr = (row + dr) % 16
                nc = (col + dc) % 16
                count += self.grid[nr][nc]
        return count

    def _update_grid(self):
        new_grid = [[0 for _ in range(16)] for _ in range(16)]
        for row in range(16):
            for col in range(16):
                neighbors = self._count_neighbors(row, col)
                if neighbors == 2:
                    new_grid[row][col] = self.grid[row][col]
                elif neighbors == 3:
                    new_grid[row][col] = 1
                else:
                    new_grid[row][col] = 0
        self.grid = new_grid

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        if clk == 1:
            load_val = int(stimulus_dict.get('load', '0'), 2)
            if load_val:
                data_val = int(stimulus_dict.get('data', '0' * 256), 2)
                self._vector_to_grid(data_val)
            else:
                self._update_grid()

        q_val = self._grid_to_vector()
        return {'q': format(q_val, '0256b')}
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


