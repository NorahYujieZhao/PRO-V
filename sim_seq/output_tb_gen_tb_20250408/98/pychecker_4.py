
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # State encoding
        self.STATE_A = 0  # Reset state
        self.STATE_B = 1  # f=1 state
        self.STATE_C = 2  # Monitor x pattern
        self.STATE_D = 3  # Monitor y with g=1
        self.STATE_E = 4  # Permanent g=1
        self.STATE_F = 5  # Permanent g=0
        
        # Initialize state registers
        self.current_state = self.STATE_A
        self.x_history = [0, 0, 0]  # Store last 3 x values
        self.y_counter = 0  # Counter for y monitoring
    
    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        if clk == 1:  # Process on rising edge
            # Convert inputs from binary strings to integers
            resetn = int(stimulus_dict['resetn'], 2)
            x = int(stimulus_dict['x'], 2)
            y = int(stimulus_dict['y'], 2)
            
            # Next state logic
            next_state = self.current_state
            
            if resetn == 0:
                next_state = self.STATE_A
            else:
                if self.current_state == self.STATE_A:
                    next_state = self.STATE_B
                elif self.current_state == self.STATE_B:
                    next_state = self.STATE_C
                elif self.current_state == self.STATE_C:
                    # Update x history
                    self.x_history = self.x_history[1:] + [x]
                    # Check for pattern 1,0,1
                    if self.x_history == [1, 0, 1]:
                        next_state = self.STATE_D
                elif self.current_state == self.STATE_D:
                    if y == 1:
                        next_state = self.STATE_E
                    else:
                        self.y_counter += 1
                        if self.y_counter >= 2:
                            next_state = self.STATE_F
            
            # Update state
            self.current_state = next_state
            
            # Reset counters if state changes
            if self.current_state != next_state:
                self.y_counter = 0
                self.x_history = [0, 0, 0]
        
        # Output logic
        f = '1' if self.current_state == self.STATE_B else '0'
        g = '1' if self.current_state in [self.STATE_D, self.STATE_E] else '0'
        
        return {'f': f, 'g': g}
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


