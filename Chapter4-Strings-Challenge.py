# Challenge 1

revenue = 45897513
margin = 12.7
profit = f'{revenue*margin/100:.2f}'


print(f'Companys profit is  ${profit}')

#Challenge 2

my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

print(my_str[32:])
print(my_str.split() [-1])

print(my_str[-1:-18:-1])

#Challenge 3
print('It Displayed \"You\'ve got an error!\"')

#Challenge 4
# value_in_feet = input('Enter a value in feet ...\n')
# value_in_cm = int(value_in_feet) * 30.48
# print (f'Value in cm is {value_in_cm:.2f} cm')

#Challenge 5
input_word = input('Enter a word ...\n')
if (input_word == input_word[::-1]):
    print(f'The word {input_word} is Palindrome')
else:
    print(f'The word {input_word} is not Palindrome')

