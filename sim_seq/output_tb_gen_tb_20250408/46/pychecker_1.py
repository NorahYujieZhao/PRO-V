
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 32-bit LFSR register to 0
        '''
        self.q = 0  # 32-bit LFSR register

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update LFSR state on clock edge based on reset and tap positions
        '''
        # Convert reset input from binary string to integer
        reset_val = int(stimulus_dict['reset'], 2)

        # Only update on clock edge (clk == 1)
        if clk == 1:
            if reset_val == 1:
                # Synchronous reset to 32'h1
                self.q = 1
            else:
                # Get current value of tap positions
                tap32 = (self.q >> 31) & 1  # MSB (position 32)
                tap22 = (self.q >> 21) & 1  # Position 22
                tap2 = (self.q >> 1) & 1    # Position 2
                tap1 = self.q & 1           # Position 1 (LSB)
                
                # Calculate feedback bit using XOR of taps
                feedback = tap32 ^ tap22 ^ tap2 ^ tap1
                
                # Shift right and insert feedback at MSB
                self.q = ((feedback << 31) | (self.q >> 1)) & 0xFFFFFFFF

        # Convert output to 32-bit binary string
        q_str = format(self.q, '032b')
        
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


