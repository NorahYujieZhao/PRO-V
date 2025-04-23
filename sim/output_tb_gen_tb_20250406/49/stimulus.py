import json
def _generate_bit_string(length: int, pattern: str) -> str:
    if pattern == 'all_zeros':
        return '0' * length
    elif pattern == 'all_ones':
        return '1' * length
    elif pattern == 'alternating':
        return ''.join(['1' if i % 2 == 0 else '0' for i in range(length)])
    elif pattern == 'sparse':
        return ''.join(['1' if i % 8 == 0 else '0' for i in range(length)])

def stimulus_gen() -> list[dict]:
    width = 255
    stimulus_list = []
    
    # AllZeros scenario
    stimulus_list.append({
        'scenario': 'AllZeros',
        'input variable': [{'in': _generate_bit_string(width, 'all_zeros')}]
    })
    
    # AllOnes scenario
    stimulus_list.append({
        'scenario': 'AllOnes',
        'input variable': [{'in': _generate_bit_string(width, 'all_ones')}]
    })
    
    # AlternatingBits scenario
    stimulus_list.append({
        'scenario': 'AlternatingBits',
        'input variable': [{'in': _generate_bit_string(width, 'alternating')}]
    })
    
    # SingleOneAtMSB scenario
    msb_pattern = '1' + '0' * (width-1)
    stimulus_list.append({
        'scenario': 'SingleOneAtMSB',
        'input variable': [{'in': msb_pattern}]
    })
    
    # SingleOneAtLSB scenario
    lsb_pattern = '0' * (width-1) + '1'
    stimulus_list.append({
        'scenario': 'SingleOneAtLSB',
        'input variable': [{'in': lsb_pattern}]
    })
    
    # OnesInLowerHalf scenario
    lower_half = '0' * 128 + '1' * 127
    stimulus_list.append({
        'scenario': 'OnesInLowerHalf',
        'input variable': [{'in': lower_half}]
    })
    
    # OnesInUpperHalf scenario
    upper_half = '1' * 128 + '0' * 127
    stimulus_list.append({
        'scenario': 'OnesInUpperHalf',
        'input variable': [{'in': upper_half}]
    })
    
    # SparseOnes scenario
    stimulus_list.append({
        'scenario': 'SparseOnes',
        'input variable': [{'in': _generate_bit_string(width, 'sparse')}]
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
