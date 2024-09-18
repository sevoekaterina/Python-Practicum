n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
for x in range(1, 1000):
    y = n - x
    if k1 * x + k2 * y == n * m:
        print(x, y)
        break 