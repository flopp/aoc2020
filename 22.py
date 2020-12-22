import sys

p1 = True
player1 = []
player2 = []
for line in sys.stdin:
    if line in ["\n", "Player 1:\n"]:
        pass
    elif line == "Player 2:\n":
        p1 = False
    else:
        (player1 if p1 else player2).append(int(line.strip()))

def play1(cards1, cards2):
    while len(cards1) > 0 and len(cards2) > 0:
        card1, card2 = cards1.pop(0), cards2.pop(0)
        if card1 > card2:
            cards1.extend([card1, card2])
        else:
            cards2.extend([card2, card1])
    return len(cards1) > 0

def play2(cards1, cards2):
    seen = set()
    while len(cards1) > 0 and len(cards2) > 0:
        key = f"{'-'.join([hex(c) for c in cards1])} {'-'.join([hex(c) for c in cards2])}"
        if key in seen:
            return True
        seen.add(key)
        card1, card2 = cards1.pop(0), cards2.pop(0)
        if card1 > len(cards1) or card2 > len(cards2):
            if card1 > card2:
                cards1.extend([card1, card2])
            else:
                cards2.extend([card2, card1])
        else:
            if play2(cards1[:card1], cards2[:card2]):
                cards1.extend([card1, card2])
            else:
                cards2.extend([card2, card1])
    return len(cards1) > 0  

def score(cards):
    return sum(i * card for i, card in zip(range(len(cards), 0, -1), cards))

print("PART1")
cards1 = list(player1)
cards2 = list(player2)
print(score(cards1 if play1(cards1, cards2) else cards2))

print("PART2")
cards1 = list(player1)
cards2 = list(player2)
print(score(cards1 if play2(cards1, cards2) else cards2))
