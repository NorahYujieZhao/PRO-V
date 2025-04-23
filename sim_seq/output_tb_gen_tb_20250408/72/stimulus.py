import json
def stimulus_gen():
    scenarios = []
    
    # Helper function to create a scenario dictionary
    def create_scenario(name, input_vars):
        return {
            "scenario": name,
            "input variable": input_vars
        }
    
    # Scenario 1: Normal Data Capture
    scenarios.append(create_scenario("NormalDataCapture", [
        {
            "clock cycles": 8,
            "d": ["0", "0", "1", "1", "0", "0", "1", "1"],
            "ar": ["0", "0", "0", "0", "0", "0", "0", "0"]
        }
    ]))
    
    # Scenario 2: Asynchronous Reset Assertion
    scenarios.append(create_scenario("AsynchronousResetAssertion", [
        {
            "clock cycles": 6,
            "d": ["1", "1", "1", "1", "1", "1"],
            "ar": ["0", "0", "1", "1", "1", "0"]
        }
    ]))
    
    # Scenario 3: Reset Release Operation
    scenarios.append(create_scenario("ResetReleaseOperation", [
        {
            "clock cycles": 6,
            "d": ["1", "1", "1", "1", "1", "1"],
            "ar": ["1", "1", "0", "0", "0", "0"]
        }
    ]))
    
    # Scenario 4: Setup Time Verification
    scenarios.append(create_scenario("SetupTimeVerification", [
        {
            "clock cycles": 8,
            "d": ["0", "1", "0", "1", "0", "1", "0", "1"],
            "ar": ["0", "0", "0", "0", "0", "0", "0", "0"]
        }
    ]))
    
    # Scenario 5: Hold Time Verification
    scenarios.append(create_scenario("HoldTimeVerification", [
        {
            "clock cycles": 8,
            "d": ["1", "0", "1", "0", "1", "0", "1", "0"],
            "ar": ["0", "0", "0", "0", "0", "0", "0", "0"]
        }
    ]))
    
    # Scenario 6: Clock Edge Sensitivity
    scenarios.append(create_scenario("ClockEdgeSensitivity", [
        {
            "clock cycles": 6,
            "d": ["0", "1", "1", "0", "0", "1"],
            "ar": ["0", "0", "0", "0", "0", "0"]
        }
    ]))
    
    # Scenario 7: Reset During Clock Edge
    scenarios.append(create_scenario("ResetDuringClockEdge", [
        {
            "clock cycles": 6,
            "d": ["1", "1", "1", "0", "0", "1"],
            "ar": ["0", "1", "1", "0", "0", "0"]
        }
    ]))
    
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
