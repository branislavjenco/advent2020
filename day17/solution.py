from utils import file_into_list
import numpy as np
from itertools import product

init = file_into_list("day17/input.txt")

def char_to_int(char):
    if char == "#":
        return 1
    elif char == ".":
        return 0

init_int = []
for line in init:
    init_int.append(list(map(char_to_int, list(line))))


L = 30
def get_neighbours(xyz, diffs):
    neighbour_positions = [xyz+diff for diff in diffs]
    neighbour_positions = np.clip(np.array(neighbour_positions), 0, L - 1)
    return neighbour_positions

def advance(old_state, new_state, lut):
    new_state.fill(0)
    it = np.nditer(old_state, flags=['multi_index'])
    for v in it:
        idx = it.multi_index
        neighbours = lut[idx]
        s = np.sum(old_state[tuple(neighbours.T)])
        if v == 1:
            if s == 2 or s == 3:
                new_state[tuple(idx)] = 1
            else:
                new_state[tuple(idx)] = 0
        elif v == 0:
            if s == 3:
                new_state[tuple(idx)] = 1
            else:
                new_state[tuple(idx)] = 0



def part_1():
    diffs = list(product(range(-1, 2), repeat=3))
    diffs.remove((0, 0, 0))
    diffs = np.array(diffs, dtype=np.int)

    state = np.zeros([L, L, L], dtype=np.int)
    state[10:13, 10:13, 10] = np.array(init_int)
    state2 = np.zeros([L, L, L], dtype=np.int)

    neighbour_lookup = {}
    it = np.nditer(state, flags=['multi_index'])
    for v in it:
        neighbours = get_neighbours(np.array(it.multi_index), diffs)
        neighbour_lookup[it.multi_index] = neighbours

    print("lut complete")

    for i in range(6):
        advance(state, state2, neighbour_lookup)
        tmp = state
        state = state2
        state2 = tmp
    

    print("part 1:", np.sum(state))

def part_2():

    diffs2 = list(product(range(-1, 2), repeat=4))
    diffs2.remove((0, 0, 0, 0))
    diffs2 = np.array(diffs2, dtype=np.int)

    state = np.zeros([L, L, L, L], dtype=np.int)
    state[10:18, 10:18, 10, 10] = np.array(init_int)
    state2 = np.zeros([L, L, L, L], dtype=np.int)

    neighbour_lookup = {}
    it = np.nditer(state, flags=['multi_index'])
    for v in it:
        neighbours = get_neighbours(np.array(it.multi_index), diffs2)
        neighbour_lookup[it.multi_index] = neighbours


    print("lut complete")
    for i in range(6):
        advance(state, state2, neighbour_lookup)
        tmp = state
        state = state2
        state2 = tmp

    print("part 2", np.sum(state))

part_2()



