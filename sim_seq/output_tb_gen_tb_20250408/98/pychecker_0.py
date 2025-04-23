
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # Define states as constants
        self.STATE_A = 0  # Reset state
        self.STATE_B = 1  # f=1 state
        self.STATE_C = 2  # Monitor x sequence
        self.STATE_D = 3  # g=1, monitor y
        self.STATE_E = 4  # g=1 permanent
        self.STATE_F = 5  # g=0 permanent
        
        # Initialize state variables
        self.current_state = self.STATE_A
        self.x_history = [0, 0, 0]  # Store last 3 x values
        self.y_count = 0  # Counter for y monitoring
        
    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        # Convert inputs from binary strings
        resetn = int(stimulus_dict['resetn'], 2)
        x = int(stimulus_dict['x'], 2)
        y = int(stimulus_dict['y'], 2)
        
        # Output signals
        f = '0'
        g = '0'
        
        if clk == 1:  # Rising edge
            if resetn == 0:  # Synchronous reset
                self.current_state = self.STATE_A
                self.x_history = [0, 0, 0]
                self.y_count = 0
            else:
                # State machine transitions
                if self.current_state == self.STATE_A:
                    self.current_state = self.STATE_B
                
                elif self.current_state == self.STATE_B:
                    self.current_state = self.STATE_C
                    
                elif self.current_state == self.STATE_C:
                    # Update x history
                    self.x_history = [self.x_history[1], self.x_history[2], x]
                    # Check for sequence 1,0,1
                    if self.x_history == [1, 0, 1]:
                        self.current_state = self.STATE_D
                        
                elif self.current_state == self.STATE_D:
                    if y == 1:
                        self.current_state = self.STATE_E
                    else:
                        self.y_count += 1
                        if self.y_count >= 2:
                            self.current_state = self.STATE_F
                            
                # STATE_E and STATE_F are terminal states until reset
        
        # Set outputs based on current state
        if self.current_state == self.STATE_B:
            f = '1'
        if self.current_state in [self.STATE_D, self.STATE_E]:
            g = '1'
            
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


