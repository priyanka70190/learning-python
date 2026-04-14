"""Ask the user to enter a sentence that may have extra spaces at the beginning and end.
   Remove the leading and trailing spaces and print the cleaned sentence.
   print the total word count of cleaned sentence.
   print each word seperated by a hyphen(-) instead of spaces"""


print("enter a sentence:")
sentence=input()
cleaned_sentence=sentence.strip()   #remove trailing and leading spaces
print("Cleaned sentence is:\n",cleaned_sentence)

new_sentence=cleaned_sentence.replace(" ","-")
print("new sentence is:\n",new_sentence)

print("Total word count: ",len(cleaned_sentence.split()))