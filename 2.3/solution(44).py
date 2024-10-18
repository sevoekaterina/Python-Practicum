summ = 0
while (x := float(input())) != 0:
    if x >= 500:
        summ += x * 0.9
    else:
        summ += x
print(summ)
