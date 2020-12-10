from utils import file_into_list
import numpy as np

adapters = list(map(int, file_into_list("day10/input.txt")))

builtin = max(adapters) + 3

adapters.append(builtin)
adapters.append(0)
adapters = sorted(adapters)
L = len(adapters)

def part_1():
    count_ones = 0
    count_threes = 0
    for i in range(1, len(adapters)):
        if adapters[i] - adapters[i-1] == 1:
            count_ones += 1
        if adapters[i] - adapters[i-1] == 3:
            count_threes += 1

    print(count_ones * count_threes)

def part_2_naive():
    def fork(i):
        print(f"{i}\n")
        s = 0
        if i+1 < L and adapters[i+1] - adapters[i] <= 3:
            s += fork(i+1)
        if i+2 < L and adapters[i+2] - adapters[i] <= 3:
            s += fork(i+2)
        if i+3 < L and adapters[i+3] - adapters[i] <= 3:
            s += fork(i+3)
        if i >= L - 1:
            return 1
        else:
            if s == 0:
                raise AssertionError("Shouldn't happen")
            return s
    print(fork(0))

def part_2():
    counts = []
    for i in range(L):
        count = 0
        if i+1 < L and adapters[i+1] - adapters[i] <= 3:
            count += 1
        if i+2 < L and adapters[i+2] - adapters[i] <= 3:
            count += 1
        if i+3 < L and adapters[i+3] - adapters[i] <= 3:
            count += 1
        counts.append(count)

    acc = 1
    i = 0
    while i < L:
        if counts[i] == 3:
            j = i + 1
            threes = 1
            while counts[j] != 1:
                if counts[j] == 3:
                    threes += 1
                j += 1
            acc *= (threes*3 + 1)
            i = j
        elif counts[i] == 2:
            acc *= 2
            i += 1
        else:
            i += 1
    print(acc)


# dynamic programming solution credit: jonathan_paulson
# mine is about as fast or slightly faster, however I don't know exactly why mine works
# that is, I am not sure of the relationships between clusters of points in the graph
# (like 4, 5, 6, 7 in test 1) and the number of paths through them
# for a cluster of three points (like 10, 11, 12) it's two paths, for cluster of four points
# (like 4, 5, 6, 7 in test 1) it's 4 paths, and I know that for a cluster of 5 points, which
# did appear in input, it's 7 paths. But not sure how the relationship works
def part_2_dp():
    DP = {}
    # dp(i) = the number of ways to complete the adapter chain given
    #         that you are currently at adapter xs[i]
    def dp(i):
        if i == L - 1:
            return 1
        if i in DP:
            return DP[i]
        ans = 0
        for j in range(i+1, L):
            if adapters[j] - adapters[i] <= 3:
                ans += dp(j)
        DP[i] = ans
        return ans
    print(dp(0))

part_2()



