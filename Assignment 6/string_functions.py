"""PROBLEM STATEMENT: Create the following 4 functions,
 each taking a sentence (string) as an argument:
count_vowels() → counts and returns the total number of vowels using a loop
count_words() → returns the total word count
longest_word() → finds and returns the longest word in the sentence using a loop
reverse_words() → returns the sentence with the word order reversed
Ask the user to enter a sentence. Call all 4 functions and print the results.
 Commit the changes of the file and Push to Github."""

def reverse_words(sentence):
    sentence1 = sentence.split(" ")
    r_w=sentence1[::-1]
    r_w_sentence = " ".join(r_w)
    return r_w_sentence

def count_words(sentence):
    sentence1 = sentence.split(" ")
    count_words=len(sentence1)
    return count_words

def count_vowels(sentence):
    i=0
    for letters in sentence:
        if ("a" ==letters or "e" ==letters or "i"==letters or "o"==letters or "u"==letters
                or "A"==letters or "E"==letters or "I"==letters or "O"==letters or "U" == letters):
            i=i+1
    return i

def longest_word(sentence):
    sentence1 = sentence.split(" ")
    max=0
    for words in sentence1:
        length=len(words)
        if length>max:
            max=length
            longest_word=words
    return longest_word



print("enter a sentence:")
sentence = input()
r_w_sentence = reverse_words(sentence)
print("Reversed Sentence :",r_w_sentence)

count_words=count_words(sentence)
print("Word Count :",count_words)

vowel_count=count_vowels(sentence)
print("Vowel Count :",vowel_count)

longest_word=longest_word(sentence)
print("Longest Word :",longest_word)