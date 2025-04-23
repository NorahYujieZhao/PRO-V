import json
def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    # Define mapping of input to expected output (from waveform)
    input_output_map = {
        0: 0x1232,
        1: 0xaee0,
        2: 0x27d4,
        3: 0x5a0e,
        4: 0x2066,
        5: 0x64ce,
        6: 0xc526,
        7: 0x2f19
    }
    
    scenarios = [
        {
            "scenario": "AllZeroInput",
            "vectors": [0]
        },
        {
            "scenario": "AllOneInput",
            "vectors": [7]
        },
        {
            "scenario": "AlternatingBits",
            "vectors": [5]  # 101
        },
        {
            "scenario": "SequentialIncrement",
            "vectors": [0, 1, 2, 3, 4, 5, 6, 7]
        },
        {
            "scenario": "SequentialDecrement",
            "vectors": [7, 6, 5, 4, 3, 2, 1, 0]
        },
        {
            "scenario": "RandomTransitions",
            "vectors": [2, 5, 1, 6, 3]
        },
        {
            "scenario": "RepeatedValues",
            "vectors": [4, 4, 4]
        },
        {
            "scenario": "GrayCodeTransitions",
            "vectors": [0, 1, 3, 2, 6, 7, 5, 4]
        }
    ]
    
    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for a_val in sc["vectors"]:
            inputs.append({
                "a": _to_bit_str(a_val, width=3)
            })
        
        stimulus_list.append({
            "scenario": sc["scenario"],
            "input variable": inputs
        })
    
    return stimulus_list
if __name__ == "__main__":
    result = stimulus_gen()
    # Convert result to JSON string
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
