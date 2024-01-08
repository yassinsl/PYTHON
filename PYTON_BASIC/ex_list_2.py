my_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

cols = int(input("Please enter the index of column: "))
rows = int(input("Please enter the index of row: "))

my_list[cols - 1][rows  - 1] = 'X'
print(my_list)
