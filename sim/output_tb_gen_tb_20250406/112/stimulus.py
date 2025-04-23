import json

def _to_hex_bit_str(value: int, width: int = 16) -> str:
    return format(value, f'0{width}b')

def _get_default_inputs():
    return {
        'a': _to_hex_bit_str(0),
        'b': _to_hex_bit_str(0),
        'c': _to_hex_bit_str(0),
        'd': _to_hex_bit_str(0),
        'e': _to_hex_bit_str(0),
        'f': _to_hex_bit_str(0),
        'g': _to_hex_bit_str(0),
        'h': _to_hex_bit_str(0),
        'i': _to_hex_bit_str(0),
        'sel': format(0, '04b')
    }

def stimulus_gen():
    stimulus_list = []
    
    # SelectInputA scenario
    inputs = _get_default_inputs()
    inputs['a'] = _to_hex_bit_str(0xAAAA)
    inputs['sel'] = format(0, '04b')
    stimulus_list.append({
        'scenario': 'SelectInputA',
        'input variable': [inputs]
    })
    
    # SelectInputI scenario
    inputs = _get_default_inputs()
    inputs['i'] = _to_hex_bit_str(0x5555)
    inputs['sel'] = format(8, '04b')
    stimulus_list.append({
        'scenario': 'SelectInputI',
        'input variable': [inputs]
    })
    
    # AllZeroInputs scenario
    vectors = []
    for sel in range(9):
        inputs = _get_default_inputs()
        inputs['sel'] = format(sel, '04b')
        vectors.append(inputs)
    stimulus_list.append({
        'scenario': 'AllZeroInputs',
        'input variable': vectors
    })
    
    # AllOnesInputs scenario
    vectors = []
    for sel in range(9):
        inputs = _get_default_inputs()
        for key in inputs:
            if key != 'sel':
                inputs[key] = _to_hex_bit_str(0xFFFF)
        inputs['sel'] = format(sel, '04b')
        vectors.append(inputs)
    stimulus_list.append({
        'scenario': 'AllOnesInputs',
        'input variable': vectors
    })
    
    # UnusedSelector9 scenario
    inputs = _get_default_inputs()
    inputs['sel'] = format(9, '04b')
    stimulus_list.append({
        'scenario': 'UnusedSelector9',
        'input variable': [inputs]
    })
    
    # UnusedSelector15 scenario
    inputs = _get_default_inputs()
    inputs['sel'] = format(15, '04b')
    stimulus_list.append({
        'scenario': 'UnusedSelector15',
        'input variable': [inputs]
    })
    
    # AlternatingPatterns scenario
    vectors = []
    for sel in range(9):
        inputs = _get_default_inputs()
        inputs['a'] = _to_hex_bit_str(0xAAAA)
        inputs['b'] = _to_hex_bit_str(0x5555)
        inputs['c'] = _to_hex_bit_str(0xAAAA)
        inputs['d'] = _to_hex_bit_str(0x5555)
        inputs['e'] = _to_hex_bit_str(0xAAAA)
        inputs['f'] = _to_hex_bit_str(0x5555)
        inputs['g'] = _to_hex_bit_str(0xAAAA)
        inputs['h'] = _to_hex_bit_str(0x5555)
        inputs['i'] = _to_hex_bit_str(0xAAAA)
        inputs['sel'] = format(sel, '04b')
        vectors.append(inputs)
    stimulus_list.append({
        'scenario': 'AlternatingPatterns',
        'input variable': vectors
    })
    
    # UniquePatterns scenario
    vectors = []
    for sel in range(9):
        inputs = _get_default_inputs()
        inputs['a'] = _to_hex_bit_str(0x1111)
        inputs['b'] = _to_hex_bit_str(0x2222)
        inputs['c'] = _to_hex_bit_str(0x3333)
        inputs['d'] = _to_hex_bit_str(0x4444)
        inputs['e'] = _to_hex_bit_str(0x5555)
        inputs['f'] = _to_hex_bit_str(0x6666)
        inputs['g'] = _to_hex_bit_str(0x7777)
        inputs['h'] = _to_hex_bit_str(0x8888)
        inputs['i'] = _to_hex_bit_str(0x9999)
        inputs['sel'] = format(sel, '04b')
        vectors.append(inputs)
    stimulus_list.append({
        'scenario': 'UniquePatterns',
        'input variable': vectors
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
