nums = [2, 4, 6, 9]
k = 3
cur_list = {}
chains = []

for a in nums:
    if a - k in cur_list:
        cur_list[a - k].append(a)
        cur_list[a] = cur_list.pop(a - k)
    else:
        cur_list[a] = [a]
        chains.append(cur_list[a])

print(chains)
