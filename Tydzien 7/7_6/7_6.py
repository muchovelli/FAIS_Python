import itertools
import random

binary = itertools.cycle([0, 1])
direction = iter((lambda: random.choice(("N", "S", "E", "W"))), 1)
days = itertools.cycle(["1", "2", "3", "4", "5", "6", "7"])

list_binary, list_directions, list_days = [], [], []
for i in range(20):
    list_binary.append(next(binary))
    list_directions.append(next(direction))
    list_days.append(next(days))

print(list_binary)
print(list_directions)
print(list_days)
