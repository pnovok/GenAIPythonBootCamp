# Challenge #1
# Write a Python script that asks the user for a number and prints a list of all its divisors for each number less than the given number.
# [Stuck? Click here to see the solution.]

# input_number = int(input("Enter a number: "))
# print(f'Let\'s find out the divisors for the {input_number}')
#
# all_divisors = list()
# for i in range(1, input_number):
#     if input_number % i == 0:
#         all_divisors.append(i)
#
# print(all_divisors)

# Challenge #2
# Write a Python program to check if an integer x is a power of another integer y. Prompt the user to input both numbers.
# Input: 16, 2
# Output: 2 ** 4 = 16
# first_number = int(input("Enter a first int: "))
# second_number = int(input("Enter a second int: "))
#
# for i in range(1, first_number):
#     if second_number ** i != first_number:
#         continue
#     else:
#         print(f'Output: {second_number} ** {i} = {first_number}')
#         break
# else:
#     print(f'The number {second_number} is not the power  {first_number}')



# Challenge #3
# Write a Python program that counts and displays the vowels of a given string, ignoring the letter case.
# Input str: Hello Everybody!
# Output: 5

# input_str = "Hello Everybody!"
#
# count = 0
# for letter in input_str.lower():
#     if letter in "aeiou":
#         count+=1
# print(count)
#
# #Another solution
# vowels = 'aeiou'
# my_str = 'Cogito, ergo sum.'
#
# count = 0
# for v in vowels:
#     if v in my_str.lower():
#         count += my_str.count(v)
#
# print(f'Total number of vowels: {count}')

# Challenge #4
# Write a Python script that checks whether a triangle is equilateral, isosceles, or scalene.
# Prompt the user to enter the lengths of the three sides.
# Triangle Types:
# Equilateral: All three sides are equal.
# Isosceles: Two sides are equal.
# Scalene: All sides are different.
# Input: Enter the lengths of the triangle sides:
# x: 6
# y: 8
# z: 12
# Output: Scalene triangle.

# first_side = int(input("Enter a first side: "))
# second_side = int(input("Enter a second side: "))
# third_side = int(input("Enter a third side: "))
#
# if first_side == second_side and first_side == third_side:
#     print("Equilateral triangle")
# elif first_side != second_side and second_side == third_side:
#     print("Isosceles Triangle")
# elif first_side == second_side and second_side != third_side:
#     print("Isosceles Triangle")
# elif first_side != second_side and first_side == third_side:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")

#Another solution
# a, b, c = input('Enter the lengths of the triangle sides [Example: 10 20 30]:').split()
# a, b, c = float(a), float(b), float(c)
# if a == b == c:
#     print("Equilateral triangle.")
# elif a == b or b == c or a == c:
#     print("Isosceles triangle.")
# else:
#     print("Scalene triangle.")

# Challenge #5
# Write a Python program that prompts the user for multiple float numbers and calculates:
# The sum
# The product
# The average
# Enter 0 to finish.

# print("Enter some floats to calculate their sum, product and average. Input 0 to exit.")
#
# count = 0
# sum = 0.0
# product = 1
#
# while True:
# 	number = float(input(''))
# 	if number == 0:
# 		break
#
# 	sum += number
# 	product *= number
# 	count += 1
#
# if count < 2:
# 	print("Inter at least two numbers.")
# else:
# 	print(f'Sum, product and average are: {sum}, {sum/count}, {product}')


# Challenge #6
# Given a string, write a program that calculates the sum and average of all digits in the string, ignoring other characters.
# Example:
# Input: "Python31py50"
# Output: Sum: 9, Average: 2.25

input_str = "Python31py50"

sum = 0
count = 0
for letter in input_str:
    if (letter.isdigit()):
        sum += int(letter)
        count += 1

print(f'Sum  and average are: {sum}, {sum/count}')

# Challenge #7
# Write a Python program that displays the multiplication table (from 1 to 10) for a number entered by the user.

n = int(input("Enter an integer number: "))

for i in range(1,11):
   print(f'{n} x {i} = {n * i}')
