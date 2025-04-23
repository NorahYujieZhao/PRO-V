import json

def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            'scenario': 'StateATransitions',
            'vectors': [
                {'in': 0, 'state': 0b0001},  # Stay in A
                {'in': 1, 'state': 0b0001}   # Go to B
            ]
        },
        {
            'scenario': 'StateBTransitions',
            'vectors': [
                {'in': 0, 'state': 0b0010},  # Go to C
                {'in': 1, 'state': 0b0010}   # Stay in B
            ]
        },
        {
            'scenario': 'StateCTransitions',
            'vectors': [
                {'in': 0, 'state': 0b0100},  # Go to A
                {'in': 1, 'state': 0b0100}   # Go to D
            ]
        },
        {
            'scenario': 'StateDTransitions',
            'vectors': [
                {'in': 0, 'state': 0b1000},  # Go to C
                {'in': 1, 'state': 0b1000}   # Go to B
            ]
        },
        {
            'scenario': 'AllZeroState',
            'vectors': [
                {'in': 0, 'state': 0b0000},
                {'in': 1, 'state': 0b0000}
            ]
        },
        {
            'scenario': 'MultipleHotBits',
            'vectors': [
                {'in': 0, 'state': 0b0011},
                {'in': 1, 'state': 0b0101},
                {'in': 0, 'state': 0b0110},
                {'in': 1, 'state': 0b1001},
                {'in': 0, 'state': 0b1010},
                {'in': 1, 'state': 0b1100}
            ]
        },
        {
            'scenario': 'AlternatingInputs',
            'vectors': [
                {'in': 0, 'state': 0b0001},
                {'in': 1, 'state': 0b0010},
                {'in': 0, 'state': 0b0100},
                {'in': 1, 'state': 0b1000}
            ]
        },
        {
            'scenario': 'AllOnesState',
            'vectors': [
                {'in': 0, 'state': 0b1111},
                {'in': 1, 'state': 0b1111}
            ]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for vec in sc['vectors']:
            inputs.append({
                'in': _to_bit_str(vec['in']),
                'state': _to_bit_str(vec['state'], width=4)
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
