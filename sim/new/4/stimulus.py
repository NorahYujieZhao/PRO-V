import json
def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllZeroInputs",
            "input variable": [{"a": "0", "b": "0"}]
        },
        {
            "scenario": "InputAOnlyHigh",
            "input variable": [{"a": "1", "b": "0"}]
        },
        {
            "scenario": "InputBOnlyHigh",
            "input variable": [{"a": "0", "b": "1"}]
        },
        {
            "scenario": "AllOneInputs",
            "input variable": [{"a": "1", "b": "1"}]
        },
        {
            "scenario": "ToggleAKeepBLow",
            "input variable": [
                {"a": "0", "b": "0"},
                {"a": "1", "b": "0"},
                {"a": "0", "b": "0"},
                {"a": "1", "b": "0"}
            ]
        },
        {
            "scenario": "ToggleBKeepALow",
            "input variable": [
                {"a": "0", "b": "0"},
                {"a": "0", "b": "1"},
                {"a": "0", "b": "0"},
                {"a": "0", "b": "1"}
            ]
        },
        {
            "scenario": "AlternatingInputs",
            "input variable": [
                {"a": "0", "b": "0"},
                {"a": "1", "b": "1"},
                {"a": "0", "b": "0"},
                {"a": "1", "b": "1"}
            ]
        },
        {
            "scenario": "RandomPatterns",
            "input variable": [
                {"a": format(i & 1, '01b'), "b": format((i >> 1) & 1, '01b')}
                for i in range(10)
            ]
        }
    ]
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
