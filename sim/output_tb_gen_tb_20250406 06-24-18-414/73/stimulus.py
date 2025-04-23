import json
def _to_bit_str(value: int, width: int) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "ValidSelectZero",
            "input variable": [{
                "sel": "000",
                "data0": "1010",
                "data1": "1111",
                "data2": "1111",
                "data3": "1111",
                "data4": "1111",
                "data5": "1111"
            }]
        },
        {
            "scenario": "ValidSelectFive",
            "input variable": [{
                "sel": "101",
                "data0": "0000",
                "data1": "0000",
                "data2": "0000",
                "data3": "0000",
                "data4": "0000",
                "data5": "0101"
            }]
        },
        {
            "scenario": "InvalidSelectSix",
            "input variable": [{
                "sel": "110",
                "data0": "1111",
                "data1": "1111",
                "data2": "1111",
                "data3": "1111",
                "data4": "1111",
                "data5": "1111"
            }]
        },
        {
            "scenario": "InvalidSelectSeven",
            "input variable": [{
                "sel": "111",
                "data0": "1111",
                "data1": "1111",
                "data2": "1111",
                "data3": "1111",
                "data4": "1111",
                "data5": "1111"
            }]
        },
        {
            "scenario": "AllZeroInputs",
            "input variable": [
                {"sel": f'{i:03b}',
                 "data0": "0000",
                 "data1": "0000",
                 "data2": "0000",
                 "data3": "0000",
                 "data4": "0000",
                 "data5": "0000"} for i in range(8)
            ]
        },
        {
            "scenario": "AllOneInputs",
            "input variable": [
                {"sel": f'{i:03b}',
                 "data0": "1111",
                 "data1": "1111",
                 "data2": "1111",
                 "data3": "1111",
                 "data4": "1111",
                 "data5": "1111"} for i in range(6)
            ]
        },
        {
            "scenario": "AlternatingPattern",
            "input variable": [
                {"sel": f'{i:03b}',
                 "data0": "1010",
                 "data1": "0101",
                 "data2": "1010",
                 "data3": "0101",
                 "data4": "1010",
                 "data5": "0101"} for i in range(6)
            ]
        },
        {
            "scenario": "OneHotDataInputs",
            "input variable": [
                {"sel": f'{i:03b}',
                 "data0": "0001",
                 "data1": "0010",
                 "data2": "0100",
                 "data3": "1000",
                 "data4": "0001",
                 "data5": "0010"} for i in range(6)
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
