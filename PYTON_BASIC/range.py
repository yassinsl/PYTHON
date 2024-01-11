c = range(1,101)
print(c)
sum_even = 0
"""
for i in c :
    print(i) 
"""
for i in c :
    if i % 2 == 0 :
        sum_even += i

print(f"the sum numbers evens between 1 and 100 is {sum_even}") 