"""Ask the user to enter product names and their quantities(for 4 products)
   store them in a dictionary then:
   -print the product with the highest quantity
   - print the product with the lowest quantity
   - print the total inventory count"""
dict1={}
i=0
while(i<4):
    print("Enter Product:")
    name=input()
    print("Enter Quantity:")
    quantity=int(input())
    dict1[name]=quantity
    i=i+1
j=0
keys=list(dict1)
first_key=keys[0]
first_value=dict1[first_key]
max=first_value

for name, quantity in dict1.items():
      if max<quantity:
         product=name
         max=quantity


print("Highest Stock:",product,"(",max,")")

keys=list(dict1)
first_key=keys[0]
first_value=dict1[first_key]
min=first_value

for name, quantity in dict1.items():
    if min>quantity:
        product=name
        min=quantity

print("Lowest Stock:",product,"(",min,")")

total=0
for name, quantity in dict1.items():
    total+=quantity
print("Total Inventory:",total)