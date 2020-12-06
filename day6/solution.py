from functools import reduce
from utils import file_into_string

input_as_string = file_into_string("day6/input.txt")

groups = input_as_string.strip().split("\n\n")

def get_yes_answers_1(group):
    return len(reduce(lambda a, b: set(a) | set(b), group.split("\n")))

def part_1():
    return sum([get_yes_answers_1(group) for group in groups])

def get_yes_answers_2(group):
    return len(reduce(lambda a, b: set(a) & set(b), group.split("\n")))

def part_2():
    return sum([get_yes_answers_2(group) for group in groups])


