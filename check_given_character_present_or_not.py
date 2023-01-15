"""
Write a python script to check if a given character is present in a given string or not
"""

# taking input from the user - character and a string
string = input("Enter a string : ")
character = input("Enter a character to search in given string : ")

# checking given character is present in string or not
if character in string :
    print(character, "is present in string.")
else :
    print(character, "is not present in string.")