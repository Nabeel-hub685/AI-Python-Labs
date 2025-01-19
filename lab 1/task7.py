# iWrite a list comprehension which, from a list, generates a lowercased version of each string that has 
# length greater than five


input_list = ["Hello!", "World", "Python", "Programming", "Code"]

# Create a new list with list comprehension
new_list = [item.lower() for item in input_list if len(item) > 5]

print(new_list)  