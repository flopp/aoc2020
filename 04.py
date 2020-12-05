import fileinput
import re

records = []
record = {}
re_field = re.compile(r"(...):(\S+)")
for line in fileinput.input():
    if line.strip() == "":
        records.append(record)
        record = {}
    for match in re_field.finditer(line):
        record[match[1]] = match[2]
records.append(record)

print("PART1")
required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
print(sum([required <= set(r.keys()) for r in records]))

print("PART2")
validators = {
    "byr": (r"(\d+)", lambda v: 1920 <= int(v) <= 2002),
    "iyr": (r"(\d+)", lambda v: 2010 <= int(v) <= 2020),
    "eyr": (r"(\d+)", lambda v: 2020 <= int(v) <= 2030),
    "hgt": (r"(\d+)(cm|in)", lambda v, u: (u == "in" and 50 <= int(v) <= 76) or (u == "cm" and 150 <= int(v) <= 193)),
    "hcl": (r"(#[0-9a-f]{6})", lambda v: True),
    "ecl": (r"(amb|blu|brn|gry|grn|hzl|oth)", lambda v: True),
    "pid": (r"([0-9]{9})", lambda v: True),
    "cid": (r"(.*)", lambda v: True),
}
def valid(record):
    if not (required <= set(record.keys())):
        return False
    for key, value in record.items():
        r, f = validators[key]
        if not ((m := re.fullmatch(r, value)) and f(*m.groups())):
            return False
    return True
print(sum([valid(r) for r in records]))

