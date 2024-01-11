import random
import string
symbols = "!@#$%^&*()_+[]{|};:,.<>?/"
num_letters = int(input("Enter the number of random letters you want: "))
num_symbols = int(input("Enter the number of random symbols you want: "))
num_digits = int(input("Enter the number of random digits you want: "))

random_letters = ''.join(random.choice(string.ascii_letters) for _ in range(num_letters))
random_symbols = ''.join(random.choice(symbols) for _ in range(num_symbols))
random_digits = ''.join(random.choice(string.digits) for _ in range(num_digits))
pasword =' '.join ([str(random_digits) + random_symbols + random_letters])
print(pasword)
#print(f"pasword is : {random_letters}{random_digits}{random_symbols}")
