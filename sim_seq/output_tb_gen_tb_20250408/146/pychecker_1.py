
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''Initialize state registers'''
        self.prev_level = 0  # Previous water level (0=lowest)
        self.fr1 = 0
        self.fr2 = 0
        self.fr3 = 0
        self.dfr = 0

    def _get_level(self, sensors):
        '''Convert sensor readings to water level'''
        if sensors & 0b100:  # s[3] is high
            return 3
        elif sensors & 0b010:  # s[2] is high
            return 2
        elif sensors & 0b001:  # s[1] is high
            return 1
        return 0

    def load(self, clk, stimulus_dict):
        '''Update state and compute outputs'''
        if clk == 1:  # Only update on clock edge
            # Convert inputs
            reset = int(stimulus_dict['reset'], 2)
            sensors = int(stimulus_dict['s'], 2)
            
            if reset:
                # Reset to low water state
                self.prev_level = 0
                self.fr1 = 1
                self.fr2 = 1
                self.fr3 = 1
                self.dfr = 1
            else:
                # Get current water level
                curr_level = self._get_level(sensors)
                
                # Set flow rate outputs based on current level
                if curr_level == 3:  # Above s[3]
                    self.fr1 = 0
                    self.fr2 = 0
                    self.fr3 = 0
                elif curr_level == 2:  # Between s[3] and s[2]
                    self.fr1 = 1
                    self.fr2 = 0
                    self.fr3 = 0
                elif curr_level == 1:  # Between s[2] and s[1]
                    self.fr1 = 1
                    self.fr2 = 1
                    self.fr3 = 0
                else:  # Below s[1]
                    self.fr1 = 1
                    self.fr2 = 1
                    self.fr3 = 1
                
                # Set dfr based on level change
                self.dfr = 1 if curr_level < self.prev_level else 0
                self.prev_level = curr_level

        # Return outputs as binary strings
        return {
            'fr3': format(self.fr3, 'b'),
            'fr2': format(self.fr2, 'b'),
            'fr1': format(self.fr1, 'b'),
            'dfr': format(self.dfr, 'b')
        }
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


