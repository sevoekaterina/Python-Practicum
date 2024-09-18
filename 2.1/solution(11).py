s = str(input())
k = str(input())
while len(k) < 3:
    k = '0' + k
while len(s) < 3:
    s = '0' + s
res = str(int(s[0]) + int(k[0]))[-1] + str(int(s[1]) + int(k[1]))[-1] + str(int(s[2]) + int(k[2]))[-1]
print(res)