from utils import file_into_list

expenses = file_into_list("day1/input.txt", lambda l: int(l))
N = len(expenses)

def part_1():
    for i in range(N):
        for j in range(i, N):
            if expenses[i] + expenses[j] == 2020:
                print(f"found {expenses[i]} and {expenses[j]}")
                print(f"multiplied: {expenses[i] * expenses[j]}")
                break

def part_2():
    for i in range(N):
        for j in range(i, N):
            for k in range(j, N):
                if expenses[i] + expenses[j] + expenses[k] == 2020:
                    print(f"found {expenses[i]} and {expenses[j]} and {expenses[k]}")
                    print(f"multiplied: {expenses[i] * expenses[j] * expenses[k]}")
                    break

part_2()
