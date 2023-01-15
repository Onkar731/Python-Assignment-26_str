"""
Write a python script to count words in a given string
"""

# taking input from the user
string = input("Enter a string of multiple words : ")

# defining a count variable to store number of words present in a string
count = len(string.split(' '))

# printing number of words in a given string
print(string, "has", count, "words")