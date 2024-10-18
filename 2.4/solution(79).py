n = int(input())


def sum_di_in_base(num, base):
    ans = 0
    while num > 0:
        ans += num % base
        num //= base
    return ans


max_sum = -1
best_base = 2
for base in range(2, 11):
    digt_sum = sum_di_in_base(n, base)
    if digt_sum > max_sum:
        max_sum = digt_sum
        best_base = base
print(best_base)
