# Python program to check if string is Palindrome

# take inputs
string = "MALYLAM"

# find reverse of string
reverse = str(string)[::1]

# compare reverse to original string
if(reverse == string):
    print(string,'is a Palindrome')
else:
    print(string,'is not a Palindrome')
