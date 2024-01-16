size = 7  # You can adjust the size of the pattern

# Upper part of 'A'
for i in range(size):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i * 2 + 1):
        if k == 0 or k == i * 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part of 'A'
for i in range(size // 2):
    for j in range(size):
        if j == size // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
