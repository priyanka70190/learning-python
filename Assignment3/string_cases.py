"""Ask the user to enter a sentence.Using String Methods to print the sentence in the following format
 1 All Uppercase
 2 All Lowercase
 3 Title Case(First letter of every word Capitilize
 4 Sentence case (only first letter of the sentence should capitilize)"""


print("Enter a sentence:")
str=input()
upperstring=str.upper()
print("Upper Case: ",upperstring)

lowerstring=str.lower()
print("Lower Case:",lowerstring)

sentencecase=str.capitalize()
print("Sentence Case: ",sentencecase)

titlecase=str.title()
print("Title case:",titlecase)
