"""Ask the user to enter a sentence.Ask the user to enter a word to search for.
   using string methods,print the following
   whether the sentence starts with the searched word(true/false)
    whether the sentence ends with the searched word(true/false)
    the index position where the word first appears in the sentence
    the total number of times the word appears in the sentence"""



print("enter the sentence")
sentence = input()
print("enter a word to search:")
word=input()
print("Starts with "+word+" ",sentence.startswith(word))
print("Ends with "+word+" ",sentence.endswith(word))
print("total number of times the word appears: ",sentence.count(word))
print("the index position where the word first appears: ",sentence.find(word))