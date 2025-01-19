# Write a Python program to count the number of strings where the string length is 2 or more and the 
# first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2.


size = int(input("Enter size of the list: "))
sampleList=[None]*size # in this way we can declare a list with certain size
print("Enter the list elements one by one: ")
for i in range(0,size):
    sampleList[i]=input("Enter: ")
    
print(sampleList)
count=0

for i in sampleList:
    if(len(i)>=2 and i[0]==i[-1]):
        count=count+1

print("So the total count is:",count)        
        