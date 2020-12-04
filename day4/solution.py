from utils import file_into_string
import re

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

input_string = file_into_string("day4/input.txt")
passport_strings = input_string.replace("\n\n", "$").split("$")
passport_strings = [s.replace("\n", " ") for s in passport_strings]

def part_1():
    def is_passport_valid_1(passport_string):
        _dict = {}
        for kv in passport_string.split(" "):
            if len(kv) < 1:
                continue
            k, v = kv.split(":")
            _dict[k] = v

        for f in required_fields:
            if f not in _dict:
                return False
            else:
                del _dict[f]

        if _dict.get("cid") is not None and len(_dict.keys()) == 1:
            return True
        elif len(_dict.keys()) == 0:
            return True
        else:
            return False

    count_valid = 0
    for ps in passport_strings:
        if is_passport_valid_1(ps):
            count_valid = count_valid + 1
    return count_valid


def is_byr_valid(value):
    return len(value) == 4 and int(value) >= 1920 and int(value) <= 2002

def is_iyr_valid(value):
    return len(value) == 4 and int(value) >= 2010 and int(value) <= 2020

def is_eyr_valid(value):
    return len(value) == 4 and int(value) >= 2020 and int(value) <= 2030

def is_hgt_valid(value):
    match = re.match("^(\d+)(cm|in)$", value)
    if match:
        if match.group(2) == "cm":
            val = match.group(1)
            return int(val) >= 150 and int(val) <= 193
        elif match.group(2) == "in":
            val = match.group(1)
            return int(val) >= 59 and int(val) <= 76
        else:
            return False
    else:
        return False

def is_hcl_valid(value):
    match = re.match("^#[0-9A-Fa-f]{6}$", value)  
    if match:
        return True
    else:
        return False

def is_ecl_valid(value):
    match = re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", value)
    if match:
        return True
    else:
        return False

def is_pid_valid(value):
    match = re.match("^[0-9]{9}$", value)
    if match:
        return True
    else:
        return False

def is_field_valid(key, value):
    if key == "byr":
        return is_byr_valid(value)
    elif key == "iyr":
        return is_iyr_valid(value)
    elif key == "eyr":
        return is_eyr_valid(value)
    elif key == "hgt":
        return is_hgt_valid(value)
    elif key == "hcl":
        return is_hcl_valid(value)
    elif key == "ecl":
        return is_ecl_valid(value)
    elif key == "pid":
        return is_pid_valid(value)
    elif key == "cid":
        return True

def part_2():
    def is_passport_valid_2(passport_string):
        _dict = {}
        for kv in passport_string.split(" "):
            if len(kv) < 1:
                continue
            k, v = kv.split(":")
            _dict[k] = v

        for f in required_fields:
            if f not in _dict:
                return False
            else:
                if not is_field_valid(f, _dict[f]):
                    return False
                del _dict[f]

        if _dict.get("cid") is not None and len(_dict.keys()) == 1:
            return True
        elif len(_dict.keys()) == 0:
            return True
        else:
            return False
                
    count_valid = 0
    for ps in passport_strings:
        if is_passport_valid_2(ps):
            count_valid = count_valid + 1
    return count_valid

print(part_2())
