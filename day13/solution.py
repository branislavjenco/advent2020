from utils import file_into_list, test
import numpy as np

inp = file_into_list("day13/input.txt")
ts = int(inp[0])
bus_ids = inp[1].split(",")

def part_1():
    count = 0
    success = False
    while success == False:
        dep = ts + count
        for bus_id in bus_ids:
            if bus_id == 'x':
                continue
            else:
                if dep % int(bus_id) == 0:
                    print(count, int(bus_id))
                    print(count * int(bus_id))
                    success = True
                    break
        count += 1

def sum_term(prev_ids, prev_divs):
    res = 0
    for i in range(len(prev_divs)):
        div = prev_divs[i]
        res += div * np.prod(prev_ids[:i])
    return res

# using the chinese remainder theorem however an inefficient algorithm
# so still not any better than brute force
def solve_naive(ids):
    enumerated = list(filter(lambda ix: ix[1] != 'x', enumerate(ids)))
    prev_ids = [int(enumerated[0][1])]
    prev_divs = [0]
    # tried sorting from the highest number, didn't make any difference
    sorted_ = sorted(enumerated[1:], key=lambda tup: int(tup[1]), reverse=True)
    for i, v in sorted_:
        v = int(v)
        print(i, v, prev_ids, prev_divs)
        count = -i - sum_term(prev_ids, prev_divs) 
        div = 0
        product = int(np.prod(prev_ids))
        while True:
            if count % product == 0:
                div = count // product
                break
            count += v
        prev_ids.append(v)
        prev_divs.append(div)
    return sum_term(prev_ids, prev_divs)


# Extended Euclidean algorithm that also computes Bezout's coefficients
# in this case we never care about the gcd value as it's always 1
def extended_euclid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_euclid(b % a, a)
        return (gcd, y - (b//a) * x, x)

# looked up other computations for chinese remainder theorem
# using extended euclid's algo now
# this one is still too slow, probably because I always accumulate the values
def solve_chinese_naive(ids):
    tuples = list(map(lambda ix: (-ix[0], int(ix[1])), filter(lambda ix: ix[1] != 'x', enumerate(ids))))
    # using notation from wiki
    a1, n1 = tuples[0]
    for (a2, n2) in tuples[1:]:
        gcd, m1, m2 = extended_euclid(n1, n2)
        print("gcd, m1, m2 ", gcd, m1, m2)
        a1 = a1*m2*n2 + a2*m1*n1
        n1 = n1*n2
        # make the a1 into a more computable number (it's modulo n1)
        while a1 > n1:
            a1 = a1 - n1
        while a1 < 0:
            a1 += n1
    return a1

# same as before, but uses pairwise solutions
# instead of accumulating like before
def solve_efficient(ids):
    def pairwise_solution(tuple1, tuple2):
        # using notation from wiki
        a1, n1 = tuple1
        a2, n2 = tuple2
        gcd, m1, m2 = extended_euclid(n1, n2)
        print("gcd, m1, m2 ", gcd, m1, m2)
        a1 = a1*m2*n2 + a2*m1*n1
        n1 = n1*n2
        # make the a1 into a more computable number (it's modulo n1)
        while a1 > n1:
            a1 = a1 - n1
        while a1 < 0:
            a1 += n1
        return a1, n1

    tuples = list(map(lambda ix: (-ix[0], int(ix[1])), filter(lambda ix: ix[1] != 'x', enumerate(ids))))
    while len(tuples) > 1:
        tup1 = tuples.pop(0)
        tup2 = tuples.pop(0)
        tuples.append(pairwise_solution(tup1, tup2))
        print(tuples)
    return tuples[0][0]


test(solve_efficient, [['17','x','13','19'], ['67','7','59','61'], ['67','x','7','59','61'], ['67','7','x','59','61'], ['1789','37','47','1889']], [3417, 754018, 779210, 1261476, 1202161486])

def part_2():
    print(solve_efficient(bus_ids))


part_2()

