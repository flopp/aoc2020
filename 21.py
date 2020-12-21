import re
import sys

re_line = re.compile(r'^([a-z ]+) \(contains ([a-z ,]+)\)$')

foods = []
possible_containers = {} # allergen -> set(food)
for line in sys.stdin:
    m = re_line.match(line)
    ingredients = set(m[1].split(" "))
    allergens = m[2].split(", ")
    foods.append((ingredients, allergens))
    for allergen in allergens:
        if allergen in possible_containers:
            possible_containers[allergen] = possible_containers[allergen].intersection(ingredients)
        else:
            possible_containers[allergen] = set(ingredients)

definitive_containers = {}
definitive_allergens = {}
while len(definitive_containers) < len(possible_containers):
    for allergen, ingredients in possible_containers.items():
        if len(ingredients) == 1:
            ingredient = ingredients.pop()
            definitive_containers[allergen] = ingredient
            definitive_allergens[ingredient] = allergen
            for allergen2, ingredient2 in possible_containers.items():
                ingredient2.discard(ingredient)
print(definitive_containers)

print("PART1")
count = 0            
for ingredients, _ in foods:
    count += sum(1 for ingredient in ingredients if ingredient not in definitive_allergens)
print(count)

print("PART2")
print(','.join([definitive_containers[allergen] for allergen in sorted(list(definitive_containers))]))
    
        


