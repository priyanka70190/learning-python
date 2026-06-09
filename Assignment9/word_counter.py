"""Ask the user to enter a sentence.Count how many times each word appears
and store the result in a dictionary.print the word counts"""

print("Enter a sentence:")
sentence = input()
words_array=sentence.split(" ")
dict1={}
i=0
while i<len(words_array):
    count=0
    j=0
    while j<len(words_array):

       if words_array[i] == words_array[j]:
         count+=1
       j=j+1
    dict1[words_array[i]]=count
    i=i+1

for key,value in dict1.items():
    print(key,":",value)

