# (i)Write a Python program to swap 4 variables values (input four values.
# Sample input:
# Before swapping
# a=2,b=56,c=78,d=9
# After Swapping
# a=,9,b=78,c=56,d=2


a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
d=int(input("Enter value of d: "))
a,d= d,a
b,c= c,b
print("a= ",a,"b= ",b,"c= ",c,"d= ",d)



