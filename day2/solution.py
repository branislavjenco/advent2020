import re
from utils import file_into_list 

input_lines = file_into_list("day2/input.txt")

def parse_line(line):
    split = re.split("^(\d+)-(\d+) (\w): (\w+)$", line)
    min_num = int(split[1])
    max_num = int(split[2])
    char = split[3]
    password = split[4]
    return min_num, max_num, char, password


def count_char_in_string(char, string):
    count = 0
    for c in string:
        if c == char:
            count = count + 1
    return count

def is_password_valid_1(min_num, max_num, char, password):
    num_actual = count_char_in_string(char, password)
    return num_actual >= min_num and num_actual <= max_num


def is_password_valid_2(first_occurence, second_occurence, char, password):
    return (password[first_occurence - 1] == char and password[second_occurence - 1] != char) or (password[first_occurence - 1] != char and password[second_occurence - 1] == char)


def part_1():
    valid_count = 0
    for line in input_lines:
        min_num, max_num, char, password = parse_line(line)
        if is_password_valid_1(min_num, max_num, char, password):
            valid_count = valid_count + 1
    print(f"Number of valid passwords is: {valid_count}")


def part_2():
    valid_count = 0
    for line in input_lines:
        first_occurence, second_occurence, char, password = parse_line(line)
        if is_password_valid_2(first_occurence, second_occurence, char, password):
            valid_count = valid_count + 1
    print(f"Number of valid passwords is: {valid_count}")


