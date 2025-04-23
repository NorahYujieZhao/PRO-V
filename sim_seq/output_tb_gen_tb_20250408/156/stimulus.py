
import json
import random
def stimulus_gen():
    stim_list = []

    # Normal counting through all digits
    stim_list.append({
        "scenario": "NormalCounting",
        "input variable": [{
            "clock cycles": 20,
            "reset": ["0"] * 20
        }]
    })

    # Reset functionality test
    stim_list.append({
        "scenario": "ResetBehavior",
        "input variable": [{
            "clock cycles": 15,
            "reset": ["0"]*5 + ["1"] + ["0"]*9
        }]
    })

    # Test digit rollover (9->0)
    stim_list.append({
        "scenario": "DigitRollover",
        "input variable": [{
            "clock cycles": 12,
            "reset": ["0"]*12
        }]
    })

    # Multiple reset pulses
    stim_list.append({
        "scenario": "MultipleResets",
        "input variable": [{
            "clock cycles": 25,
            "reset": ["0"]*5 + ["1"] + ["0"]*8 + ["1"] + ["0"]*10
        }]
    })

    # Random test sequences
    import random
    for i in range(10):
        cycles = random.randint(15, 30)
        reset_seq = ["0"] * cycles
        # Insert random reset pulses
        for j in range(2):
            pos = random.randint(0, cycles-2)
            reset_seq[pos] = "1"
        
        stim_list.append({
            "scenario": f"RandomTest{i}",
            "input variable": [{
                "clock cycles": cycles,
                "reset": reset_seq
            }]
        })

    return stim_list
if __name__ == "__main__":
    result = stimulus_gen()
    # 将结果转换为 JSON 字符串
    if isinstance(result, list):
        result = json.dumps(result, indent=4)
    elif not isinstance(result, str):
        result = json.dumps(result, indent=4)

    with open("stimulus.json", "w") as f:
        f.write(result)
