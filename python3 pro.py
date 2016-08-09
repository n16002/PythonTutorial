"""W, H, x, y, r = [int(i) for i in input().split()]
if (x - r) >= 0 and (x + r) <= W:
    if (y - r) >= 0 and (y + r) <= H:
        print("Yes")
    else:
        print("No")
else:
    print("No")
    """
"""
data = [
    [[0 for r in range(10)] for f in range(3)] for b in range(4)
]

count = int(input())
for c in range(count):
    b, f, r, v = [int(i) for i in input().split()]
    data[b-1][f-1][r-1] += v


for bi, b in enumerate(data):
    for f in b:
        for r in f:
            print(' {0}'.format(r), end='')

        print()

    if bi < 3:
        print('#' * 20)
"""
"""
(n, m) = [int(i) for i in input().split()]
A = []
b = []
for i in range(n):
    A.append([int(j) for j in input().split()])

for i in range(m):
    b.append(int(input()))

for i in range(n):
    s = 0
    for j in range(m):
        s += A[i][j] * b[j]
    print(s)
"""
"""
while True:
    m, f, r = [int(i) for i in input().split()]
    if m == f == r ==-1:
        break
    if m == -1 or f == -1 or m + f < 30:
            print('F')
        elif m + f >= 80:
            print('A')
        elif m + f >= 65:
            print('B')
        elif m + f >= 50:
            print('C')
        elif m + f >= 30:
            print('C' if r >= 50 else 'D')
"""
"""
while True:
    n, x = map(int, input().split())
    if n == x == 0:
        break

    result = 0
    for a in range(1, x // 3):
        for b in range(a + 1,  x // 2):
            c = x - a - b
            if b < c <= n:
                result += 1
    print(result)
"""

