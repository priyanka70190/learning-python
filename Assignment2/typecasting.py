

#For int datatype
a=8
print("integer a: ",a)
print("float a:",float(a))
print("boolean a:",bool(a))
print("str1ing a:",str(a))
#print("List a:",list(a)) //errror
#print("set a:",set(a))   //error a(int object) is not iteratble
#print("tuple a: ",tuple(a))
#print("dict a:",dict(a))

#For Float Datatype
b=8.53
print("integer b:",int(b))
print("float b:",float(b))
print("boolean b:",bool(b))
print("str1ing b:",str(b))
#print("List b:",list(b)) #error float object is not iterable
#print("Set b:",set(b)) #error
#print("Tuple b:",tuple(b)) #error
#print("Dictionary b:",dict(b)) #error

#For Boolean Type

c= False
print("Integer c: ",int(c))
print("Float c:",float(c))
print("boolean c:",c)
print("string c:",str(c))
#print("List is:",list(c)) #bool object is not iterable
#print("Set is: ",set(c))
#print("Tuple is: ",tuple(c))
#print("Dict is : ",dict(c))

#For string Datatype
str1="hello world India"
#print("Integer str1ing: ",int(str1)) #invalid literal for int
print("str1ing str1: ",str1)
#print("Float str1: ",float(str11)) #could not convert string to float
print("Boolean str1: ",bool(str1))  # give value true
print("List str1: ",list(str1))
print("Set str1: ",set(str1))
print("Tuple str1: ",tuple(str1))
#print("Dictionary str1: ",dict(str1)) #required 2 values bt it has only 1 like key and value


#For List Data Type
l=["apple","Mango","Banana"]
print("List l: ",l)
#print("Integer List: ",int(l)) #Error int argument must be str1ing or real number not list
#print("float List: ",float(l)) #Error same
print("Boolean List: ",bool(l)) #true
print("string List: ",str(l))
print("Set List: ",set(l))
print("Tuple List: ",tuple(l))
#print("Dictionary List: ",dict(l)) #Error Key + value required


#For Set Datatype
s ={1,2,3,4,5,"Mango"}
print("Set s: ",s)
#print("Integer Set: ",int(s)) #int argument can be string or real number
#print("float set: ",float(s)) #error same
print("Boolean Set: ",bool(s)) # true
print("String Set: ",str(s))
print("List set: ",list(s))
print("Tuple set: ",tuple(s))
#print("Dictionary set: ",dict(s)) # Error Object is not iterable

#For Tuple DataType
t=("apple","Mango","Banana","apple")
print("tuple Tuple: ",t)
#print("Integer Tuple: ",int(t)) #Error
#print("Float Tuple: ",float(t)) # Error
print("Boolean tuple: ",bool(t))
print("String tuple: ",str(t))
print("List tuple: ",list(t))
print("Set Tuple: ",set(t))
#print("Dictionary Tuple: ",dict(t)) #Key and value required

#For Dictionary Data Type
d={"Priyanka":"Burger","Amy":"Pizza","Ankush":"Roti"}
print("Dict d: ",d)
print("Boolean Dict: ",bool(d)) #true
#print("Integer Dict: ",int(d)) #Error
#print("Float Dict: ",float(d)) #Error
print("String Dict: ",str(d))
print("List Dict: ",list(d))
print("Tuple Dict: ",tuple(d))
print("Set Dict: ",set(d))