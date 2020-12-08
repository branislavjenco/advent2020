from utils import file_into_list
import re

instructions = file_into_list("day8/input.txt")

def parse_ins(line):
    match = re.match("^(\w+) ((?:-|\+)\d+)$", line)
    if not match:
        raise AssertionError("No match when parsing line")
    return match.groups()

parsed_instructions = [parse_ins(i) for i in instructions]

class State:
    acc = 0
    ic = 0
    visited = set()
    
    def __init__(self, acc, ic):
        self.acc = acc
        self.ic = ic
        self.visited = set()
    
    def __str__(self):
        return f"Acc: {self.acc}, Ic: {self.ic}, Visited: {self.visited}"


def accumulate(state, value):
    state.acc += value

def jump(state, value):
    state.ic += value

def advance(state):
    state.ic += 1

def update_visited(state, value):
    state.visited.add(value)

def assert_not_visited(state):
    if state.ic in state.visited:
        raise AssertionError("Found loop")


def execute_ins(op, arg, state):
    current_ic = state.ic
    assert_not_visited(state)
    if op == "acc":
        accumulate(state, (int(arg)))
        advance(state)
    elif op == "jmp":
        jump(state, int(arg))
    elif op == "nop":
        advance(state)
    else:
        raise AssertionError("Unknown operation")
    update_visited(state, current_ic) 


def part_1():
    state = State(0, 0)
    while True:
        print(state)
        operation, argument = parsed_instructions[state.ic]
        try:
            execute_ins(operation, argument, state)
        except AssertionError as e:
            print(f"Terminating because looping. {e}")
            break

    print(state)

def flip_ins(instruction_list, count):
    new_list = instruction_list.copy()
    inner_count = 0
    for i, (op, arg) in enumerate(instruction_list):
        if op == "nop" or op == "jmp":
            if inner_count == count:
                if op == "nop":
                    new_list[i] = ("jmp", arg)
                elif op == "jmp":
                    new_list[i] = ("nop", arg)
                break
            inner_count += 1
    else:
        raise AssertionError("shouldnt go through all of the list")
    return new_list


    

def part_2():
    success = False
    counter = 0
    while True:
        if success:
            break

        modified_instructions = flip_ins(parsed_instructions, counter)
        state = State(0, 0)
        while True:
            if state.ic == len(modified_instructions):
                success = True
                break
            operation, argument = modified_instructions[state.ic]
            try:
                execute_ins(operation, argument, state)
            except AssertionError as e:
                print(f"Terminating because looping, {e}")
                success = False
                break
        counter += 1
    print(state)

