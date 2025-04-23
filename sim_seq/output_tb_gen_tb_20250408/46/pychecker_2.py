
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
        Update LFSR state on rising clock edge
        '''
        # Convert input binary strings to integers
        reset_val = int(stimulus_dict['reset'], 2)

        # Only update on rising clock edge
        if clk == 1:
            if reset_val == 1:
                # Synchronous reset to 1
                self.q = 1
            else:
                # Get output bit (LSB)
                output_bit = self.q & 1
                
                # Calculate next state
                # XOR taps (32,22,2,1) with output bit if output_bit is 1
                next_q = self.q >> 1  # Basic right shift
                if output_bit:
                    # XOR with taps when output bit is 1
                    next_q ^= (1 << 31)  # Tap at bit 32
                    next_q ^= (1 << 21)  # Tap at bit 22
                    next_q ^= (1 << 1)   # Tap at bit 2
                    next_q ^= (1 << 0)   # Tap at bit 1
                
                # Update state
                self.q = next_q & 0xFFFFFFFF  # Ensure 32-bit value

        # Convert current state to 32-bit binary string
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


