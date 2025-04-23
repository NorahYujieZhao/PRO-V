
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        '''
        Initialize all internal state registers.
        Each internal register/state variable must align with the module header.
        Explicitly initialize these states according to the RTL specification.
        '''
        # This is combinational logic, no state registers needed
        pass
    
    def load(self, stimulus_dict: Dict[str, any]):
        '''
        Process inputs and generate outputs according to RTL specification
        '''
        stimulus_outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input strings to integers
            cpu_overheated = int(stimulus['cpu_overheated'])
            arrived = int(stimulus['arrived'])
            gas_tank_empty = int(stimulus['gas_tank_empty'])
            
            # Calculate shut_off_computer
            shut_off_computer = 1 if cpu_overheated else 0
            
            # Calculate keep_driving
            keep_driving = 0 if arrived else (0 if gas_tank_empty else 1)
            
            # Add outputs to result list
            output = {
                'shut_off_computer': str(shut_off_computer),
                'keep_driving': str(keep_driving)
            }
            stimulus_outputs.append(output)
        
        return {
            'scenario': stimulus_dict['scenario'],
            'output variable': stimulus_outputs
        }
def check_output(stimulus_list):

    dut = GoldenDUT()
    tb_outputs = []


    for stimulus in stimulus_list:

        tb_outputs.append(dut.load(stimulus))

    return tb_outputs

if __name__ == "__main__":

    with open("stimulus.json", "r") as f:
        stimulus_data = json.load(f)


    if isinstance(stimulus_data, dict):
        stimulus_list = stimulus_data.get("input variable", [])
    else:
        stimulus_list = stimulus_data



    outputs = check_output(stimulus_list)

    print(json.dumps(outputs, indent=2))

