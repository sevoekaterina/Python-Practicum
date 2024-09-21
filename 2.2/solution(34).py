a = str(input())
b = str(input())

list = [a[0], a[1], b[0], b[1]]
mi = min(list)
ma = max(list)
list.remove(mi)
list.remove(ma)
su = int(list[0]) + int(list[1])
su = str(su)[-1]
print(ma + su + mi)