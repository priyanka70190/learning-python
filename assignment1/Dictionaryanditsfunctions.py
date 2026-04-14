d1={ }
print(type(d1))
d2={"Harry": "Burger","Rohan":"Fish","SkillF":"Roti"}
print(d2)
print(d2["Harry"])
d2={"Harry":"Burger","Rohan":"Fish","SkillF":"Roti","Shubham":{"B":"maggie","L":"Roti","D":"Chicken"}}
print(d2)
print(d2["Shubham"]["B"])
d2["Ankit"]="Junk Food"
print(d2)
d2[420]="kebabs"
print(d2)
del d2["Ankit"]
print(d2)
print(d2.copy())  #it will return copy of d2
#d3=d2 #here d3 is not a new dictionary its just pointing to d2 dictinory so both pointing to same
#del d3["Harry"]
print(d2)
d3=d2.copy()
del d3["Harry"]
print(d3)
print(d2) #here Harry will not be deleted
print(d2["Harry"])
print(d2.get("Rohan"))  #it will return none
d2.update({"Leena":"Toffee"})
print(d2)
print(d2.keys())
print(d2.items())