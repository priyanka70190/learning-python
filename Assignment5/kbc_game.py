"""PROBLEM STATEMENT: Simulate the famous "Kaun Banega Crorepati (KBC)" game show.
 Create a quiz with 15 questions, each having 4 options (A, B, C, D).
 If the player answers incorrectly, the game ends and they walk away with their last safe milestone amount.
There are 2 safe milestones — at question 5 (₹10,000) and question 10 (₹3,20,000).
After each correct answer, ask the player "Lock kar diya jaaye? (Y/N)" — if they choose Y,
the answer is locked and checked. After completing all 15 questions correctly,
declare them the winner of ₹1 Crore.
Prize Money Ladder:
Question
Prize Money
1
₹1,000
2
₹2,000
3
₹3,000
4
₹5,000
5 ✅ Safe
₹10,000
6
₹20,000
7
₹40,000
8
₹80,000
9
₹1,60,000
10 ✅ Safe
₹3,20,000
11
₹6,40,000
12
₹12,50,000
13
₹25,00,000
14
₹50,00,000
15 🏆
₹1,00,00,000
Rules:
Player must enter their name at the start.
Each question has 4 options: A, B, C, D.
After entering an answer, ask "Lock kar diya jaaye? (Y/N)"
If N → allow the player to change their answer.
If Y → lock and check the answer.
If the answer is correct → move to the next question and show updated prize.
If the answer is wrong → game ends, player walks away with the last safe milestone amount.
If the player quits mid-game by entering Q → they walk away with the last safe milestone amount.
Safe milestones: Question 5 → ₹10,000 | Question 10 → ₹3,20,000.
After all 15 correct answers → declare the player as KBC Crorepati.

EXAMPLE:

🎬 Welcome to Kaun Banega Crorepati! 🎬
Enter your name: Alia Bhatt

Namaste, Alia Bhatt! Are you ready to play KBC?
Let's start!

------------------------------------------------------------
Question 1 for ₹1,000
------------------------------------------------------------
Which planet is known as the Red Planet?
A. Venus
B. Jupiter
C. Mars
D. Saturn
------------------------------------------------------------
Enter your answer (A/B/C/D) or Q to quit: C
Lock kar diya jaaye? (Y/N): N
Enter your answer (A/B/C/D) or Q to quit: C
Lock kar diya jaaye? (Y/N): Y

✅ Correct! Alia Bhatt, aapne jeete ₹1,000!

------------------------------------------------------------
Question 2 for ₹2,000
------------------------------------------------------------
How many bones are in the adult human body?
A. 206
B. 212
C. 195
D. 230
------------------------------------------------------------
Enter your answer (A/B/C/D) or Q to quit: A
Lock kar diya jaaye? (Y/N): Y

✅ Correct! Alia Bhatt, aapne jeete ₹2,000!

... (questions 3 and 4 answered correctly) ...

------------------------------------------------------------
Question 5 for ₹10,000 🔒 SAFE ZONE
------------------------------------------------------------
Who wrote the national anthem of India?
A. Bankim Chandra Chatterjee
B. Rabindranath Tagore
C. Sarojini Naidu
D. Mahatma Gandhi
------------------------------------------------------------
Enter your answer (A/B/C/D) or Q to quit: B
Lock kar diya jaaye? (Y/N): Y

✅ Correct! Alia Bhatt, aapne jeete ₹10,000!
🔒 ₹10,000 is now your safe amount!

... (questions 6 to 9 answered correctly) ...

------------------------------------------------------------
Question 10 for ₹3,20,000 🔒 SAFE ZONE-2
------------------------------------------------------------
What is the capital of Australia?
A. Sydney
B. Melbourne
C. Canberra
D. Brisbane
------------------------------------------------------------
Enter your answer (A/B/C/D) or Q to quit: A
Lock kar diya jaaye? (Y/N): Y

❌ Wrong Answer! The correct answer was C. Canberra.

------------------------------------------------------------
💔 Game Over, Alia Bhatt!
You answered incorrectly at Question 10.
Your safe amount was: ₹10,000
You walk away with: ₹10,000
------------------------------------------------------------"""

print("🎬 Welcome to Kaun Banega Crorepati! 🎬")
print("Enter your name :")
name = input()
print("Namaste, ", name," Are you ready to play KBC?")
print("Lets start!")
dict1={1:"what is the capital of india? \nA:Mumbai\nB:New Delhi\nC:KolKata\nD:Chennai",
       2:"Which Planet is Known as red Planet? \nA:Earth\nB:Venus\nC:Mars\nD:Jupiter",
       3:"What is 5+7? \nA:10\nB:11\nC:12\nD:13",
       4:"what is 2+2?\nA:3\nB:4\nC:5\nD:6",
       5:"Which Color is the sky?\nA:Green\nB:Blue\nC:Red\nD:Yellow",
       6:"How many Days are in a week?\nA:5\nB:6\nC:7\nD:8",
       7:"Which animal says Meow?\nA:Dog\nB:Cat\nC:Cow\nD:Lion",
       8:"What is 5*2?\nA:7\nB:10\nC:12\nD:15",
       9:"Which Fruit is Yellow?\nA:Apple\nB:Banana\nC:Grapes\nD:Orange",
       10:"How many legs does a dog have?\nA:2\nB:3\nC:4\nD:5",
       11:"Which shape has 4 sides?\nA:Circle\nB:Triangle\nC:Square\nD:Oval",
       12:"What do we drink to stay hydrated?\nA:Juice\nB:Milk\nC:Water\nD:Tea",
       13:"Which planet do we live on?\nA:Mars\nB:Venus\nC:Earth\nD:Jupitor",
       14:"What is 10 - 3?\nA:6\nB:7\nC:8\nD:9",
       15:"Which bird can fly?\nA:Penguin\nB:Ostrich\nC:Sparrow\nD:Hen"
       }

dict2={1:1000,2:2000,3:3000,4:5000,5:10000,6:20000,7:40000,8:80000,9:160000,10:320000,11:640000,
       12:1250000,13:2500000,14:5000000,15:10000000}
dict3={1:"B",2:"C",3:"C",4:"B",5:"B",6:"C",7:"B",8:"B",9:"B",10:"C",11:"C",12:"C",13:"C",14:"B",15:"C"}
i=1
amount=0
for key in dict1:
 print(40*"-")
 print("Question",i," for ",dict2[i],"rs")
 print(40*"-")
 print(dict1[i])
 print(40*"-")
 print("Enter your answer (A/B/C/D) or Q to quit: ")
 answer = input()
 print("Lock kar diya jaaye? (Y/N): ")
 lock=input()
 if(lock=="N"):
  print("Enter your answer (A/B/C/D) or Q to quit: ")
  answer = input()
  print("Lock kar diya jaaye? (Y/N): ")
  lock=input()
 elif(lock=="Y"):
     if(answer==dict3[i]):
         print("✅ Correct!", name, "aapne jeete ",dict2[i]," rs!")
         amount=dict2[i]
     elif(answer == "Q"):
         if(amount == 10000 or amount == 320000):
             safeamount = amount
         else:
             safeamount = 0
         print("💔 Game Over, ", name, "!", "\nYoy Quit Game at Question", i,
               "\nYour safe amount was: ", safeamount, "\nYou walk away with: ₹", safeamount
               )
         break
     else:
         if (amount == 10000 or amount == 320000):
             safeamount = amount
         else:
             safeamount = 0
         print("💔 Game Over, ", name, "!", "\nYou answered incorrectly at Question", i,
               "\nYour safe amount was: ", safeamount, "\nYou walk away with: ₹", safeamount
               )
         break

 i=i+1