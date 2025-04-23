import json
def _to_bit_str(value: int, width: int = 1) -> str:
    return format(value, f'0{width}b')

def stimulus_gen() -> list[dict]:
    scenarios = [
        {
            "scenario": "AllInputsLow",
            "vectors": [(0, 0, 0)]
        },
        {
            "scenario": "AllInputsHigh",
            "vectors": [(1, 1, 1)]
        },
        {
            "scenario": "CpuOverheatedOnly",
            "vectors": [(1, 0, 0)]
        },
        {
            "scenario": "ArrivedWithEmptyTank",
            "vectors": [(0, 1, 1)]
        },
        {
            "scenario": "ArrivedWithFullTank",
            "vectors": [(0, 1, 0)]
        },
        {
            "scenario": "DrivingWithEmptyTank",
            "vectors": [(0, 0, 1)]
        },
        {
            "scenario": "CpuOverheatWhileDriving",
            "vectors": [(1, 0, 0)]
        },
        {
            "scenario": "EmptyTankWithOverheat",
            "vectors": [(1, 0, 1)]
        }
    ]

    stimulus_list = []
    for sc in scenarios:
        inputs = []
        for cpu_oh, arr, gas_empty in sc["vectors"]:
            inputs.append({
                "cpu_overheated": _to_bit_str(cpu_oh),
                "arrived": _to_bit_str(arr),
                "gas_tank_empty": _to_bit_str(gas_empty)
            })

        stimulus_list.append({
            "scenario": sc["scenario"],
            "input variable": inputs
        })

    return stimulus_list
if __name__ == "__main__":
    result = stimulus_gen()
    # Convert result to JSON string
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
