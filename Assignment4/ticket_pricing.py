"""A cinema charges ticket prices based on age group and day of the week.
 Ask the user to enter their age and the day of the week.
 determinine the ticket price based on the following rules:
 Age Groups:
  12 and below--->child
  13 to 59 -->adult
  60 and above -->senior
 Pricing Rules:
  weekday(Monday to friday)
  child-->5$
  Adult -->10$
  Senior -->7$
  Weekend(Saturday or Sunday)
   child -->8$
   Adult -->15$
   Senior -->10$
if the users enters an invalid day,print an error message
 """
print("Enter your Age:")
age=int(input())
print("Enter the Day of the week:")
day=input()
weekday_list=["monday","tuesday","wednesday","thursday","friday"]
weekend_list=["saturday","sunday"]
if(age>=60 and (day in weekday_list)):
    print("Age Group: Senior")
    print("Day: Weekday")
    print("your ticket price is : 7$")
elif(age>=60 and (day in weekend_list)):
    print("Age Group: Senior")
    print("Day: Weekend")
    print("your ticket price is : 10$")
elif(age>=60 and (day not in weekday_list and day not in weekend_list)):
    print("Invalid Day entered")
elif(age>=13 and(day in weekday_list)):
    print("Age Group: Adult")
    print("Day: Weekday")
    print("your ticket price is : 10$")
elif(age>=13 and(day in weekend_list)):
    print("Age Group: Adult")
    print("Day: Weekend")
    print("your ticket price is : 15$")
elif(age>=13 and(day not in weekday_list and day not in weekend_list)):
    print("Invalid Day entered")
elif(age<=12 and(day in weekday_list)):
    print("Age Group: child")
    print("Day: Weekday")
    print("your ticket price is : 5$")
elif (age <= 12 and (day in weekend_list)):
    print("Age Group: child")
    print("Day: Weekend")
    print("your ticket price is : 8$")
elif (age <= 12 and (day not in weekend_list and day not in weekday_list)):
   print("Invalid Day entered")

