import json
def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            'scenario': 'BasicPatternDetection',
            'vectors': [
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000000001'},
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000000010'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0000000100'}
            ]
        },
        {
            'scenario': 'PatternRestart',
            'vectors': [
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000000001'},
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000000010'},
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000000100'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0000000100'}
            ]
        },
        {
            'scenario': 'ShiftStateTransitions',
            'vectors': [
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0000010000'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0000100000'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0001000000'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0010000000'}
            ]
        },
        {
            'scenario': 'CountingStateBehavior',
            'vectors': [
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0100000000'},
                {'d': '0', 'done_counting': '1', 'ack': '0', 'state': '0100000000'}
            ]
        },
        {
            'scenario': 'WaitStateAcknowledge',
            'vectors': [
                {'d': '0', 'done_counting': '1', 'ack': '0', 'state': '1000000000'},
                {'d': '0', 'done_counting': '1', 'ack': '1', 'state': '1000000000'}
            ]
        },
        {
            'scenario': 'EarlyPatternAbort',
            'vectors': [
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000000001'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0000000010'}
            ]
        },
        {
            'scenario': 'MultiplePatternAttempts',
            'vectors': [
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000000001'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0000000010'},
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000000001'},
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000000010'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0000000100'}
            ]
        },
        {
            'scenario': 'CompleteFlowVerification',
            'vectors': [
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000000001'},
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000000010'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0000000100'},
                {'d': '1', 'done_counting': '0', 'ack': '0', 'state': '0000001000'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0000010000'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0000100000'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0001000000'},
                {'d': '0', 'done_counting': '0', 'ack': '0', 'state': '0010000000'},
                {'d': '0', 'done_counting': '1', 'ack': '0', 'state': '0100000000'},
                {'d': '0', 'done_counting': '1', 'ack': '1', 'state': '1000000000'}
            ]
        }
    ]
    
    stimulus_list = []
    for sc in scenarios:
        stimulus_list.append({
            'scenario': sc['scenario'],
            'input variable': sc['vectors']
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
