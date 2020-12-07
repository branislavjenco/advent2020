import re
from utils import file_into_list

rules = file_into_list("day7/input.txt")

def part_1():
    current_candidates = {"shiny gold"}
    while True:
        prev_count = len(current_candidates)
        for rule in rules:
            children_with_counts = re.findall("(\d+) (\w+ \w+) bags?", rule)
            parent_bag = re.match("^\w+ \w+", rule).group(0)
            for count, child in children_with_counts:
                if child in current_candidates:
                    current_candidates.add(parent_bag)
        if prev_count == len(current_candidates):
            break
    return len(current_candidates)

def make_graph(rules):
    graph = {}
    for rule in rules:
        children_with_counts = re.findall("(\d+) (\w+ \w+) bags?", rule)
        parent_bag_name = re.match("^\w+ \w+", rule).group(0)
        graph[parent_bag_name] = children_with_counts
    return graph


def part_2():
    g = make_graph(rules)
    def count_bags(gr, name):
        num = 0
        children_with_counts = gr[name]
        for count, child in gr[name]:
            num = num + int(count) + int(count)*count_bags(gr, child)
        return num
    return count_bags(g, "shiny gold")

print(part_2())
        


