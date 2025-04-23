import json
def stimulus_gen():
    scenarios = [
        {
            'scenario': 'AllZeros',
            'input variable': [{'in': '000'}]
        },
        {
            'scenario': 'Single1_Position0',
            'input variable': [{'in': '001'}]
        },
        {
            'scenario': 'Single1_Position1',
            'input variable': [{'in': '010'}]
        },
        {
            'scenario': 'Single1_Position2',
            'input variable': [{'in': '100'}]
        },
        {
            'scenario': 'Double1s_Position01',
            'input variable': [{'in': '011'}]
        },
        {
            'scenario': 'Double1s_Position12',
            'input variable': [{'in': '110'}]
        },
        {
            'scenario': 'Double1s_Position02',
            'input variable': [{'in': '101'}]
        },
        {
            'scenario': 'AllOnes',
            'input variable': [{'in': '111'}]
        }
    ]
    
    # Add 10 random test cases
    import random
    for i in range(10):
        random_input = format(random.randint(0, 7), '03b')
        scenarios.append({
            'scenario': f'RandomTest_{i}',
            'input variable': [{'in': random_input}]
        })
    
    return scenarios
if __name__ == "__main__":
    result = stimulus_gen()
    # 将结果转换为 JSON 字符串
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
