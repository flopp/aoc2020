import sys

numbers = []
for line in sys.stdin:
    for char in line.strip():
        numbers.append(int(char))
class Cup:
    def __init__(self):
        self.n = None
        self.p = None

def create_cups(numbers):
    cups = [None]
    for i in numbers:
        cups.append(Cup())
    current = numbers[0]
    prev = numbers[-1]
    for i in numbers:
        cups[i].p = prev
        cups[prev].n = i
        prev = i
    return cups

def select_destination(current, slice, max):
    d = current - 1
    while True:
        while d in slice:
            d = d - 1
        if d >= 1:
            break
        d = max
    return d

def loop(cups, current, rounds):
    max_cup = len(cups) - 1
    for _ in range(rounds):
        slice1 = cups[current].n
        slice2 = cups[slice1].n
        slice3 = cups[slice2].n
        cups[current].n = cups[slice3].n
        cups[cups[slice3].n].p = current

        destination = select_destination(current, [slice1, slice2, slice3], max_cup)
        cups[cups[destination].n].p = slice3
        cups[slice3].n = cups[destination].n
        cups[cups[slice3].n].p = slice3
        cups[slice1].p = destination
        cups[destination].n = slice1

        current = cups[current].n

def play1(numbers, rounds):
    cups = create_cups(numbers)

    loop(cups, numbers[0], rounds)

    result = []
    c = cups[1].n
    while c != 1:
        result.append(str(c))
        c = cups[c].n
    return ''.join(result)

def play2(numbers):
    numbers2 = list(numbers)
    for i in range(10, 1_000_000 + 1):
        numbers2.append(i)
    cups = create_cups(numbers2)

    loop(cups, numbers[0], 10_000_000)

    return cups[1].n * cups[cups[1].n].n
    
print("PART1")
print(10, play1(numbers, 10))
print(100, play1(numbers, 100))

print("PART2")
print(play2(numbers))
