
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 5-bit LFSR register to 1
        '''
        self.q = 1  # 5-bit LFSR initialized to 1

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        # Only process on rising clock edge
        if clk == 1:
            # Convert reset signal from binary string to integer
            reset = int(stimulus_dict['reset'], 2)
            
            if reset:
                # Synchronous reset - set to 1
                self.q = 1
            else:
                # Get current state
                current_state = self.q
                
                # Get feedback bit (LSB)
                feedback = current_state & 1
                
                # Calculate next state
                next_state = current_state >> 1  # Shift right by 1
                
                # Apply XOR feedback to tap positions (5 and 3)
                if feedback:
                    next_state ^= (1 << 4)  # XOR bit 5 (index 4)
                    next_state ^= (1 << 2)  # XOR bit 3 (index 2)
                
                # Update state (maintain 5-bit width)
                self.q = next_state & 0x1F
        
        # Return current state as 5-bit binary string
        return {'q': format(self.q, '05b')}
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


