import at
x = {}
with open("score.txt", "r") as f:
    x = at.load(f)

print(x)