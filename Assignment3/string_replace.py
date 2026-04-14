"""Ask the user to enter a sentence .
   Ask the user to enter a word that they want to replace
   Ask the user to enter the new word.
   Replace the old word with the new word
   and print the updated sentence.
   also print the total number of times the old word appereaed in the original sentence"""


print("enter a sentence: ")
sentence=input()
print("enter word to replace:")
old_word=input()
print("enter new word:")
new_word=input()
print("updated sentence:\n")
sentence1=sentence.replace(old_word,new_word)
print(sentence1)
print("total number of times the old word appeared",sentence.count(old_word))
