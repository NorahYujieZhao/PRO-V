
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize internal state registers
        '''
        self.prev_sensors = 0  # Previous sensor state
        self.fr1 = 0
        self.fr2 = 0
        self.fr3 = 0
        self.dfr = 0

    def load(self, clk: int, stimulus_dict: Dict[str, str]) -> Dict[str, str]:
        if clk == 1:  # Only update on rising edge
            # Convert inputs from binary strings to integers
            reset = int(stimulus_dict['reset'], 2)
            sensors = int(stimulus_dict['s'], 2)

            if reset == 1:
                # Reset state - equivalent to low water for long time
                self.fr1 = 1
                self.fr2 = 1
                self.fr3 = 1
                self.dfr = 1
                self.prev_sensors = 0
            else:
                # Determine flow rates based on sensor readings
                if sensors == 7:  # All sensors on (s[3],s[2],s[1] = 1)
                    self.fr1 = 0
                    self.fr2 = 0
                    self.fr3 = 0
                elif sensors >= 3:  # s[2],s[1] = 1, s[3] = 0
                    self.fr1 = 1
                    self.fr2 = 0
                    self.fr3 = 0
                elif sensors >= 1:  # s[1] = 1, s[3],s[2] = 0
                    self.fr1 = 1
                    self.fr2 = 1
                    self.fr3 = 0
                else:  # No sensors on
                    self.fr1 = 1
                    self.fr2 = 1
                    self.fr3 = 1

                # Set dfr if water level increased
                if sensors > self.prev_sensors:
                    self.dfr = 1
                else:
                    self.dfr = 0

                self.prev_sensors = sensors

        # Convert outputs to binary strings
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


