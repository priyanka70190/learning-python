"""Create a dictionary & take input from user and
assume user will give input word that is in our dictionary
& return the meaning of that word from the dictionary"""


dict={"Food":"somethong we eat to live",
      "Rain":"water falling from clouds",
      "Home":"A Place where we live",
      "Fish":"A Animal that lives in water"}
print("Enter a word From these words to know the meaning\n 1 Food\n 2 Rain\n 3 Home\n 4 Fish ")
word=input()
print("Meaning of this word is: ",dict.get(word))
