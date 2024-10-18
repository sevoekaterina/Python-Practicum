n = int(input())


def palendron(n):
    str_n = str(n)
    return str_n == str_n[::-1]


ans = 0

for _ in range(n):
    num = int(input())
    if palendron(num):
        ans += 1

print(ans)