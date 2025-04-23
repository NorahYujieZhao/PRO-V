
import json
from typing import Dict, List, Union


class GoldenDUT:
    def __init__(self):
        # No state registers needed for combinational circuit
        # Create lookup table mapping 3-bit input to 16-bit output
        self.lut = {
            0: 0x1232,
            1: 0xaee0,
            2: 0x27d4,
            3: 0x5a0e,
            4: 0x2066,
            5: 0x64ce,
            6: 0xc526,
            7: 0x2f19
        }

    def load(self, stimulus_dict: Dict[str, any]):
        stimulus_outputs = []
        
        for stimulus in stimulus_dict['input variable']:
            # Convert input 'a' from binary string to integer
            a = int(stimulus['a'], 2)
            
            # Look up corresponding output value
            q = self.lut[a]
            
            # Format as 16-bit binary string
            q_bin = format(q, '016b')
            
            # Add to outputs
            stimulus_outputs.append({"q": q_bin})

        return {
            "scenario": stimulus_dict['scenario'],
            "output variable": stimulus_outputs
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

