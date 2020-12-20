import re
import sys


def forward(x, y, d, value):
    if d == 270:
        return x, y - value
    if d == 90:
        return x, y + value
    if d == 0:
        return x + value, y
    if d == 180:
        return x - value, y
    raise ValueError(f"bad direction: {d}")


def rotate_ship(d, value):
    return (d + 360 + value) % 360


def rotate_waypoint(x, y, d):
    if d == 0:
        return x, y
    if d == 90:
        return -y, x
    if d == 180:
        return -x, -y
    if d == 270:
        return y, -x
    raise ValueError(f"bad direction: {d}")


directions = {"E": 0, "S": 90, "W": 180, "N": 270}

nav = [
    (x[0], int(x[1]))
    for x in [re.match(r"^([A-Z])(\d+)$", line).groups() for line in sys.stdin]
]

print("PART1")
x, y, d = 0, 0, directions["E"]
for action, value in nav:
    if action in directions:
        x, y = forward(x, y, directions[action], value)
    elif action == "F":
        x, y = forward(x, y, d, value)
    elif action in ["L", "R"]:
        d = rotate_ship(d, -value if action == "L" else value)
    else:
        raise ValueError(f"bad action: {action}")
print(abs(x) + abs(y))


print("PART2")
x, y, wx, wy = 0, 0, 10, -1
for action, value in nav:
    if action in directions:
        wx, wy = forward(wx, wy, directions[action], value)
    elif action == "F":
        x += wx * value
        y += wy * value
    elif action in ["L", "R"]:
        wx, wy = rotate_waypoint(wx, wy, (360 - value) if action == "L" else value)
    else:
        raise ValueError(f"bad action: {action}")
print(abs(x) + abs(y))
