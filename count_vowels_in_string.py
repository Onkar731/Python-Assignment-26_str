"""
Write a python script to count vowels in a given string
"""

# taking input from the user
string = input("Enter a string : ")

# defining a count variable to store count of vowels in string
count = 0

# counting vowels in given string
for ch in string :
    if ch in 'aeiouAEIOU' :
        count += 1

# printing number of vowels
print("Vowels in string :", count)