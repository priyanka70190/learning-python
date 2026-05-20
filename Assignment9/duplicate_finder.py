"""Ask the user to enter a list of words seprated by spaces .Using a set,idientify and
print the words that appear more than once(duplicates)"""

print("Enter words:",end=" ")
words=input()
words_strings=words.split(" ")
words_set=set()
duplicate_words_set=set()
for word in words_strings:
    if word in words_set:
        duplicate_words_set.add(word)
    else:
        words_set.add(word)

print("duplicate words:",duplicate_words_set)