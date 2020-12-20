from utils import file_into_list
import numpy as np

exprs = file_into_list("day18/input.txt")


def ev(expr, i=0):
    acc = 0
    op = None 
    while i < len(expr):
        c = expr[i]
        if c == "+" or c == "*":
            op = c
        elif c == "(":
            subresult, new_i = ev(expr, i+1)
            if op == "+":
                acc += subresult
            elif op == "*":
                acc *= subresult
            elif op is None:
                acc += subresult
            i = new_i
        elif c == ")":
            return acc, i
        else:
            if op == "+":
                acc += int(c)
            elif op == "*":
                acc *= int(c)
            elif op is None:
                acc = int(c)
        i += 1
    return acc

def ev2(expr, i=0):
    sums = []
    is_adding = False
    curr_acc = 0
    while i < len(expr):
        c = expr[i]
        if c == "+":
            is_adding = True
        elif c == "*":
            is_adding = False
            sums.append(curr_acc)
            curr_acc = 0
        elif c == "(":
            subresult, new_i = ev2(expr, i+1)
            curr_acc += subresult
            i = new_i
        elif c == ")":
            sums.append(curr_acc)
            return np.prod(sums, dtype=np.int), i
        else:
            curr_acc += int(c)

        i += 1
    sums.append(curr_acc)
    return np.prod(sums, dtype=np.int)


s = 0
s2 = 0
for expr in exprs:
    expr = expr.replace(" ", "")
    s += ev(expr)
    subres = ev2(expr)
    s2 += subres

print("Part 1:", s)
print("Part 2:", s2)

    
