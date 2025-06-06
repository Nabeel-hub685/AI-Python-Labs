# (ii)Write a Python program to print a specified list after removing the 0th, 4th and 5th elements 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow',’Teapink’]
# Expected Output : ['Green', 'White', 'Black']



sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']


result = [sample_list[i] for i in range(len(sample_list)) if i not in (0, 4, 5)]


print(result)  # Expected Output: ['Green', 'White', 'Black']

