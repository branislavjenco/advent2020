from utils import file_into_list

preamble_length = 25

L = list(map(int, file_into_list("day9/input.txt")))

def part_1():
    for i, value in enumerate(L[preamble_length:]):
        i = preamble_length + i
        print(i, value)
        preceeding = L[i-preamble_length:i]
        print(preceeding)
        hit = False
        for num in preceeding:
            sub = value - num
            print(f"sub {sub}")
            if sub in preceeding:
                hit = True
        if hit is False:
            print(f"value {value} at position {i} is invalid")
            break

find_number = 70639851 # position 561
position = 561

def get_sequence(_list):
    curr_length = 2
    while True:
        for i in range(position - preamble_length - curr_length):
            print(i, L[i])
            if sum(L[i:i+curr_length]) == find_number:
                print(L[i:i+curr_length])
                return L[i:i+curr_length]
        for i in range(position + 1, len(L) - curr_length):
            print(i, L[i])
            if sum(L[i:i+curr_length]) == find_number:
                print(L[i:i+curr_length])
                return L[i:i+curr_length]
        curr_length += 1 

def part_2():
    seq = get_sequence(L)
    print(min(seq) + max(seq))


        

    
