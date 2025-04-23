import json
def create_input_vector(pattern_type, sel_value=0):
    if pattern_type == 'single_bit':
        return format(1 << sel_value, '0256b')
    elif pattern_type == 'alternating':
        return ''.join(['1' if i % 2 == 0 else '0' for i in range(256)])
    elif pattern_type == 'all_ones':
        return '1' * 256
    elif pattern_type == 'all_zeros':
        return '0' * 256
    elif pattern_type == 'one_hot':
        return format(1 << sel_value, '0256b')

def format_sel(value):
    return format(value, '08b')

def stimulus_gen():
    scenarios = [
        {
            'scenario': 'SelectFirstBit',
            'input variable': [{'in': create_input_vector('single_bit', 0),
                              'sel': format_sel(0)}]
        },
        {
            'scenario': 'SelectLastBit',
            'input variable': [{'in': create_input_vector('single_bit', 255),
                              'sel': format_sel(255)}]
        },
        {
            'scenario': 'SelectMiddleBit',
            'input variable': [{'in': create_input_vector('single_bit', 128),
                              'sel': format_sel(128)}]
        },
        {
            'scenario': 'AlternatingInputPattern',
            'input variable': [{'in': create_input_vector('alternating'),
                              'sel': format_sel(i)} for i in [0, 1, 2, 3, 254, 255]]
        },
        {
            'scenario': 'AllOnesInput',
            'input variable': [{'in': create_input_vector('all_ones'),
                              'sel': format_sel(i)} for i in [0, 127, 255]]
        },
        {
            'scenario': 'AllZerosInput',
            'input variable': [{'in': create_input_vector('all_zeros'),
                              'sel': format_sel(i)} for i in [0, 127, 255]]
        },
        {
            'scenario': 'OneHotInput',
            'input variable': [{'in': create_input_vector('one_hot', i),
                              'sel': format_sel(i)} for i in [1, 128, 254]]
        },
        {
            'scenario': 'BoundaryTransition',
            'input variable': [{'in': create_input_vector('single_bit', i),
                              'sel': format_sel(i)} for i in [0, 1, 254, 255]]
        }
    ]
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
