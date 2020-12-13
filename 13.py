import math
import sys

earliest_departure_time = -1
buses = []
for index, line in enumerate(sys.stdin):
    if index == 0:
        earliest_departure_time = int(line)
    else:
        buses = [(int(token), offset) for offset, token in enumerate(line.split(',')) if token != 'x']


print("PART1")
min_wait = None
min_bus_id = None
for bus_id, offset in buses:
    wait = bus_id - (earliest_departure_time % bus_id)
    if min_wait is None or wait < min_wait:
        min_wait = wait
        min_bus_id = bus_id
print(min_wait * min_bus_id)


print("PART2")
def lcm(a, b):
    return a * b // math.gcd(a, b)

jump = 1
t = 0
for bus_id, offset in buses:
    while (t + offset) % bus_id != 0:
        t += jump
    jump = jump * bus_id // math.gcd(jump, bus_id) # lcm
print(t)
