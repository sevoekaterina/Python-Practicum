s1 = str(input())
s2 = str(input())
s3 = str(input())
if (('зайка' in s1) + ('зайка' in s2) + ('зайка' in s3)) > 1:
    list = [s1, s2, s3]
    mi = min(list)
    if 'зайка' in mi:
        print(mi, len(mi))
    else:
        list.remove(mi)
        print(min(list), len(min(list)))
else:
    if 'зайка' in s1:
        print(s1, len(s1))
    if 'зайка' in s2:
        print(s2, len(s2))
    if 'зайка' in s3:
        print(s3, len(s3))
