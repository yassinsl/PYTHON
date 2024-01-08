my_list =[[" ✔ ",  " ✔ ",  " ✔ "], [ " ✔ ",  " ✔ ", " ✔ "], [" ✔ ", " ✔ ", " ✔ "]]

cols = int(input("Please enter the index of column: "))
rows = int(input("Please enter the index of row: "))

my_list[cols - 1][rows  - 1] = " ✖ "
print(my_list)
