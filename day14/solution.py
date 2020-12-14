from utils import file_into_list
import numpy as np
from itertools import chain, combinations
import re

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

program = file_into_list("day14/input.txt")
multiplier = 10
memory = np.zeros(2**multiplier, dtype=np.int)


def parse_mask(line):
    _, mask = line.split(" = ")
    floatmask_indexes = []
    reversed_mask = mask[::-1]
    for i in range(len(mask)):
        if reversed_mask[i] == "X":
            floatmask_indexes.append(i)
    ormask = mask.replace("X", "0")
    andmask = mask.replace("X", "1")
    floatmask_combinations = powerset(floatmask_indexes)
    return int(ormask, 2), int(andmask, 2), floatmask_indexes, floatmask_combinations

def parse_mask2(line):
    _, mask = line.split(" = ")
    floatmask_indexes = []
    for i in range(len(mask)):
        if mask[i] == "X":
            floatmask_indexes.append(i)
    floatmask_combinations = powerset(floatmask_indexes)
    return mask, floatmask_indexes, floatmask_combinations

def parse_memset(line):
    match = re.match("^mem\[(\d+)\] = (\d+)$", line)
    if not match:
        raise AssertionError()
    return match.group(1), match.group(2)

def part_1():
    multiplier = 1
    memory = {}
    current_mask = None

    for line in program:
        if line.startswith("mask"):
            current_mask = parse_mask(line)
        elif line.startswith("mem"):
            address, value = parse_memset(line)
            ormask, andmask, _, _ = current_mask 
            bvalue = int(value)
            memory[int(address)] = bvalue & andmask | ormask
    print(sum(memory.values()))


# not efficient in the slightest but I was stuck on a bug
# that was completely unrelated to the puzzle and the test
# didnt uncover it
def part_2():
    memory = {}
    current_mask = None

    for line in program:
        if line.startswith("mask"):
            current_mask = line
        elif line.startswith("mem"):
            address, value = parse_memset(line)
            mask, all_floating_indexes, combinations = parse_mask2(current_mask)

            address = int(address)
            masked_addresses = []
            new_address_base = address
            address_as_list = list(bin(address).replace("0b","").rjust(36, '0'))
            for i in range(36):
                if mask[i] == "1":
                    address_as_list[i] = "1"

            for c in combinations:
                res = address_as_list.copy()
                for i in range(36):
                    if i in all_floating_indexes:
                        if i in c:
                            res[i] = '1'
                        else:
                            res[i] = '0'
                res = int("".join(res), 2)
                masked_addresses.append(res)
            for addr in masked_addresses:
                memory[addr] = int(value)
    print(sum(memory.values()))

part_2()

        
        
