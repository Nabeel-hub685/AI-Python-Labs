# Identity Operators in Python

x = 6
if (type(x) is int): 
 print ("true") 
else: 
 print ("false")


 x = 7.2
if (type(x) is not int): 
 print ("true") 
else: 
 print ("false") 


#  Membership operator:


list1=[1,2,3,4,5] 
list2=[6,7,8,9] 
for item in list1: 
 if item in list2: 
     print("overlapping") 
else: 
     print("not overlapping")

#Floor division and Exponent and Assign

a=9
a//=3
print('floor divide=',a)
a**=5
print('exponent=',a)


#Bitwise Operaotors:

a = 60 
b = 13 
c = 0 
c = a & b 
print("Line 1", c )
c = a | b 
print("Line 2 ", c )
c = a ^ b
print("Line 3 ", c )
c = ~a 
print("Line 4", c )
c = a << 2 
print("Line 5 ", c )
c = a >> 2 
print("Line 6 -", c )

