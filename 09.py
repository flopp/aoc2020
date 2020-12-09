import sys

preamble_length = int(sys.argv[1])
numbers = [int(line) for line in sys.stdin]

def is_valid(n, previous):
    for a in previous:
        for b in previous:
            if a != b and n == a + b:
                return True
    return False

print("PART1")
invalid_number = -1
for index, invalid_number in enumerate(numbers[preamble_length:]):
    if not is_valid(invalid_number, numbers[index:index+preamble_length]):
        break
print(invalid_number)

def find_range(range_sum, numbers):
    for index in range(len(numbers)):
        for length in range(len(numbers)):
            s = sum(numbers[index:index+length])
            if s == range_sum:
                return min(numbers[index:index+length]) + max(numbers[index:index+length])
            elif s > range_sum:
                break
    return -1

print("PART2")
print(find_range(invalid_number, numbers))
