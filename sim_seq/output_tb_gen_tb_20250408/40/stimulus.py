import json

def gen_32bit_sequence():
    return ''.join(['1' if i % 2 == 0 else '0' for i in range(32)])

def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Normal Branch Prediction
    scenarios.append({
        'scenario': 'NormalBranchPrediction',
        'input variable': [{
            'clock cycles': 8,
            'predict_valid': ['1', '1', '1', '1', '1', '1', '1', '1'],
            'predict_taken': ['1', '0', '1', '0', '1', '0', '1', '0'],
            'train_mispredicted': ['0', '0', '0', '0', '0', '0', '0', '0'],
            'train_taken': ['0', '0', '0', '0', '0', '0', '0', '0'],
            'train_history': [format(0, '032b')] * 8
        }]
    })

    # Scenario 2: Branch Misprediction Recovery
    scenarios.append({
        'scenario': 'BranchMispredictionRecovery',
        'input variable': [{
            'clock cycles': 4,
            'predict_valid': ['0', '0', '0', '0'],
            'predict_taken': ['0', '0', '0', '0'],
            'train_mispredicted': ['1', '1', '1', '1'],
            'train_taken': ['1', '0', '1', '0'],
            'train_history': [
                '10101010101010101010101010101010',
                '01010101010101010101010101010101',
                '11111111111111111111111111111111',
                '00000000000000000000000000000000'
            ]
        }]
    })

    # Scenario 3: Prediction During Misprediction
    scenarios.append({
        'scenario': 'PredictionDuringMisprediction',
        'input variable': [{
            'clock cycles': 4,
            'predict_valid': ['1', '1', '1', '1'],
            'predict_taken': ['1', '1', '1', '1'],
            'train_mispredicted': ['1', '1', '1', '1'],
            'train_taken': ['0', '0', '0', '0'],
            'train_history': [gen_32bit_sequence()] * 4
        }]
    })

    # Scenario 4: Asynchronous Reset Operation
    scenarios.append({
        'scenario': 'AsynchronousResetOperation',
        'input variable': [{
            'clock cycles': 4,
            'predict_valid': ['0', '0', '0', '0'],
            'predict_taken': ['0', '0', '0', '0'],
            'train_mispredicted': ['0', '0', '0', '0'],
            'train_taken': ['0', '0', '0', '0'],
            'train_history': [format(0, '032b')] * 4
        }]
    })

    # Scenario 5: Consecutive Predictions
    scenarios.append({
        'scenario': 'ConsecutivePredictions',
        'input variable': [{
            'clock cycles': 32,
            'predict_valid': ['1'] * 32,
            'predict_taken': ['1', '0'] * 16,
            'train_mispredicted': ['0'] * 32,
            'train_taken': ['0'] * 32,
            'train_history': [format(0, '032b')] * 32
        }]
    })

    # Scenario 6: Consecutive Mispredictions
    scenarios.append({
        'scenario': 'ConsecutiveMispredictions',
        'input variable': [{
            'clock cycles': 8,
            'predict_valid': ['0'] * 8,
            'predict_taken': ['0'] * 8,
            'train_mispredicted': ['1'] * 8,
            'train_taken': ['1', '0'] * 4,
            'train_history': [format(i, '032b') for i in range(8)]
        }]
    })

    # Scenario 7: Reset Recovery
    scenarios.append({
        'scenario': 'ResetRecovery',
        'input variable': [{
            'clock cycles': 8,
            'predict_valid': ['1', '1', '1', '1', '0', '0', '0', '0'],
            'predict_taken': ['1', '1', '1', '1', '0', '0', '0', '0'],
            'train_mispredicted': ['0', '0', '0', '0', '1', '1', '1', '1'],
            'train_taken': ['0', '0', '0', '0', '1', '1', '1', '1'],
            'train_history': [format(0, '032b')] * 8
        }]
    })

    # Scenario 8: Long Run Pattern
    scenarios.append({
        'scenario': 'LongRunPattern',
        'input variable': [{
            'clock cycles': 40,
            'predict_valid': ['1'] * 32 + ['0'] * 8,
            'predict_taken': (['1'] * 16 + ['0'] * 16 + ['0'] * 8),
            'train_mispredicted': ['0'] * 32 + ['1'] * 8,
            'train_taken': ['0'] * 32 + ['1'] * 8,
            'train_history': [format(i % 2**32, '032b') for i in range(40)]
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
