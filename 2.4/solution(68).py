n = int(input())
res = ''
for _ in range(n):
    mm = '0'
    for i in range(len(s := input())):
        mm = max(mm, s[i])
    res += mm
print(res)