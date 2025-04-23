import json
def _to_bit_str(value: int) -> str:
    return format(value, '01b')

def _generate_alternating_pattern(length: int) -> list:
    return [{'in': _to_bit_str(i % 2)} for i in range(length)]

def _generate_random_pattern(length: int) -> list:
    import random
    return [{'in': _to_bit_str(random.randint(0, 1))} for _ in range(length)]

def stimulus_gen() -> list[dict]:
    stimulus_list = [
        {
            "scenario": "InputLowStable",
            "input variable": [{'in': '0'} for _ in range(5)]
        },
        {
            "scenario": "InputHighStable",
            "input variable": [{'in': '1'} for _ in range(5)]
        },
        {
            "scenario": "LowToHighTransition",
            "input variable": [{'in': '0'}, {'in': '1'}]
        },
        {
            "scenario": "HighToLowTransition",
            "input variable": [{'in': '1'}, {'in': '0'}]
        },
        {
            "scenario": "AlternatingPattern",
            "input variable": _generate_alternating_pattern(8)
        },
        {
            "scenario": "FastToggling",
            "input variable": _generate_alternating_pattern(16)
        },
        {
            "scenario": "SlowToggling",
            "input variable": [{'in': v} for v in ['0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1']]
        },
        {
            "scenario": "RandomPattern",
            "input variable": _generate_random_pattern(10)
        }
    ]
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
