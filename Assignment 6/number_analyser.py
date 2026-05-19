"""Create a function called analyse_numbers() that accepts any number of integers
as arguments using *args and returns a dictionary containing:
total → sum of all numbers
average → average of all numbers
maximum → largest number
minimum → smallest number
even_count → count of even numbers
odd_count → count of odd numbers
Ask the user to enter how many numbers they want to enter,
collect them in a loop, and pass them all to the function using *args.
Print each result from the returned dictionary in a formatted way.
Commit the changes of the file and Push to Github."""

def number_analyser(*arguments):
    dict1={}
    sum=0
    max=0
    min=int(arguments[0])
    for n in arguments:
        sum+=int(n)
    len1=len(arguments)
    average=round(sum/len1,2)
    for n in arguments:
        if(int(n)>max):
           max=int(n)
    for n in arguments:
        if(int(n)<min):
           min=int(n)
    even=0
    for n in arguments:
        if(int(n)%2==0):
            even=even+1
    odd=0
    for n in arguments:
        if(int(n)%2!=0):
            odd=odd+1



    dict1.update({"Total": sum})
    dict1.update({"Average": average})
    dict1.update({"Maximum": max})
    dict1.update({"Minimum": min})
    dict1.update({"even_count": even})
    dict1.update({"odd_count": odd})
    #print("Total is:",total)


#    max_number=max()
 #   dict1.update({"Maximum": max_number})
    return dict1


print("How many numbers do you wish to enter?")
numbers=int(input())
i=1
list1=[]
while(i<=numbers):
    print("Enter the number:")
    n=input()
    list1.append(n)
    i=i+1

n_a=number_analyser(*list1)
print("Total is:",n_a["Total"])
print("Average is:",n_a["Average"])
print("Maximum Value is:",n_a["Maximum"])
print("Minimum Value is:",n_a["Minimum"])
print("eVEN nUMBERS:",n_a["even_count"])
print("ODD nUMBERS:",n_a["odd_count"])


