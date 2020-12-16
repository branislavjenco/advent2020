from utils import file_into_string

input_ = file_into_string("day16/input.txt")

def parse_input(inp):
    rules, ticket, others = inp.split("\n\n")
    rules = rules.split("\n")
    rules_as_dict = {}
    for rule in rules:
        name, ranges = rule.split(": ")
        ranges = ranges.split(" or ")
        ranges = [r.split("-") for r in ranges]
        ranges = [range(int(fro), int(to)+1) for fro, to in ranges]
        rules_as_dict[name] = ranges

    rules = rules_as_dict
    ticket = list(map(int, ticket.split("\n")[1].split(",")))
    others = others.strip().split("\n")[1:]
    for i in range(len(others)):
        others[i] = list(map(int, others[i].split(",")))
    return rules, ticket, others

rules, my_ticket, others = parse_input(input_)

error_rate = 0
valid_others = []
for ticket in others:
    is_valid_ticket = True
    possible_fields_per_pos = []
    for number in ticket:
        possible_fields = set()
        present = False
        for field, rangelist in rules.items():
            for _range in rangelist:
                if number not in _range:
                    present |= False
                else:
                    possible_fields.add(field)
                    present |= True
        if not present:
            error_rate += number
            is_valid_ticket = False
        possible_fields_per_pos.append(possible_fields)
    if is_valid_ticket:
        valid_others.append((ticket, possible_fields_per_pos))

print("Part 1 error rate:", error_rate)

# Coalesce the possible fields
final_rule_positions = valid_others[0][1]
for ticket, rule_positions in valid_others[1:]:
    for i, candidate in enumerate(rule_positions):
        final_rule_positions[i] &= candidate

# Filter out 
already_removed = set()
while True:
    to_remove = None
    for candidate in final_rule_positions:
        if len(candidate) == 1 and list(candidate)[0] not in already_removed:
            to_remove = candidate
            break
    for i in range(len(final_rule_positions)):
        cand = final_rule_positions[i]
        if len(cand) > 1:
            final_rule_positions[i] = cand - to_remove
    
    already_removed.add(list(to_remove)[0])
    finished = True
    for candidate in final_rule_positions:
        finished &= len(candidate) < 2
    if finished:
        break

final_rule_positions = list(map(lambda s: s.pop(), final_rule_positions))

result = 1
for i in range(len(my_ticket)):
    field = final_rule_positions[i]
    if field.startswith("departure"):
        result *= my_ticket[i]
print("Part 2 result:", result)









