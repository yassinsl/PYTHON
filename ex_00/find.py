find_num = []
for i in range(1500, 2700):
    if i % 5 == 0 and i % 7 == 0:
        find_num.append(str(i))

find_n = ','.join(map(str, find_num))
print(find_n)
