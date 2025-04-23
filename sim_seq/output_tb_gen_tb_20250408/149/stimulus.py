import json

def stimulus_gen():
    scenarios = []
    
    def gen_basic_prediction():
        return {
            'scenario': 'BasicBranchPrediction',
            'input variable': [
                {
                    'clock cycles': 4,
                    'predict_valid': ['1', '1', '1', '1'],
                    'predict_pc': ['0000001', '0000010', '0000100', '0001000'],
                    'train_valid': ['0', '0', '0', '0'],
                    'train_taken': ['0', '0', '0', '0'],
                    'train_mispredicted': ['0', '0', '0', '0'],
                    'train_history': ['0000000', '0000000', '0000000', '0000000'],
                    'train_pc': ['0000000', '0000000', '0000000', '0000000']
                }
            ]
        }

    def gen_history_update():
        return {
            'scenario': 'BranchHistoryUpdate',
            'input variable': [
                {
                    'clock cycles': 3,
                    'predict_valid': ['1', '1', '1'],
                    'predict_pc': ['0000001', '0000001', '0000001'],
                    'train_valid': ['0', '0', '0'],
                    'train_taken': ['0', '0', '0'],
                    'train_mispredicted': ['0', '0', '0'],
                    'train_history': ['0000000', '0000001', '0000011'],
                    'train_pc': ['0000000', '0000000', '0000000']
                }
            ]
        }

    def gen_basic_training():
        return {
            'scenario': 'BasicTrainingOperation',
            'input variable': [
                {
                    'clock cycles': 4,
                    'predict_valid': ['0', '0', '0', '0'],
                    'predict_pc': ['0000000', '0000000', '0000000', '0000000'],
                    'train_valid': ['1', '1', '1', '1'],
                    'train_taken': ['1', '1', '0', '0'],
                    'train_mispredicted': ['0', '0', '0', '0'],
                    'train_history': ['0000000', '0000001', '0000011', '0000111'],
                    'train_pc': ['0000001', '0000001', '0000001', '0000001']
                }
            ]
        }

    def gen_saturating_counter():
        return {
            'scenario': 'SaturatingCounterBehavior',
            'input variable': [
                {
                    'clock cycles': 5,
                    'predict_valid': ['0', '0', '0', '0', '0'],
                    'predict_pc': ['0000000', '0000000', '0000000', '0000000', '0000000'],
                    'train_valid': ['1', '1', '1', '1', '1'],
                    'train_taken': ['1', '1', '1', '1', '1'],
                    'train_mispredicted': ['0', '0', '0', '0', '0'],
                    'train_history': ['0000000', '0000000', '0000000', '0000000', '0000000'],
                    'train_pc': ['0000001', '0000001', '0000001', '0000001', '0000001']
                }
            ]
        }

    def gen_misprediction_recovery():
        return {
            'scenario': 'MispredictionRecovery',
            'input variable': [
                {
                    'clock cycles': 3,
                    'predict_valid': ['0', '0', '0'],
                    'predict_pc': ['0000000', '0000000', '0000000'],
                    'train_valid': ['1', '1', '1'],
                    'train_taken': ['1', '0', '1'],
                    'train_mispredicted': ['0', '1', '0'],
                    'train_history': ['0000001', '0000011', '0000111'],
                    'train_pc': ['0000001', '0000010', '0000100']
                }
            ]
        }

    def gen_concurrent_predict_train():
        return {
            'scenario': 'ConcurrentPredictAndTrain',
            'input variable': [
                {
                    'clock cycles': 3,
                    'predict_valid': ['1', '1', '1'],
                    'predict_pc': ['0000001', '0000010', '0000100'],
                    'train_valid': ['1', '1', '1'],
                    'train_taken': ['1', '0', '1'],
                    'train_mispredicted': ['1', '0', '0'],
                    'train_history': ['0000001', '0000011', '0000111'],
                    'train_pc': ['0000001', '0000010', '0000100']
                }
            ]
        }

    def gen_pht_collision():
        return {
            'scenario': 'PHTEntryCollision',
            'input variable': [
                {
                    'clock cycles': 4,
                    'predict_valid': ['1', '1', '1', '1'],
                    'predict_pc': ['0000001', '1000001', '0000001', '1000001'],
                    'train_valid': ['0', '0', '0', '0'],
                    'train_taken': ['0', '0', '0', '0'],
                    'train_mispredicted': ['0', '0', '0', '0'],
                    'train_history': ['0000000', '0000000', '0000000', '0000000'],
                    'train_pc': ['0000000', '0000000', '0000000', '0000000']
                }
            ]
        }

    def gen_async_reset():
        return {
            'scenario': 'AsynchronousReset',
            'input variable': [
                {
                    'clock cycles': 3,
                    'predict_valid': ['0', '0', '0'],
                    'predict_pc': ['0000000', '0000000', '0000000'],
                    'train_valid': ['0', '0', '0'],
                    'train_taken': ['0', '0', '0'],
                    'train_mispredicted': ['0', '0', '0'],
                    'train_history': ['0000000', '0000000', '0000000'],
                    'train_pc': ['0000000', '0000000', '0000000']
                }
            ]
        }

    def gen_index_hashing():
        return {
            'scenario': 'IndexHashingVerification',
            'input variable': [
                {
                    'clock cycles': 4,
                    'predict_valid': ['1', '1', '1', '1'],
                    'predict_pc': ['0101010', '1010101', '1111000', '0000111'],
                    'train_valid': ['0', '0', '0', '0'],
                    'train_taken': ['0', '0', '0', '0'],
                    'train_mispredicted': ['0', '0', '0', '0'],
                    'train_history': ['1010101', '0101010', '0000111', '1111000'],
                    'train_pc': ['0000000', '0000000', '0000000', '0000000']
                }
            ]
        }

    def gen_pht_read_before_write():
        return {
            'scenario': 'PHTReadBeforeWrite',
            'input variable': [
                {
                    'clock cycles': 3,
                    'predict_valid': ['1', '1', '1'],
                    'predict_pc': ['0000001', '0000001', '0000001'],
                    'train_valid': ['1', '1', '1'],
                    'train_taken': ['1', '0', '1'],
                    'train_mispredicted': ['0', '0', '0'],
                    'train_history': ['0000000', '0000001', '0000011'],
                    'train_pc': ['0000001', '0000001', '0000001']
                }
            ]
        }

    scenarios.extend([
        gen_basic_prediction(),
        gen_history_update(),
        gen_basic_training(),
        gen_saturating_counter(),
        gen_misprediction_recovery(),
        gen_concurrent_predict_train(),
        gen_pht_collision(),
        gen_async_reset(),
        gen_index_hashing(),
        gen_pht_read_before_write()
    ])

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
