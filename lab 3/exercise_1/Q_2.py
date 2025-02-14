# write a Python program to find if a given string starts with a given character using Lambda.

given_str= 'Shah Rukh Khan'

firstCharChecker =  lambda  string, first_char : string[0] == first_char

print(firstCharChecker(given_str,'S'))
print(firstCharChecker(given_str, 'N'))


