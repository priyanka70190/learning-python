""" Ask the user to enter a sentence. Using String Methods only.
    Print following analysis:
    1 The words with all extra spaces between words removed
     2 total number of characters excluding spaces
     3 the sentence reversed word by word(first split,reverse using slicing,then join
     4 whether the sentence is same forwards and backwards -i.e a palindrome (true or false)
        ignore spaces and capitilization"""

# remove extra space between words
print("enter any  sentence")
sentence=input()
sentence1=sentence.split()
print(sentence1)
cleaned_sentense=" ".join(sentence1)
print(cleaned_sentense)

#total number of characters excluding space
nospace_sentense="".join(sentence1)
print("Chracters count with out spaces: ",len(nospace_sentense))

#sentence reverse word by word

reverse_sentence=sentence1[::-1]
print("Reverse sentence: "," ".join(reverse_sentence))

#palindrome
r_s=nospace_sentense[::-1]
print("String is palindrome: ",nospace_sentense==r_s)
