# Challenge 1
#Write a Python script that removes all occurrences of a given element from a list.

my_list = [1, 2, 3, 2, 2, 5]
#print(my_list)

#My Solution
def remove_element(a,b):
    a = [n for n in a if n != b]
    #a.remove(b)
    print(a)

remove_element(my_list, 2)

# item to remove from the list
n = 2
while n in  my_list:
    my_list.remove(n)

print(my_list)

#Challenge 2
#Write a Python script that removes all duplicate elements from a list.
my_list2 = [1, 2, 3, 2, 2, 5]

def remove_duplicates(a):
    unique_list = []
    for item in a:
        if item not in unique_list:
            unique_list.append(item)
    print(unique_list)

remove_duplicates(my_list2)

#Challenge 3
#Given the string nums = '10,20,30,40,50', write a Python script that converts it into a list of integers: [10, 20, 30, 40, 50].

nums = ['10,20,30,40,50']
new_nums = []

def convert_func(a):
    nums2 = a[0].split(',')
   #print(nums2)
    for item in nums2:
        new_nums.append(int(item))
    print(new_nums)

print(nums)

convert_func(nums)

# Udemy Solution
nums = '10,20,30,40,50'
nums_list = nums.split(',')
print(nums_list)  # => ['10', '20', '30', '40', '50']

nums1 = [int(n) for n in nums_list]
print(nums1)    # => [10, 20, 30, 40, 50]

#Challenge #4
#Write a Python script that finds all numbers between 1500 and 3200 (inclusive) that are divisible by 7 but not multiples of 5.
#Print the results as a comma-separated sequence on a single line.

result = []
for i in range(1500, 3200):
    if i % 7 == 0:
        if i % 5 != 0:
            result.append(str(i))

print(','.join(result))

#Challenge #5
#Write a program that prompts the user for a string containing multiple words separated by spaces and prints the words in reverse order.

user_string = input("Please enter a string: ")
print("You entered:", user_string)

my_list3 = user_string.split()
print(my_list3)
print(my_list3[::-1])


#Challenge #6

#Write a Python program that takes a hyphen-separated sequence of words as input and prints them in alphabetical order, maintaining the hyphen separation.

text_str = "hello-my-world-of-python-awesome"
print(text_str)
print(text_str)
my_list4 = text_str.split('-')
my_list4.sort()
separator = "-"
new_test_str = separator.join(str(item) for item in my_list4)
print(new_test_str)

#Challenge #7
#Write a Python program that takes a sequence of words separated by spaces and prints the words with their letters reversed. Do not use list comprehension.

text_str2 = "I love cats and dogs"
my_list6 = text_str2.split()
new_my_list6 = list()
print(my_list6)

for item in my_list6:
    new_my_list6.append(item[::-1])

print(new_my_list6)


#Challenge #8

# Write a Python program that accepts a hyphen-separated sequence of words as input and prints
# the words in a hyphen-separated sequence after sorting them alphabetically.


string = input("Enter a few words separated by whitespaces: ")
words = string.split()

# reverse the letters in each word
words = [w[::-1] for w in words]

new_str = ' '.join(words)

print(new_str)

#Challenge #9

#Given a list of words, write a Python script that generates a list of tuples where each tuple contains a word and its length. Use list comprehension if possible.

words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

def produce_tuples(words):
    tuples = []
    for word in words:
        tuples.append((word, len(word)))
    print(tuples)

produce_tuples(words)
