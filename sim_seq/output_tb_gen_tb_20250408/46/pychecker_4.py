
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 32-bit LFSR state to 1
        '''
        self.q = 1  # 32-bit LFSR initialized to 1

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Convert input binary strings to integers
        reset_val = int(stimulus_dict['reset'], 2)

        # Only update on clock edge
        if clk == 1:
            if reset_val == 1:
                # Synchronous reset to 1
                self.q = 1
            else:
                # Get current LSB (output bit)
                output_bit = self.q & 1
                
                # Calculate feedback based on taps
                # Taps at 32,22,2,1 mean we XOR output with these positions
                feedback = output_bit
                
                # Create next state by shifting right
                next_q = self.q >> 1
                
                # Apply feedback to tap positions
                if output_bit:
                    next_q ^= (1 << 31)  # Position 32
                    next_q ^= (1 << 21)  # Position 22
                    next_q ^= (1 << 1)   # Position 2
                    next_q ^= (1 << 0)   # Position 1
                
                # Update state
                self.q = next_q & 0xFFFFFFFF  # Mask to 32 bits

        # Return output as 32-bit binary string
        return {'q': format(self.q, '032b')}
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


