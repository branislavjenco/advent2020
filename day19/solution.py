from utils import file_into_string
import pprint

pp = pprint.PrettyPrinter(indent=2)

contents = file_into_string("day19/input_test.txt")

rules, messages = contents.split("\n\n")

rules = rules.split("\n")

rule_dict = {}
for rule in rules:
    number, rest = rule.split(":")
    if rest[1] == '"':
        val = rest[2]
        rule_dict[number] = val
    else:
        val = rest.split("|")
        rule_dict[number] = list(map(lambda x: x.strip().split(" "), val))

# print(rule_dict)


base_rule = rule_dict['0']


def visit(rd, k):
    rules = rd[k]
    if type(rules) == str:
        # print("found literal", rules)
        return rules
    elif type(rules) == list:
        # print("rules", rules)
        for i in range(len(rules)):
            rule = rules[i]
            # print("on rule", rule)
            for j in range(len(rule)):
                nt = rule[j]
                if nt != 'a' and nt != 'b':
                    t = visit(rd, nt)
                    rule[j] = t
            is_all_string = True
            for c in rule:
                if type(c) != str:
                    is_all_string = False
                    break
            if is_all_string:
                rule = "".join(rule)
            rules[i] = rule
        return rules


print("base rule", base_rule)
for i in range(len(base_rule[0])):
    t = visit(rule_dict, base_rule[0][i])
    base_rule[0][i] = t

pp.pprint(rule_dict['0'])

rule = base_rule[0]
messages = [list(m.strip()) for m in messages.strip().split("\n")]


def match(r, i, m):
    is_match = True
    new_i = i
    if type(r) == str:
        l = len(r)
        is_match = is_match & (r == "".join(m[i:i + l]))
        new_i = i + l
    elif type(r) == list:
        sub_match = False
        for x in r:
            sub_i, part_match = match(x, i, m)
            sub_match |= part_match
            if part_match:
                new_i = sub_i
        is_match &= sub_match
    return new_i, is_match


for msg in messages:
    i = 0
    is_match = True
    while i < len(msg) and is_match:
        i, is_local_match = match(base_rule[0], i, msg)
        is_match &= is_local_match
    print("MSG", "".join(msg))
    print("Match", is_match)

# literals = set()
# for k,v in rule_dict.items():
#     if type(v) == str:
#         literals.add(k)
# for k in rule_dict.keys():
#     v = rule_dict[k]
#     if type(v) == list:
#         alts = v 
#         new_alts = []
#         for seq in alts:
#             new_seq = seq
#             for l in literals:
#                 new_seq = new_seq.replace(l, rule_dict[l])
#             new_alts.append(new_seq)
#         rule_dict[k] = new_alts


# l = 1
# finished = False
# first = True
# while not finished:
#    new_messages = []
#    print("============================================")
#    for msg in messages:
#        print()
#        print("msg", "".join(msg))
#        new_msg = []
#        l = 1
#        to_add = None
#        while to_add is None:
#            for seq_start in range(0, len(msg), l):
#                seq_end = min(seq_start+l, len(msg))
#                seq = msg[seq_start:seq_end]
#                print("seq", "".join(seq))
#                to_add = None
#                for k,v in rule_dict.items():
#                    for alt in v:
#                        if alt == seq:
#                            to_add = k
#                            #print("found k" , k)
#                            break
#                    if to_add is not None:
#                        break
#            l += 1
#                    
#            if to_add is None:
#                for i in range(seq_start, seq_end):
#                    new_msg.append(msg[i])
#            else:
#                new_msg.append(to_add)
#            
#            print("new_msg", "".join(new_msg))
#        new_messages.append(new_msg)
#        if len(new_msg) == 1:
#            finished = True
#    messages = new_messages
#    if l == 2:
#        break
#    if first:
#        l += 1
#    first = False
#
#
#
#
# print(["".join(m) for m in new_messages])
#
