import json
def stimulus_gen():
    # Since there are no inputs in the DUT, we'll create scenarios
    # that verify the constant high output over different durations
    scenarios = [
        {
            "scenario": "BasicOperation",
            "input variable": [{}]
        },
        {
            "scenario": "ExtendedOperation",
            "input variable": [{} for _ in range(10)]
        },
        {
            "scenario": "LongTermOperation",
            "input variable": [{} for _ in range(20)]
        },
        {
            "scenario": "InitialState",
            "input variable": [{}]
        },
        {
            "scenario": "ContinuousOperation",
            "input variable": [{} for _ in range(15)]
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
