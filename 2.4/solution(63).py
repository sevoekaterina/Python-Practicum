def cs(n):
    s = str(n)
    res = 0
    for i in range(len(s)):
        res += int(s[i])
    return res


n = int(input())
a = []
res = 0
for i in range(n):
    a.append(int(input()))
for x in a:
    res += cs(x)
print(res)