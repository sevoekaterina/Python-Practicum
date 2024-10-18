def pr(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return x > 1


ans = 0
for i in range(n := int(input())):
    if pr(int(input())):
        ans += 1

print(ans)
