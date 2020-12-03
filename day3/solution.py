from utils import file_into_list
from functools import reduce

map_ = file_into_list("day3/input.txt")

def count_trees(_map, slope):
    dx = slope[0]
    dy = slope[1]
    x = 0
    y = 0
    max_y = len(map_)
    line_length = len(map_[0])

    trees_count = 0 
    while y < max_y:
        if map_[y][x] == "#":
            trees_count = trees_count + 1
        x = (x + dx) % line_length
        y = y + dy

    return trees_count


def part_1():
    print(count_trees(map_, (3, 1)))
    

def part_2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    counts = [count_trees(map_, slope) for slope in slopes]
    print(reduce(lambda a, b: a * b, counts))


part_1()
part_2()

