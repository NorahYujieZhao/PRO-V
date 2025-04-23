
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        self.q = 0  # 256-bit game state
        self.grid = [[0 for _ in range(16)] for _ in range(16)]

    def _vector_to_grid(self, vector):
        for i in range(16):
            for j in range(16):
                bit_pos = i * 16 + j
                self.grid[i][j] = (vector >> bit_pos) & 1

    def _grid_to_vector(self):
        vector = 0
        for i in range(16):
            for j in range(16):
                if self.grid[i][j]:
                    vector |= (1 << (i * 16 + j))
        return vector

    def _count_neighbors(self, row, col):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                neighbor_row = (row + i) % 16
                neighbor_col = (col + j) % 16
                count += self.grid[neighbor_row][neighbor_col]
        return count

    def _apply_rules(self):
        new_grid = [[0 for _ in range(16)] for _ in range(16)]
        for i in range(16):
            for j in range(16):
                neighbors = self._count_neighbors(i, j)
                if neighbors == 2:
                    new_grid[i][j] = self.grid[i][j]
                elif neighbors == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0
        self.grid = new_grid

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        if clk == 1:
            load_val = int(stimulus_dict.get('load', '0'), 2)
            data_val = int(stimulus_dict.get('data', '0' * 256), 2)
            
            if load_val:
                self.q = data_val
                self._vector_to_grid(data_val)
            else:
                self._vector_to_grid(self.q)
                self._apply_rules()
                self.q = self._grid_to_vector()

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


