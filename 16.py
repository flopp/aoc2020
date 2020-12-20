import re
import sys

fields = {}
your_ticket = None
nearby_tickets = []

re_field = re.compile(r"^(.+): (\d+)-(\d+) or (\d+)-(\d+)$")
re_ticket = re.compile(r"^([\d,]+)$")
re_empty = re.compile(r"^$")
re_your_ticket = re.compile(r"^your ticket:$")
re_nearby_tickets = re.compile(r"^nearby tickets:$")

state = 0
for line in sys.stdin:
    if re_empty.match(line):
        state += 1
        continue
    if state == 0:
        m = re_field.match(line)
        assert m
        fields[m.groups()[0]] = [int(x) for x in m.groups()[1:]]
    elif state == 1:
        assert re_your_ticket.match(line)
        state = 2
    elif state == 2:
        m = re_ticket.match(line)
        assert m
        assert your_ticket is None
        your_ticket = [int(x) for x in line.split(",")]
    elif state == 3:
        assert re_nearby_tickets.match(line)
        state = 4
    elif state == 4:
        m = re_ticket.match(line)
        assert m
        nearby_tickets.append([int(x) for x in line.split(",")])
    else:
        raise ValueError(f"bad state: {state}")

print("PART1")
valid_tickets = [your_ticket]
ticket_scanning_error_rate = 0
for ticket in nearby_tickets:
    is_valid = True
    for value in ticket:
        for field_ranges in fields.values():
            if (
                field_ranges[0] <= value <= field_ranges[1]
                or field_ranges[2] <= value <= field_ranges[3]
            ):
                break
        else:
            ticket_scanning_error_rate += value
            is_valid = False
    if is_valid:
        valid_tickets.append(ticket)
print(ticket_scanning_error_rate)

print("PART2")
possible_fields = [set(fields.keys())] * len(your_ticket)
for ticket in valid_tickets:
    for index, value in enumerate(ticket):
        possible = set()
        for field in possible_fields[index]:
            field_ranges = fields[field]
            if (
                field_ranges[0] <= value <= field_ranges[1]
                or field_ranges[2] <= value <= field_ranges[3]
            ):
                possible.add(field)
        possible_fields[index] = possible_fields[index].intersection(possible)

field_indexes = {}
while len(field_indexes) < len(your_ticket):
    single_field = None
    for index, possible in enumerate(possible_fields):
        if len(possible) == 1:
            for single_field in possible:
                break
            assert single_field not in field_indexes
            field_indexes[single_field] = index
            break
    assert single_field is not None
    new_possible_fields = []
    for possible in possible_fields:
        new_possible_fields.append(possible.difference(set([single_field])))
    possible_fields = new_possible_fields

product = 1
for key, index in field_indexes.items():
    if key.startswith("departure"):
        product *= your_ticket[index]
print(product)
