
import json
import random

def stimulus_gen():
    scenarios = [
        {
            'scenario': 'SelectInputA',
            'input variable': [
                {'sel': '0', 'a': '10101010', 'b': '11110000'}
            ]
        },
        {
            'scenario': 'SelectInputB',
            'input variable': [
                {'sel': '1', 'a': '10101010', 'b': '11110000'}
            ]
        },
        {
            'scenario': 'AllZeros',
            'input variable': [
                {'sel': '0', 'a': '00000000', 'b': '00000000'}
            ]
        },
        {
            'scenario': 'AllOnes',
            'input variable': [
                {'sel': '1', 'a': '11111111', 'b': '11111111'}
            ]
        },
        {
            'scenario': 'AlternatingPatterns',
            'input variable': [
                {'sel': '0', 'a': '10101010', 'b': '01010101'},
                {'sel': '1', 'a': '10101010', 'b': '01010101'}
            ]
        }
    ]
    
    # Add random test cases
    import random
    for i in range(15):
        a_val = format(random.randint(0, 255), '08b')
        b_val = format(random.randint(0, 255), '08b')
        sel_val = format(random.randint(0, 1), '01b')
        scenarios.append({
            'scenario': f'RandomTest_{i}',
            'input variable': [
                {'sel': sel_val, 'a': a_val, 'b': b_val}
            ]
        })
    
    return scenarios
if __name__ == "__main__":
    result = stimulus_gen()
    # Convert result to JSON string
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
