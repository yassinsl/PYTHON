tuple_0 = (1, 2, 3, 4,81,45,100,2)
tuple_1 = (1,"yassin",True,10.01)
i = 0

while i < len(tuple_0) :
    print(tuple_0[i])
    i = i + 1

print("#"*45)

print(min(tuple_0))
print(max(tuple_0))

c = tuple_0.index(3)
print(f"index is {c}")

d = tuple_0.count(2)
print(f"count is {d}" )

tuple_2 = (tuple_0, tuple_1)
length = len(tuple_2)
print(f"length is {length}")

tuple_3 = tuple_0 + tuple_1
print(tuple_3)
print(len(tuple_3))
