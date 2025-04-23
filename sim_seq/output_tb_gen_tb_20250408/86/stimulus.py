import json
def stimulus_gen():
    def gen_shift_sequence(value, bits=4):
        return [format((value >> i) & 1, '01b') for i in range(bits-1, -1, -1)]

    scenarios = []

    # Scenario 1: Basic Shift Operation
    scenario1 = {
        'scenario': 'BasicShiftOperation',
        'input variable': [{
            'clock cycles': 4,
            'shift_ena': ['1', '1', '1', '1'],
            'count_ena': ['0', '0', '0', '0'],
            'data': ['1', '0', '1', '1']
        }]
    }
    scenarios.append(scenario1)

    # Scenario 2: Basic Down Count Operation
    scenario2 = {
        'scenario': 'BasicDownCountOperation',
        'input variable': [{
            'clock cycles': 4,
            'shift_ena': ['1', '1', '1', '1'],
            'count_ena': ['0', '0', '0', '0'],
            'data': ['1', '0', '1', '0']
        }, {
            'clock cycles': 3,
            'shift_ena': ['0', '0', '0'],
            'count_ena': ['1', '1', '1'],
            'data': ['0', '0', '0']
        }]
    }
    scenarios.append(scenario2)

    # Scenario 3: Counter Rollover
    scenario3 = {
        'scenario': 'CounterRollover',
        'input variable': [{
            'clock cycles': 4,
            'shift_ena': ['1', '1', '1', '1'],
            'count_ena': ['0', '0', '0', '0'],
            'data': ['0', '0', '0', '0']
        }, {
            'clock cycles': 2,
            'shift_ena': ['0', '0'],
            'count_ena': ['1', '1'],
            'data': ['0', '0']
        }]
    }
    scenarios.append(scenario3)

    # Scenario 4: Shift Register Boundary
    scenario4 = {
        'scenario': 'ShiftRegisterBoundary',
        'input variable': [{
            'clock cycles': 4,
            'shift_ena': ['1', '1', '1', '1'],
            'count_ena': ['0', '0', '0', '0'],
            'data': ['1', '0', '1', '0']
        }]
    }
    scenarios.append(scenario4)

    # Scenario 5: Counter Maximum Value
    scenario5 = {
        'scenario': 'CounterMaximumValue',
        'input variable': [{
            'clock cycles': 4,
            'shift_ena': ['1', '1', '1', '1'],
            'count_ena': ['0', '0', '0', '0'],
            'data': ['1', '1', '1', '1']
        }, {
            'clock cycles': 4,
            'shift_ena': ['0', '0', '0', '0'],
            'count_ena': ['1', '1', '1', '1'],
            'data': ['0', '0', '0', '0']
        }]
    }
    scenarios.append(scenario5)

    # Scenario 6: Mode Switching
    scenario6 = {
        'scenario': 'ModeSwitching',
        'input variable': [{
            'clock cycles': 2,
            'shift_ena': ['1', '1'],
            'count_ena': ['0', '0'],
            'data': ['1', '0']
        }, {
            'clock cycles': 2,
            'shift_ena': ['0', '0'],
            'count_ena': ['1', '1'],
            'data': ['0', '0']
        }, {
            'clock cycles': 2,
            'shift_ena': ['1', '1'],
            'count_ena': ['0', '0'],
            'data': ['1', '1']
        }]
    }
    scenarios.append(scenario6)

    # Scenario 7: Clock Edge Behavior
    scenario7 = {
        'scenario': 'ClockEdgeBehavior',
        'input variable': [{
            'clock cycles': 4,
            'shift_ena': ['1', '1', '1', '1'],
            'count_ena': ['0', '0', '0', '0'],
            'data': ['1', '0', '1', '0']
        }]
    }
    scenarios.append(scenario7)

    # Scenario 8: Initial State
    scenario8 = {
        'scenario': 'InitialState',
        'input variable': [{
            'clock cycles': 1,
            'shift_ena': ['0'],
            'count_ena': ['0'],
            'data': ['0']
        }]
    }
    scenarios.append(scenario8)

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
