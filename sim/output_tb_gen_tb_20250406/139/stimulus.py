import json
def stimulus_gen() -> list[dict]:
    # Define scenarios with their input vectors
    scenarios = [
        {
            'scenario': 'AllZeroInputs',
            'vectors': [(0, 0, 0)]
        },
        {
            'scenario': 'AllOneInputs',
            'vectors': [(1, 1, 1)]
        },
        {
            'scenario': 'XNORSameInputs',
            'vectors': [(0, 0, 1)]
        },
        {
            'scenario': 'XNORDifferentInputs',
            'vectors': [(0, 1, 0)]
        },
        {
            'scenario': 'AlternatingPattern1',
            'vectors': [(1, 0, 1)]
        },
        {
            'scenario': 'AlternatingPattern2',
            'vectors': [(0, 1, 1)]
        },
        {
            'scenario': 'XNOROneXORZero',
            'vectors': [(1, 1, 0)]
        },
        {
            'scenario': 'XNORZeroXOROne',
            'vectors': [(1, 0, 0)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for in1_val, in2_val, in3_val in sc['vectors']:
            inputs.append({
                'in1': format(in1_val, '1b'),
                'in2': format(in2_val, '1b'),
                'in3': format(in3_val, '1b')
            })
        
        stimulus_list.append({
            'scenario': sc['scenario'],
            'input variable': inputs
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
