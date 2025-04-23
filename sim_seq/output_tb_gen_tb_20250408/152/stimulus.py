import json

import random

def create_empty_grid():
    return '0' * 256

def set_cell(grid, x, y, value):
    pos = y * 16 + x
    return grid[:pos] + value + grid[pos+1:]

def create_block_pattern(x, y):
    grid = create_empty_grid()
    grid = set_cell(grid, x, y, '1')
    grid = set_cell(grid, x+1, y, '1')
    grid = set_cell(grid, x, y+1, '1')
    grid = set_cell(grid, x+1, y+1, '1')
    return grid

def create_blinker_pattern(x, y):
    grid = create_empty_grid()
    grid = set_cell(grid, x, y, '1')
    grid = set_cell(grid, x, y+1, '1')
    grid = set_cell(grid, x, y+2, '1')
    return grid

def stimulus_gen():
    scenarios = []
    
    # Scenario 1: Initial State Loading
    scenarios.append({
        'scenario': 'InitialStateLoading',
        'input variable': [{
            'clock cycles': 3,
            'load': ['1', '0', '0'],
            'data': [create_block_pattern(4, 4), create_empty_grid(), create_empty_grid()]
        }]
    })
    
    # Scenario 2: Single Cell Evolution
    single_cell = set_cell(create_empty_grid(), 8, 8, '1')
    scenarios.append({
        'scenario': 'SingleCellEvolution',
        'input variable': [{
            'clock cycles': 4,
            'load': ['1', '0', '0', '0'],
            'data': [single_cell, single_cell, single_cell, single_cell]
        }]
    })
    
    # Scenario 3: Stable Pattern
    block = create_block_pattern(4, 4)
    scenarios.append({
        'scenario': 'StablePattern',
        'input variable': [{
            'clock cycles': 5,
            'load': ['1', '0', '0', '0', '0'],
            'data': [block, block, block, block, block]
        }]
    })
    
    # Scenario 4: Cell Birth
    birth_pattern = create_blinker_pattern(7, 7)
    scenarios.append({
        'scenario': 'CellBirth',
        'input variable': [{
            'clock cycles': 4,
            'load': ['1', '0', '0', '0'],
            'data': [birth_pattern, birth_pattern, birth_pattern, birth_pattern]
        }]
    })
    
    # Scenario 5: Overpopulation
    dense_pattern = '1' * 256
    scenarios.append({
        'scenario': 'Overpopulation',
        'input variable': [{
            'clock cycles': 3,
            'load': ['1', '0', '0'],
            'data': [dense_pattern, dense_pattern, dense_pattern]
        }]
    })
    
    # Scenario 6: Toroidal Edge Wrapping
    edge_pattern = set_cell(create_empty_grid(), 0, 0, '1')
    scenarios.append({
        'scenario': 'ToroidalEdgeWrapping',
        'input variable': [{
            'clock cycles': 4,
            'load': ['1', '0', '0', '0'],
            'data': [edge_pattern, edge_pattern, edge_pattern, edge_pattern]
        }]
    })
    
    # Scenario 7: Oscillator Pattern
    blinker = create_blinker_pattern(5, 5)
    scenarios.append({
        'scenario': 'OscillatorPattern',
        'input variable': [{
            'clock cycles': 6,
            'load': ['1', '0', '0', '0', '0', '0'],
            'data': [blinker, blinker, blinker, blinker, blinker, blinker]
        }]
    })
    
    # Scenario 8: All Cells Dead
    all_dead = create_empty_grid()
    scenarios.append({
        'scenario': 'AllCellsDead',
        'input variable': [{
            'clock cycles': 3,
            'load': ['1', '0', '0'],
            'data': [all_dead, all_dead, all_dead]
        }]
    })
    
    # Scenario 9: All Cells Alive
    all_alive = '1' * 256
    scenarios.append({
        'scenario': 'AllCellsAlive',
        'input variable': [{
            'clock cycles': 4,
            'load': ['1', '0', '0', '0'],
            'data': [all_alive, all_alive, all_alive, all_alive]
        }]
    })
    
    # Scenario 10: Multiple Generation Evolution
    complex_pattern = create_blinker_pattern(4, 4)
    complex_pattern = set_cell(complex_pattern, 7, 7, '1')
    scenarios.append({
        'scenario': 'MultipleGenerationEvolution',
        'input variable': [{
            'clock cycles': 8,
            'load': ['1', '0', '0', '0', '0', '0', '0', '0'],
            'data': [complex_pattern] * 8
        }]
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
