import json
def stimulus_gen():
    # Helper function to generate binary combinations for 4 inputs
    def gen_binary_combinations(n):
        return [format(i, f'0{n}b') for i in range(2**n)]
    
    scenarios = []
    
    # Test all combinations for first NAND gate
    for bits in gen_binary_combinations(4):
        scenarios.append({
            "scenario": f"NAND1_Input_{bits}",
            "input variable": [{
                "p1a": bits[0],
                "p1b": bits[1],
                "p1c": bits[2],
                "p1d": bits[3],
                "p2a": "0",
                "p2b": "0",
                "p2c": "0",
                "p2d": "0"
            }]
        })
    
    # Test all combinations for second NAND gate
    for bits in gen_binary_combinations(4):
        scenarios.append({
            "scenario": f"NAND2_Input_{bits}",
            "input variable": [{
                "p1a": "0",
                "p1b": "0",
                "p1c": "0",
                "p1d": "0",
                "p2a": bits[0],
                "p2b": bits[1],
                "p2c": bits[2],
                "p2d": bits[3]
            }]
        })
    
    # Test both NAND gates simultaneously with same inputs
    for bits in gen_binary_combinations(4):
        scenarios.append({
            "scenario": f"BOTH_NAND_Same_Input_{bits}",
            "input variable": [{
                "p1a": bits[0],
                "p1b": bits[1],
                "p1c": bits[2],
                "p1d": bits[3],
                "p2a": bits[0],
                "p2b": bits[1],
                "p2c": bits[2],
                "p2d": bits[3]
            }]
        })
    
    # Add alternating pattern tests
    scenarios.append({
        "scenario": "Alternating_Pattern",
        "input variable": [{
            "p1a": "1",
            "p1b": "0",
            "p1c": "1",
            "p1d": "0",
            "p2a": "0",
            "p2b": "1",
            "p2c": "0",
            "p2d": "1"
        }]
    })
    
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
