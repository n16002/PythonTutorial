import random
x = {}
with open("score.txt", "r") as f:
    x = random.load(f)

print(x)