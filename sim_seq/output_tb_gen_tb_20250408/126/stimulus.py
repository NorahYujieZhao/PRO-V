import json
def stimulus_gen():
    # List to store all test scenarios
    scenarios = []
    
    # Scenario 1: Basic Toggle Operation with Input High
    scenarios.append({
        "scenario": "BasicToggleOperationWithInputHigh",
        "input variable": [
            {
                "clock cycles": 10,
                "in": ["1"] * 10  # Hold input high for 10 cycles to observe toggling
            }
        ]
    })
    
    # Scenario 2: Basic Hold Operation with Input Low
    scenarios.append({
        "scenario": "BasicHoldOperationWithInputLow",
        "input variable": [
            {
                "clock cycles": 10,
                "in": ["0"] * 10  # Hold input low for 10 cycles to verify stable output
            }
        ]
    })
    
    # Scenario 3: Input Transition during Clock Edge
    scenarios.append({
        "scenario": "InputTransitionDuringClockEdge",
        "input variable": [
            {
                "clock cycles": 8,
                "in": ["0", "1", "0", "1", "0", "1", "0", "1"]  # Alternate input each cycle
            }
        ]
    })
    
    # Scenario 4: Initial Power Up State
    scenarios.append({
        "scenario": "InitialPowerUpState",
        "input variable": [
            {
                "clock cycles": 5,
                "in": ["0", "0", "1", "1", "0"]  # Test initial state and transitions
            }
        ]
    })
    
    # Scenario 5: Clock Glitch Immunity
    scenarios.append({
        "scenario": "ClockGlitchImmunity",
        "input variable": [
            {
                "clock cycles": 6,
                "in": ["1", "1", "1", "0", "0", "0"]  # Stable inputs during clock glitches
            }
        ]
    })
    
    # Scenario 6: Rapid Input Changes
    scenarios.append({
        "scenario": "RapidInputChanges",
        "input variable": [
            {
                "clock cycles": 8,
                "in": ["1", "0", "1", "0", "1", "0", "1", "0"]  # Rapid alternating pattern
            }
        ]
    })
    
    # Scenario 7: Long Term Toggle Pattern
    scenarios.append({
        "scenario": "LongTermTogglePattern",
        "input variable": [
            {
                "clock cycles": 16,
                "in": ["1", "1", "1", "1", "0", "0", "0", "0",
                       "1", "1", "1", "1", "0", "0", "0", "0"]  # Extended pattern
            }
        ]
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
