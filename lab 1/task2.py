# (ii) Write a Python program to convert temperatures to and from celsius,
# Fahrenheit.
# Formula : c/5 = f-32/9
# Expected Output :
# Enter temp in Celsius: 60°C
# Temperature in Fahrenheit is :140

a=int(input('Enter 1 to convert temperature from celcius to fahrenheit\nEnter 2 to convert temperature from fahrenheit to celcius \n'))

if(a==1):
    c= float(input("Enter temperature in celcius : "))
    f= c * (9/5) + 32
    print('Temperature in Fahrenheit is :',round(f,1))

else:
    f= float(input("Enter temperature in fahrenheit : "))
    c= (f-32)/(9/5)
    print('Temperature in Celcius is :',round(c,1))







