
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize the 5-bit LFSR register
        '''
        self.q = 0  # 5-bit LFSR state

    def load(self, clk: int, stimulus_dict: Dict[str, str]):
        '''
        Update LFSR state on rising clock edge
        '''
        # Convert input signals from binary strings
        reset = int(stimulus_dict['reset'], 2)

        if clk == 1:  # Rising edge
            if reset == 1:
                # Synchronous reset to 1
                self.q = 1
            else:
                # LFSR feedback logic
                feedback = self.q & 1  # LSB (output bit)
                # Shift right and apply feedback to tap positions (5 and 3)
                next_q = self.q >> 1
                if feedback:
                    # XOR with feedback at tap positions
                    next_q ^= (1 << 4)  # Bit 5
                    next_q ^= (1 << 2)  # Bit 3
                # Apply 5-bit mask
                self.q = next_q & 0x1F

        # Return current LFSR value as 5-bit binary string
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


