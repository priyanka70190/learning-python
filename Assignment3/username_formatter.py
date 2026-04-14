"""Ask the user to enter their first name and last name seprately.
   Using String Methods & Slicing,generate the following outputs:
   1 full name with a space in between
   2 username in the format: first 3 letters of first name +full last name in lower case
   3 Email address in the format:firstname.lastname@email.com in lowercase
   total characters in the username(excluding spaces)
   """

print("enter first name: ")
f_n=input()
print("enter last name: ")
l_n=input()
full_name=" ".join([f_n,l_n])
print("full name: ",full_name)
username="".join([f_n[0:3],l_n.lower()])
print("UserName: ",username)
#print("Email:",f"{f_n}{"."}{l_n}{"@email.com"}")
print("Email address: ","".join([f_n.lower(),".",l_n.lower(),"@email.com"]))

username1=username.replace(" ","")
print("total characters in Username: ",len(username1))



