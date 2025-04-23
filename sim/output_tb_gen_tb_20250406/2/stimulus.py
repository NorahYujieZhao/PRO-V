
import json
import random

def stimulus_gen():
    scenarios = [
        {
            'scenario': 'FromStateA_Transitions',
            'input variable': [
                {'y': '000', 'w': '0'},  # A->B
                {'y': '000', 'w': '1'}   # A->A
            ]
        },
        {
            'scenario': 'FromStateB_Transitions',
            'input variable': [
                {'y': '001', 'w': '0'},  # B->C
                {'y': '001', 'w': '1'}   # B->D
            ]
        },
        {
            'scenario': 'FromStateC_Transitions',
            'input variable': [
                {'y': '010', 'w': '0'},  # C->E
                {'y': '010', 'w': '1'}   # C->D
            ]
        },
        {
            'scenario': 'FromStateD_Transitions',
            'input variable': [
                {'y': '011', 'w': '0'},  # D->F
                {'y': '011', 'w': '1'}   # D->A
            ]
        },
        {
            'scenario': 'FromStateE_Transitions',
            'input variable': [
                {'y': '100', 'w': '0'},  # E->E
                {'y': '100', 'w': '1'}   # E->D
            ]
        },
        {
            'scenario': 'FromStateF_Transitions',
            'input variable': [
                {'y': '101', 'w': '0'},  # F->C
                {'y': '101', 'w': '1'}   # F->D
            ]
        },
        {
            'scenario': 'RandomTransitions',
            'input variable': [
                {'y': '000', 'w': '0'},  # A->B
                {'y': '001', 'w': '1'},  # B->D
                {'y': '011', 'w': '0'},  # D->F
                {'y': '101', 'w': '1'},  # F->D
                {'y': '011', 'w': '1'}   # D->A
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
