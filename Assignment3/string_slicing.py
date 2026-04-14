"""Ask the user to enter a word.Using String Slicing only
   Print the following:
   First 3 Characters
   Last 3 Characters
   Middle Characters(excluding first and last)
   Entire word in reverse"""

print("Enter a word:")
word=input()
print("Length of word:",len(word))
print("First 3 Characters:",word[0:3])
print("Last 3 characters:",word[-3:-1])
print("last 3 charaters:",word[8:11])
print("Middle Characters:",word[1:10])
print("Reverse the word:",word[::-1])