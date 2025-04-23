
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        self.state = 0  # 256-bit state representing 16x16 grid

    def count_neighbors(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                # Handle toroidal wrapping
                nx = (x + dx) % 16
                ny = (y + dy) % 16
                # Calculate bit position in 256-bit vector
                bit_pos = ny * 16 + nx
                if (self.state >> bit_pos) & 1:
                    count += 1
        return count

    def get_next_state(self, x, y):
        neighbors = self.count_neighbors(x, y)
        curr_cell = (self.state >> (y * 16 + x)) & 1
        
        if neighbors <= 1:
            return 0
        elif neighbors == 2:
            return curr_cell
        elif neighbors == 3:
            return 1
        else:  # neighbors >= 4
            return 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        if clk == 1:
            load_val = int(stimulus_dict.get('load', '0'), 2)
            data_val = int(stimulus_dict.get('data', '0' * 256), 2)
            
            if load_val:
                # Load new state when load is high
                self.state = data_val
            else:
                # Calculate next state based on Game of Life rules
                next_state = 0
                for y in range(16):
                    for x in range(16):
                        if self.get_next_state(x, y):
                            next_state |= (1 << (y * 16 + x))
                self.state = next_state

        # Return current state as 256-bit binary string
        return {'q': format(self.state, '0256b')}
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


