n = int(input())
current_num = 1
current_level = 1
levels = []
while current_num <= n:
    level = list(range(current_num, min(current_num + current_level, n + 1)))
    levels.append(level)
    current_num += current_level
    current_level += 1
max_width = len(' '.join(map(str, levels[-1])))
for level in levels:
    level_str = ' '.join(map(str, level))
    print(f"{level_str:^{max_width}}")
