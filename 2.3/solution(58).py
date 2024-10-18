aa = [i for i in range(1, 1001)]
st = -1
end = 1000
mm = (st + end) // 2
print(aa[mm])
while ((s := input()) != 'Угадал!'):
    if s == 'Меньше':
        end = mm
    if s == 'Больше':
        st = mm
    mm = (st + end) // 2
    print(aa[mm])