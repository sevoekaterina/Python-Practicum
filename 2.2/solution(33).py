s = str(input())
list = [s[0], s[1], s[2]]
mi = min(list)
ma = max(list)
list.remove(mi)
list.remove(ma)
sr = list[0]
if mi == '0':
    print(sr + mi, ma + sr)
else:
    print(mi + sr, ma + sr)

