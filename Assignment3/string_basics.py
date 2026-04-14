"""Ask the user to enter their full name.Using String Properties
Print the following:
1 The Full Name as eneterd
2 total number of characters in the name
3 the first character of the name
4 the last character of the name"""


print("Enter your full name:")
name=input()
print("Full name:",name)

print("Total Characters including spaces:",len(name))

print("First Character of name:",name[0])
print("Last Character of name:",name[13])
