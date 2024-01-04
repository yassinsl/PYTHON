"""
Author: YASSINE LAHSSINI
Date: 04/01/2024
Time: 10:04
Program: rogram that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

"""
numbers_input = input("Enter the numbers separated by commas: ")
numbers_list = numbers_input.split(",")
numbers_tuple = tuple(numbers_list)

print("Tuple is:", numbers_tuple)
print("list is:", numbers_list)
