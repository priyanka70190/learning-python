"""Ask the user to enter 2 words.print the letters that appear in both words(common letters)
   using sets"""

print("enter fisrt word:")
word1=input()
i=0
word1_set=set()
while i<len(word1):
    word1_set.add(word1[i])
    i=i+1

print("enter second word:")
word2=input()
j=0
word2_set=set()
while j<len(word2):
    word2_set.add(word2[j])
    j=j+1

common_letters=word1_set.intersection(word2_set)
print("common letters:",common_letters)