import json
def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "NoRingNoVibrate",
            "input variable": [{
                "ring": "0",
                "vibrate_mode": "0"
            }]
        },
        {
            "scenario": "RingInNormalMode",
            "input variable": [{
                "ring": "1",
                "vibrate_mode": "0"
            }]
        },
        {
            "scenario": "RingInVibrateMode",
            "input variable": [{
                "ring": "1",
                "vibrate_mode": "1"
            }]
        },
        {
            "scenario": "NoRingInVibrateMode",
            "input variable": [{
                "ring": "0",
                "vibrate_mode": "1"
            }]
        },
        {
            "scenario": "ModeTransitionToVibrate",
            "input variable": [
                {"ring": "1", "vibrate_mode": "0"},
                {"ring": "1", "vibrate_mode": "1"}
            ]
        },
        {
            "scenario": "ModeTransitionToNormal",
            "input variable": [
                {"ring": "1", "vibrate_mode": "1"},
                {"ring": "1", "vibrate_mode": "0"}
            ]
        },
        {
            "scenario": "RapidModeToggle",
            "input variable": [
                {"ring": "1", "vibrate_mode": "0"},
                {"ring": "1", "vibrate_mode": "1"},
                {"ring": "1", "vibrate_mode": "0"},
                {"ring": "1", "vibrate_mode": "1"}
            ]
        },
        {
            "scenario": "RapidRingToggle",
            "input variable": [
                {"ring": "0", "vibrate_mode": "0"},
                {"ring": "1", "vibrate_mode": "0"},
                {"ring": "0", "vibrate_mode": "0"},
                {"ring": "1", "vibrate_mode": "0"}
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
