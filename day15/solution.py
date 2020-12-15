from utils import file_into_list, test, file_into_string

tests = file_into_list("day15/tests_2.txt")
tests = [line.split(" ") for line in tests]
inputs, expected = zip(*tests)

inputs = [list(map(int, i.split(","))) for i in inputs]
expected = list(map(int, expected))

def solve(starting_numbers, position=30000000):
    print("Starting")
    memory = {}
    res = None
    most_recent = starting_numbers[-1] 
    for i, n in enumerate(starting_numbers):
        memory[n] = [i+1]
    for i in range(len(starting_numbers) + 1, position+1):
        #print(i, most_recent, memory)
        if len(memory[most_recent]) == 1:
            #print(f"Saving {0} at {i}")
            if 0 not in memory:
                memory[0] = [i]
            memory[0] = [memory[0][-1], i]
            res = 0
        else:
            num = memory[most_recent][1] - memory[most_recent][0]
            #print(f"Saving {num} at {i}")
            if num not in memory:
                memory[num] = [i]
            memory[num] = [memory[num][-1], i]
            res = num
            #print(i, num)
        most_recent = res
    return res

#test(solve, inputs[::-1], expected[::-1])
_input = file_into_string("day15/input.txt")
_input = list(map(int, _input.split(",")))
print(solve(_input))
