# Python program to check if string is Palindrome
# take inputs
string = input('Enter the string: ')

# find reverse of string
i = string
reverse = ''
while(len(i) > 0):
    if(len(i) > 0):
        a = i[-1]
        i = i[:-1]
        reverse += a

# compare reverse to original string
if(reverse == string):
    print(string,'is a Palindrome')
else:
    print(string,'is not a Palindrome')
    