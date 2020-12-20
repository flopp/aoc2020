import re
import regex
import sys

rules = {}
messages = []
for line in sys.stdin:
    if m := re.match(r'^(\d+): "(.)"$', line):
        rules[m[1]] = m[2]
    elif m := re.match(r"^(\d+): ([\d ]+)$", line):
        rules[m[1]] = [m[2].split(" ")]
    elif m := re.match(r"^(\d+): ([\d ]+) \| ([\d ]+)$", line):
        rules[m[1]] = [m[2].split(" "), m[3].split(" ")]
    elif len(line) > 0:
        messages.append(line)

count_r11 = 0


def build_re(rules, rule_id, part2):
    if part2:
        global count_r11
        if rule_id == "8":
            r42 = build_re(rules, "42", part2)
            return f"(?:{r42}+)"
        if rule_id == "11":
            r31 = build_re(rules, "31", part2)
            r42 = build_re(rules, "42", part2)
            count_r11 += 1
            return f"(?P<R{count_r11}>{r42}(?&R{count_r11}){r31}|{r42}{r31})"
    rule = rules[rule_id]
    if isinstance(rule, str):
        return f"{rule}"
    sub_res = []
    for sub in rule:
        sub_res.append("".join([build_re(rules, r, part2) for r in sub]))
    return "(?:" + "|".join(sub_res) + ")"


print("PART1")
re_rules1 = "^" + build_re(rules, "0", part2=False) + "$"
print(sum([1 for message in messages if re.match(re_rules1, message)]))

print("PART2")
re_rules2 = "^" + build_re(rules, "0", part2=True) + "$"
print(sum([1 for message in messages if regex.match(re_rules2, message)]))
