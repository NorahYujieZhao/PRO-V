import json
def _to_bit_str(value: int) -> str:
    return '1' if value else '0'

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            'scenario': 'HeatingModeTooCold',
            'vectors': [(1, 1, 0, 0)]
        },
        {
            'scenario': 'CoolingModeTooHot',
            'vectors': [(0, 0, 1, 0)]
        },
        {
            'scenario': 'ManualFanOnly',
            'vectors': [(0, 0, 0, 1)]
        },
        {
            'scenario': 'HeatingModeIgnoreHot',
            'vectors': [(1, 0, 1, 0)]
        },
        {
            'scenario': 'CoolingModeIgnoreCold',
            'vectors': [(0, 1, 0, 0)]
        },
        {
            'scenario': 'AllInputsActive',
            'vectors': [(1, 1, 1, 1)]
        },
        {
            'scenario': 'AllInputsInactive',
            'vectors': [(0, 0, 0, 0)]
        },
        {
            'scenario': 'FanOverride',
            'vectors': [(1, 1, 0, 1)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for mode, too_cold, too_hot, fan_on in sc['vectors']:
            inputs.append({
                'mode': _to_bit_str(mode),
                'too_cold': _to_bit_str(too_cold),
                'too_hot': _to_bit_str(too_hot),
                'fan_on': _to_bit_str(fan_on)
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
