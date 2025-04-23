import json
def stimulus_gen():
    scenarios = [
        {
            'scenario': 'InitialState',
            'input variable': [
                {'in': '0', 'state': '0000000001', 'areset': '0'}
            ]
        },
        {
            'scenario': 'PathToS7_Output01',
            'input variable': [
                {'in': '1', 'state': '0000000001', 'areset': '0'},  # S0->S1
                {'in': '1', 'state': '0000000010', 'areset': '0'},  # S1->S2
                {'in': '1', 'state': '0000000100', 'areset': '0'},  # S2->S3
                {'in': '1', 'state': '0000001000', 'areset': '0'},  # S3->S4
                {'in': '1', 'state': '0000010000', 'areset': '0'},  # S4->S5
                {'in': '1', 'state': '0000100000', 'areset': '0'},  # S5->S6
                {'in': '1', 'state': '0001000000', 'areset': '0'}   # S6->S7
            ]
        },
        {
            'scenario': 'PathToS8_Output10',
            'input variable': [
                {'in': '1', 'state': '0000000001', 'areset': '0'},  # S0->S1
                {'in': '1', 'state': '0000000010', 'areset': '0'},  # S1->S2
                {'in': '1', 'state': '0000000100', 'areset': '0'},  # S2->S3
                {'in': '1', 'state': '0000001000', 'areset': '0'},  # S3->S4
                {'in': '1', 'state': '0000010000', 'areset': '0'},  # S4->S5
                {'in': '0', 'state': '0000100000', 'areset': '0'}   # S5->S8
            ]
        },
        {
            'scenario': 'PathToS9_Output11',
            'input variable': [
                {'in': '1', 'state': '0000000001', 'areset': '0'},  # S0->S1
                {'in': '1', 'state': '0000000010', 'areset': '0'},  # S1->S2
                {'in': '1', 'state': '0000000100', 'areset': '0'},  # S2->S3
                {'in': '1', 'state': '0000001000', 'areset': '0'},  # S3->S4
                {'in': '1', 'state': '0000010000', 'areset': '0'},  # S4->S5
                {'in': '1', 'state': '0000100000', 'areset': '0'},  # S5->S6
                {'in': '0', 'state': '0001000000', 'areset': '0'}   # S6->S9
            ]
        },
        {
            'scenario': 'ReturnToS0FromS7',
            'input variable': [
                {'in': '0', 'state': '0010000000', 'areset': '0'}   # S7->S0
            ]
        },
        {
            'scenario': 'ReturnToS0FromS8',
            'input variable': [
                {'in': '0', 'state': '0100000000', 'areset': '0'}   # S8->S0
            ]
        },
        {
            'scenario': 'ReturnToS0FromS9',
            'input variable': [
                {'in': '0', 'state': '1000000000', 'areset': '0'}   # S9->S0
            ]
        },
        {
            'scenario': 'StayInS7',
            'input variable': [
                {'in': '1', 'state': '0010000000', 'areset': '0'}   # S7->S7
            ]
        },
        {
            'scenario': 'S8ToS1',
            'input variable': [
                {'in': '1', 'state': '0100000000', 'areset': '0'}   # S8->S1
            ]
        },
        {
            'scenario': 'S9ToS1',
            'input variable': [
                {'in': '1', 'state': '1000000000', 'areset': '0'}   # S9->S1
            ]
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
