"""
    Author: YASSINE LAHSSINI
    Date: 22/01/2024
    Time: 10:01
"""
def cipher(user_input, user_name, user_shift, length):
    result_name = ""
    for i in range(length):
        if user_input == 1:
            if user_name[i].isalpha():
                c = (ord(user_name[i]) + user_shift - ord('A'))% 26 + ord('A')
                result_name += chr(c).lower()
            else:
                result_name += user_name[i]
        elif user_input == 2:
            if user_name[i].isalpha():
                c = (ord(user_name[i]) - user_shift+ 14 - ord('A')) % 26 + ord('A')
                result_name += chr(c).lower()
            else:
                result_name += user_name[i]
    return result_name

while True:
    user_in = int(input("Please enter 1 if you want to encrypt and 2 to decrypt:\n"))
    user_msg = input("Please enter the message:\n")
    user_sh = int(input("Please enter the shift number:\n"))
    length = len(user_msg)

    result = cipher(user_in, user_msg, user_sh, length)

    if user_in == 1:
        print(f"Encrypted message is: {result}")
    elif user_in == 2:
        print(f"Decrypted message is: {result}")

    repeat = int(input("If you want to repeat this message, enter 1. Otherwise, enter 0: "))
    if repeat != 1:
        break

