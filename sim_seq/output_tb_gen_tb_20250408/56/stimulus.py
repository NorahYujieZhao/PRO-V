import json
def stimulus_gen():
    scenarios = []
    
    # Rising Edge Data Capture
    scenarios.append({
        'scenario': 'RisingEdgeDataCapture',
        'input variable': [{
            'clock cycles': 4,
            'd': ['0', '1', '1', '0']  # Data changes before rising edges
        }]
    })
    
    # Falling Edge Data Capture
    scenarios.append({
        'scenario': 'FallingEdgeDataCapture',
        'input variable': [{
            'clock cycles': 4,
            'd': ['0', '1', '0', '1']  # Data changes before falling edges
        }]
    })
    
    # Rapid Input Changes
    scenarios.append({
        'scenario': 'RapidInputChanges',
        'input variable': [{
            'clock cycles': 8,
            'd': ['0', '1', '0', '1', '0', '1', '0', '1']  # Rapid toggles
        }]
    })
    
    # Clock Edge Setup Time
    scenarios.append({
        'scenario': 'ClockEdgeSetupTime',
        'input variable': [{
            'clock cycles': 6,
            'd': ['0', '1', '1', '0', '0', '1']  # Data stable before edges
        }]
    })
    
    # Clock Edge Hold Time
    scenarios.append({
        'scenario': 'ClockEdgeHoldTime',
        'input variable': [{
            'clock cycles': 6,
            'd': ['0', '0', '1', '1', '0', '0']  # Data held after edges
        }]
    })
    
    # Alternating Edge Capture
    scenarios.append({
        'scenario': 'AlternatingEdgeCapture',
        'input variable': [{
            'clock cycles': 8,
            'd': ['0', '1', '0', '1', '1', '0', '1', '0']  # Alternating patterns
        }]
    })
    
    # High Frequency Operation
    scenarios.append({
        'scenario': 'HighFrequencyOperation',
        'input variable': [{
            'clock cycles': 10,
            'd': ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1']  # Maximum toggle rate
        }]
    })
    
    # Initial Power Up State
    scenarios.append({
        'scenario': 'InitialPowerUpState',
        'input variable': [{
            'clock cycles': 4,
            'd': ['0', '0', '0', '0']  # Initial state verification
        }]
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
