n = int(input())


def cn(x):
    res = 0
    s = str(x)
    for i in range(len(s)):
        res += int(s[i])
    return res


winer = ''
msm = 0
for i in range(n):
    name = input()
    num = int(input())
    sm = cn(num)
    if sm >= msm:
        msm = sm
        winer = name
print(winer)


