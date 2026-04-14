mystr="harry is a good boy"
#print(mystr)
print(mystr[5]) #it will print space

print(mystr[0:4])
print(len(mystr))

print(mystr[0:18])

#print(mystr[78])  it will throw error
print(mystr[0:78])
#Advance String Slicing

print(mystr[0:5:2])
print(mystr[0:])
print(mystr[:5])
print(mystr[: :])   #same as mystr[0:19:1]
print(mystr[0: :2])
print(mystr[ : :9])
print(mystr[ : :559])
print(mystr[-1:0])
print(mystr[-4:])
print(mystr[-4:-2])
print(mystr[ : :-1]) #string ulta krna
print(mystr[ : :-2])
print(type(mystr))
print(mystr.isalnum())
mystr1="harryisagoodboy"
print(mystr1.isalnum())
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.upper()) #mystr.lower()
print(mystr.find("is"))
print(mystr.replace("is","are"))
