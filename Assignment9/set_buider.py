"""Ask the user to enter words one by one.After each entry show the current set.
   stop when the user types "Done" At the end print the total number of unique words enter"""
word_set=set()
while True:
  print("Enter word:",end="")
  word = input()
  if word == "Done":
      break
  else:
    word_set.add(word)
    print("Current Set:",word_set)
    continue
print("Total Unique Words:",len(word_set))