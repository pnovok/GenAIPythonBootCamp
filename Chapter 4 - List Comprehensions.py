#List Comprehensions

#Old way of doing things
clicks = [10,5,15,20]

doubled_clicks = []

for c in clicks:
    doubled_clicks.append(c*2)

print(doubled_clicks)

# New way [expression for item in iterable]

doubled_clicks = [c*2 for c in clicks]
print(doubled_clicks)

contributors = ['alice', 'Bob', 'CHARLIE']
formatted_names = [name.capitalize() for name in contributors]
print(formatted_names)

# [expression for item in iterable if condition]
nums = [1,7,8,14,21,30,50]
divisible_by_seven =  [n for n in nums if n %7 == 0]
print(divisible_by_seven)

# Shared elements from multiple lists
ai_team = ['Alice', 'Bob', 'Charlie']
data_team = ['Alice', 'David', 'Charlie']
shared_skills = [name for name in ai_team if name in data_team]
print(shared_skills)