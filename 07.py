import fileinput
import re

re_rule1 = re.compile(r'(\w+ \w+) bags contain')
re_rule2 = re.compile(r' (\d+) (\w+ \w+) bags?')
rules = {}
for line in fileinput.input():
    m1 = re_rule1.match(line)
    rules[m1[1]] = [(int(m2[1]), m2[2]) for m2 in re_rule2.finditer(line)]

print("PART1")
containers = set(["shiny gold"])
while True:
    new_containers = set(containers)
    for bag in containers:
        for bag2, contents in rules.items():
            for (_, bag3) in contents:
                if bag3 == bag:
                    new_containers.add(bag2)
    if len(new_containers) == len(containers):
        break
    containers = new_containers
print(len(containers) - 1)
                    
print("PART2")
size_cache = {}
def compute_size(bag):
    if bag in size_cache:
        return size_cache[bag]
    size = 1
    for other_count, other_bag in rules[bag]:
        size += other_count * compute_size(other_bag)
    return size
print(compute_size("shiny gold") - 1)
