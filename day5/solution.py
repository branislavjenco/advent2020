from utils import file_into_list, test

boarding_passes = file_into_list("day5/input.txt")

numrows = 128
numcols = 8

def midpoint(_min, _max):
    return (_min + _max) // 2 


def get_seat_coordinates(boarding_pass):
    min_row = 0
    max_row = 127

    for i in range(7):
        if boarding_pass[i] == "F":
            max_row = midpoint(min_row, max_row)
        elif boarding_pass[i] == "B":
            min_row = midpoint(min_row, max_row) + 1
        # print(f"Min row: {min_row}. Max row: {max_row}.")

    min_col = 0
    max_col = 7
    for i in range(7, 10):
        if boarding_pass[i] == "L":
            max_col = midpoint(min_col, max_col)
        elif boarding_pass[i] == "R":
            min_col = midpoint(min_col, max_col) + 1
        # print(f"Min col: {min_col}. Max col: {max_col}.")

    if min_row != max_row or min_col != max_col:
        print(min_row, max_row, min_col, max_col)
        raise AssertionError("Shouldn't happen")

    return max_row, max_col


def get_seat_id(coords):
    return coords[0] * 8 + coords[1]

test(get_seat_coordinates, ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"], [(70, 7), (14, 7), (102, 4)])
test(get_seat_id, [[70, 7], [14, 7], [102, 4]], [567, 119, 820])



def part_1():
    max_id = 0
    for bp in boarding_passes:
        seat_id = get_seat_id(get_seat_coordinates(bp))
        if seat_id > max_id:
            max_id = seat_id
    return max_id


def part_2():
    ids = set(range(128*8))
    for bp in boarding_passes:
        seat_id = get_seat_id(get_seat_coordinates(bp))
        ids.remove(seat_id) 
    return ids



