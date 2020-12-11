from utils import file_into_list
from copy import deepcopy

_input = list(map(lambda line: list(line), file_into_list("day11/input.txt")))
floor = "."
empty = "L"
occup = "#"
width = len(_input[0])
height = len(_input)

def get_neighbourhood(point, layout):
    diffs = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
    return [at(point[0] + diff[0], point[1] + diff[1], layout) for diff in diffs]

def at(y, x, layout):
    if x < 0 or y < 0 or x >= width or y >= height:
        return None
    else:
        return layout[y][x]

def part_1(inp):
    while True:
        res = deepcopy(inp)
        changes = 0
        for y in range(height):
            for x in range(width):
                if inp[y][x] == empty and occup not in get_neighbourhood((y, x), inp):
                    changes += 1
                    res[y][x] = occup
                elif inp[y][x] == occup and len(list(filter(lambda s: s == occup, get_neighbourhood((y, x), inp)))) >= 4:
                    changes += 1
                    res[y][x] = empty
        if changes == 0:
            break
        inp = res

    count_occup = 0
    for x in range(width):
        for y in range(height):
            if res[y][x] == occup:
                count_occup += 1
    print(count_occup)
    
def incr(value):
    if value == 0:
        return value
    if value < 0:
        return value - 1
    if value > 0:
        return value + 1

def get_neighbourhood_expanded(point, layout):
    diffs = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
    for diff in diffs:
        while True:
            found = at(point[0] + diff[0], point[1] + diff[1], layout)
            if found == floor:
                diff[0] = incr(diff[0])
                diff[1] = incr(diff[1])
            else:
                break
    n = [at(point[0] + diff[0], point[1] + diff[1], layout) for diff in diffs]
    return n

                
def part_2(inp):
    while True:
        res = deepcopy(inp)
        changes = 0
        for y in range(height):
            for x in range(width):
                if inp[y][x] == empty and occup not in get_neighbourhood_expanded((y, x), inp):
                    changes += 1
                    res[y][x] = occup
                elif inp[y][x] == occup and len(list(filter(lambda s: s == occup, get_neighbourhood_expanded((y, x), inp)))) >= 5:
                    changes += 1
                    res[y][x] = empty
        if changes == 0:
            break
        inp = res

    count_occup = 0
    for x in range(width):
        for y in range(height):
            if res[y][x] == occup:
                count_occup += 1
    print(count_occup)

part_1(_input)
