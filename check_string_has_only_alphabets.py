"""
Write a python script to check if a given string has only alphabets in it
"""

# taking input from the user
string = input("Enter a string : ")

# checking alphabets in given string
for e in string :
    if e in '0123456789' :
        print(string, "has digits in it.")
        break;
else :
    print(string,"has only alphabets in it.")