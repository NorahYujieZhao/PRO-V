
import json
import random

def stimulus_gen():
    scenarios = [
        {
            'scenario': 'StateA_Transitions',
            'input variable': [
                {'y': '000001', 'w': '0'},  # A->B
                {'y': '000001', 'w': '1'}   # A->A
            ]
        },
        {
            'scenario': 'StateB_Transitions',
            'input variable': [
                {'y': '000010', 'w': '0'},  # B->C
                {'y': '000010', 'w': '1'}   # B->D
            ]
        },
        {
            'scenario': 'StateC_Transitions',
            'input variable': [
                {'y': '000100', 'w': '0'},  # C->E
                {'y': '000100', 'w': '1'}   # C->D
            ]
        },
        {
            'scenario': 'StateD_Transitions',
            'input variable': [
                {'y': '001000', 'w': '0'},  # D->F
                {'y': '001000', 'w': '1'}   # D->A
            ]
        },
        {
            'scenario': 'StateE_Transitions',
            'input variable': [
                {'y': '010000', 'w': '0'},  # E->E
                {'y': '010000', 'w': '1'}   # E->D
            ]
        },
        {
            'scenario': 'StateF_Transitions',
            'input variable': [
                {'y': '100000', 'w': '0'},  # F->C
                {'y': '100000', 'w': '1'}   # F->D
            ]
        },
        {
            'scenario': 'ComplexPathTraversal',
            'input variable': [
                {'y': '000001', 'w': '0'},  # A->B
                {'y': '000010', 'w': '0'},  # B->C
                {'y': '000100', 'w': '0'},  # C->E
                {'y': '010000', 'w': '1'},  # E->D
                {'y': '001000', 'w': '1'}   # D->A
            ]
        },
        {
            'scenario': 'EdgeCases',
            'input variable': [
                {'y': '000000', 'w': '0'},  # All zeros
                {'y': '111111', 'w': '1'},  # All ones
                {'y': '010101', 'w': '0'},  # Alternating pattern
                {'y': '101010', 'w': '1'}   # Another alternating pattern
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
