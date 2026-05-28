"""Create a simple phonebook program.Allow the user to :
1.Add a contact(name and number)
2 search for a contact by a name
3. Delete a contact
4. display all contacts
5.Exit
"""


print("Menu:")
print("1. Add a contact")
print("2. Search for a contact")
print("3. Delete a contact")
print("4. Display all contacts")
print("5. Exit")
dict1={}
while True:
 print("Enter your option:")
 option=int(input())

 if option==1:
    print("Enter Name:")
    name=input()
    print("Enter number:")
    number=input()
    dict1[name]=number
    print("contact Added")
 elif option==2:
    print("Enter name to search:")
    name1=input()
    for name in dict1.keys():
        if name==name1:
            print(name,":",dict1[name])
 elif option==3:
     print("Enter the contact name to be deleted:")
     name2=input()
     for name in list(dict1.keys()):
        if name==name2:
            del dict1[name]
     print("contact Deleted")
 elif option==4:
     for name,number in dict1.items():
         print(name,":",number)


 elif option==5:
       print("Goodbye")
       break

