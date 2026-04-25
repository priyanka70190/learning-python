#Simulate a restaurant Ordering System
#Display a fixed menu of 5 items with prices
#Ask the user to keep entering item numbers and quantities until they enter '0','end' or'done' to finish.
#Apply GST based on the order total.
#print a full bill at the end.
#Menu:
# A. Burger -->120 rs
# B. Pizza --> 250 rs
# C. Pasta -->180 rs
# D. Cold Drink -->60 rs
# E. Ice Cream -->90 rs
#GST criteria:
#.Total above 1000 -->18% GST
#.Total above 500 --> 12 % GST
# 500 or below -->5% GST


print("Menu:")
print("A. Burger -->120 rs\nB. Pizza -->250 rs\n C. Pasta -->180 rs\n D. Cold Drink -->60 rs \n E. Ice Cream -->90 rs")
dict1={}
while(True):
    print("Enter item number(1 to 5): ")
    item=input()
    if(item =="0" or item=="end" or item=="done"):
        break
    else:
        print("Enter Quantity: ")
        quantity=int(input())
    dict1.update({item:quantity})

dict2={"1":"Burger","2":"Pizza","3":"Pasta","4":"Cold Drink","5":"Ice Cream"}

dict3={"1":120,"2":250,"3":180,"4":60,"5":90}
sum=0
print(40*"-")
print("Restraunt Bill")
print(40*"-")
for key in dict1:
   if(key in dict2):
       print(dict2[key],end=" ")
       if(key in dict3):
           print(dict3[key],end=" ")
           print("*",dict1[key]," = ",dict3[key]*dict1[key])
           sum+=dict3[key]*dict1[key]
       continue


print(40*"-")
print("SubTotal=",sum)
if(sum>1000):
    gst=18/100*sum
    print("GST(18%)",gst)
    total=sum+gst
    print("Total=",total)
elif(sum>500):
    gst=12/100*sum
    print("GST(12%): ",gst)
    total=sum+gst
    print("Total=",total)
elif(sum<=500):
    gst=5/100*sum
    print("GST(5%): ",gst)
    total=sum+gst
    print("Total=",total)

print(40*"-")
print("Thank you for Dining with us...!")
print(40*"-")