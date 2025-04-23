import json

def gen_pattern_with_delay(delay_bits):
    # Generate 1101 pattern followed by delay bits
    return ['1', '1', '0', '1'] + [bit for bit in delay_bits]

def stimulus_gen():
    scenarios = []
    
    # Basic Pattern Detection
    scenarios.append({
        'scenario': 'BasicPatternDetection',
        'input variable': [{
            'clock cycles': 8,
            'data': ['1', '1', '0', '1', '0', '0', '0', '0'],
            'reset': ['0'] * 8,
            'ack': ['0'] * 8
        }, {
            'clock cycles': 1000,
            'data': ['0'] * 1000,
            'reset': ['0'] * 1000,
            'ack': ['0'] * 1000
        }]
    })

    # Maximum Delay Count
    scenarios.append({
        'scenario': 'MaximumDelayCount',
        'input variable': [{
            'clock cycles': 8,
            'data': ['1', '1', '0', '1', '1', '1', '1', '1'],
            'reset': ['0'] * 8,
            'ack': ['0'] * 8
        }, {
            'clock cycles': 16000,
            'data': ['0'] * 16000,
            'reset': ['0'] * 16000,
            'ack': ['0'] * 16000
        }]
    })

    # Partial Pattern Reset
    scenarios.append({
        'scenario': 'PartialPatternReset',
        'input variable': [{
            'clock cycles': 3,
            'data': ['1', '1', '0'],
            'reset': ['0', '0', '1'],
            'ack': ['0'] * 3
        }, {
            'clock cycles': 8,
            'data': ['1', '1', '0', '1', '0', '0', '0', '0'],
            'reset': ['0'] * 8,
            'ack': ['0'] * 8
        }]
    })

    # Multiple Pattern Occurrences
    scenarios.append({
        'scenario': 'MultiplePatternOccurrences',
        'input variable': [{
            'clock cycles': 12,
            'data': ['1', '1', '0', '1', '0', '0', '1', '1', '0', '1', '0', '0'],
            'reset': ['0'] * 12,
            'ack': ['0'] * 12
        }, {
            'clock cycles': 1000,
            'data': ['0'] * 1000,
            'reset': ['0'] * 1000,
            'ack': ['0'] * 1000
        }]
    })

    # Count Output Verification
    scenarios.append({
        'scenario': 'CountOutputVerification',
        'input variable': [{
            'clock cycles': 8,
            'data': ['1', '1', '0', '1', '0', '0', '1', '1'],
            'reset': ['0'] * 8,
            'ack': ['0'] * 8
        }, {
            'clock cycles': 4000,
            'data': ['0'] * 4000,
            'reset': ['0'] * 4000,
            'ack': ['0'] * 4000
        }]
    })

    # Acknowledgment Handling
    scenarios.append({
        'scenario': 'AcknowledgmentHandling',
        'input variable': [{
            'clock cycles': 8,
            'data': ['1', '1', '0', '1', '0', '0', '0', '0'],
            'reset': ['0'] * 8,
            'ack': ['0'] * 8
        }, {
            'clock cycles': 1000,
            'data': ['0'] * 1000,
            'reset': ['0'] * 1000,
            'ack': ['0'] * 999 + ['1']
        }]
    })

    # Post Acknowledgment Behavior
    scenarios.append({
        'scenario': 'PostAcknowledgmentBehavior',
        'input variable': [{
            'clock cycles': 8,
            'data': ['1', '1', '0', '1', '0', '0', '0', '0'],
            'reset': ['0'] * 8,
            'ack': ['0'] * 8
        }, {
            'clock cycles': 1000,
            'data': ['0'] * 1000,
            'reset': ['0'] * 1000,
            'ack': ['0'] * 999 + ['1']
        }, {
            'clock cycles': 8,
            'data': ['1', '1', '0', '1', '0', '0', '0', '1'],
            'reset': ['0'] * 8,
            'ack': ['0'] * 8
        }]
    })

    # Input During Counting
    scenarios.append({
        'scenario': 'InputDuringCounting',
        'input variable': [{
            'clock cycles': 8,
            'data': ['1', '1', '0', '1', '0', '0', '0', '0'],
            'reset': ['0'] * 8,
            'ack': ['0'] * 8
        }, {
            'clock cycles': 1000,
            'data': ['1', '1', '0', '1'] + ['0'] * 996,
            'reset': ['0'] * 1000,
            'ack': ['0'] * 1000
        }]
    })

    # Reset During Counting
    scenarios.append({
        'scenario': 'ResetDuringCounting',
        'input variable': [{
            'clock cycles': 8,
            'data': ['1', '1', '0', '1', '0', '0', '0', '0'],
            'reset': ['0'] * 8,
            'ack': ['0'] * 8
        }, {
            'clock cycles': 500,
            'data': ['0'] * 500,
            'reset': ['0'] * 499 + ['1'],
            'ack': ['0'] * 500
        }]
    })

    # Reset During Done State
    scenarios.append({
        'scenario': 'ResetDuringDoneState',
        'input variable': [{
            'clock cycles': 8,
            'data': ['1', '1', '0', '1', '0', '0', '0', '0'],
            'reset': ['0'] * 8,
            'ack': ['0'] * 8
        }, {
            'clock cycles': 1000,
            'data': ['0'] * 1000,
            'reset': ['0'] * 999 + ['1'],
            'ack': ['0'] * 1000
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
