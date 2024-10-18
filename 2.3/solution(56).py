s = input()
res = ''
for i in range(len(s)):
    if int(s[i]) % 2 == 1:
        res += s[i]
print(res)