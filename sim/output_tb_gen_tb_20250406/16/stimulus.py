
import json
import random

def stimulus_gen():
    def generate_onehot(pos):
        return format(1 << pos, '06b')

    scenarios = [
        {
            'scenario': 'InitialStateA_TransitionToB',
            'input variable': [
                {'y': '000001', 'w': '1'}
            ]
        },
        {
            'scenario': 'StateB_TransitionToC',
            'input variable': [
                {'y': '000010', 'w': '1'}
            ]
        },
        {
            'scenario': 'StateB_TransitionToD',
            'input variable': [
                {'y': '000010', 'w': '0'}
            ]
        },
        {
            'scenario': 'StateC_TransitionToE',
            'input variable': [
                {'y': '000100', 'w': '1'}
            ]
        },
        {
            'scenario': 'StateC_TransitionToD',
            'input variable': [
                {'y': '000100', 'w': '0'}
            ]
        },
        {
            'scenario': 'StateD_TransitionToF',
            'input variable': [
                {'y': '001000', 'w': '1'}
            ]
        },
        {
            'scenario': 'StateD_TransitionToA',
            'input variable': [
                {'y': '001000', 'w': '0'}
            ]
        },
        {
            'scenario': 'StateE_SelfLoop',
            'input variable': [
                {'y': '010000', 'w': '1'}
            ]
        },
        {
            'scenario': 'StateE_TransitionToD',
            'input variable': [
                {'y': '010000', 'w': '0'}
            ]
        },
        {
            'scenario': 'StateF_TransitionToC',
            'input variable': [
                {'y': '100000', 'w': '1'}
            ]
        },
        {
            'scenario': 'StateF_TransitionToD',
            'input variable': [
                {'y': '100000', 'w': '0'}
            ]
        },
        {
            'scenario': 'LongSequenceTest',
            'input variable': [
                {'y': '000001', 'w': '1'},  # A->B
                {'y': '000010', 'w': '1'},  # B->C
                {'y': '000100', 'w': '1'},  # C->E
                {'y': '010000', 'w': '0'},  # E->D
                {'y': '001000', 'w': '1'},  # D->F
                {'y': '100000', 'w': '1'}   # F->C
            ]
        }
    ]
    
    # Add random test sequences
    import random
    for i in range(10):
        random_sequence = []
        current_state = '000001'  # Start from state A
        for _ in range(5):
            w_value = str(random.randint(0, 1))
            random_sequence.append({'y': current_state, 'w': w_value})
            # Update current_state based on FSM rules
            if current_state == '000001':  # State A
                current_state = '000010' if w_value == '1' else '000001'
            elif current_state == '000010':  # State B
                current_state = '000100' if w_value == '1' else '001000'
            elif current_state == '000100':  # State C
                current_state = '010000' if w_value == '1' else '001000'
            elif current_state == '001000':  # State D
                current_state = '100000' if w_value == '1' else '000001'
            elif current_state == '010000':  # State E
                current_state = '010000' if w_value == '1' else '001000'
            elif current_state == '100000':  # State F
                current_state = '000100' if w_value == '1' else '001000'
        
        scenarios.append({
            'scenario': f'RandomSequence_{i}',
            'input variable': random_sequence
        })
    
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
