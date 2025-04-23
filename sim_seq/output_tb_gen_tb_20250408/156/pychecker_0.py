
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers
        '''
        self.q = 0  # 16-bit counter (4 BCD digits)
        self.ena = [0] * 3  # Enable signals for digits [3:1]

    def load(self, clk, stimulus_dict: Dict[str, str]):
        '''
        Update counter state on clock edge
        '''
        # Convert reset input to integer
        reset = int(stimulus_dict['reset'], 2)

        if clk == 1:  # Rising edge
            if reset:
                self.q = 0
                self.ena = [0] * 3
            else:
                # Extract current digits
                d0 = (self.q >> 0) & 0xF
                d1 = (self.q >> 4) & 0xF
                d2 = (self.q >> 8) & 0xF
                d3 = (self.q >> 12) & 0xF

                # Calculate enable signals
                self.ena[0] = 1 if d0 == 9 else 0
                self.ena[1] = 1 if d0 == 9 and d1 == 9 else 0
                self.ena[2] = 1 if d0 == 9 and d1 == 9 and d2 == 9 else 0

                # Increment digits
                d0 = (d0 + 1) % 10
                if d0 == 0:
                    d1 = (d1 + 1) % 10
                    if d1 == 0:
                        d2 = (d2 + 1) % 10
                        if d2 == 0:
                            d3 = (d3 + 1) % 10

                # Combine digits back into counter
                self.q = (d3 << 12) | (d2 << 8) | (d1 << 4) | d0

        # Format outputs as binary strings
        ena_str = ''.join(str(x) for x in reversed(self.ena))
        return {
            'ena': ena_str,
            'q': format(self.q, '016b')
        }
def check_output(stimulus_list_scenario):

    dut = GoldenDUT()
    tb_outputs = []


    for stimulus_list in stimulus_list_scenario["input variable"]:


        clock_cycles = stimulus_list['clock cycles']
        
        input_vars_list = {k: v for k, v in stimulus_list.items() if k != "clock cycles"}
        output_vars_list = {'clock cycles':clock_cycles}
        for k,v in input_vars_list.items():
            if len(v) < clock_cycles:
                v.extend([v[-1]] * (clock_cycles - len(v)))
                
        

        for i in range(clock_cycles):
            input_vars = {k:v[i] for k,v in input_vars_list.items()}
            
            clk= 0
            output_vars = dut.load(clk,input_vars)
            clk = 1
            output_vars = dut.load(clk,input_vars)
            for k,v in output_vars.items():
                if k not in output_vars_list:
                    output_vars_list[k] = []
                output_vars_list[k].append(v)
            


        tb_outputs.append(output_vars_list)

    return tb_outputs

if __name__ == "__main__":
    stimulus_file_name = "stimulus.json"
    with open(stimulus_file_name, "r") as f:
        stimulus_data = json.load(f)


    if isinstance(stimulus_data, dict):
        stimulus_list_scenarios = stimulus_data.get("input variable", [])
    else:
        stimulus_list_scenarios = stimulus_data

    outputs=[]
    for stimulus_list_scenario in stimulus_list_scenarios:
        outputs.append( check_output(stimulus_list_scenario))
    with open(stimulus_file_name, "w") as f:
        json.dump(stimulus_list_scenarios, f, indent=4)

    print(json.dumps(outputs, indent=2))



