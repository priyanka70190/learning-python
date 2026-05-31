"""
Build a simple shopping cart using a dictionary where the key is the item name
and the value is a dictionary with 'price' and 'quantity'. Allow the user to:
  1. Add item (name, price, quantity)
  2. Update quantity of an existing item
  3. Remove an item
  4. View cart (name, price, qty, subtotal per item)
  5. View total bill and exit
"""
print("1. Add item (name, price, quantity)\n2. Update quantity of an existing item\n"
      "3. Remove an item\n4. View cart (name, price, qty, subtotal per item)\n"
      "5. View total bill and exit")
"""from collections import defaultdict
cart = defaultdict(list)"""
cart={}
while True:
    print("Choose an option:")
    option = int(input())
    if option == 1:
        print("Item:",end=" ")
        name = input()
        print("Price:",end=" ")
        price = float(input())
        print("Quantity:",end=" ")
        quantity = int(input())

        cart[name] = {"price":price,"quantity":quantity}
    if option == 2:
        print("item name whose quantity is to be updated:",end=" ")
        item_name = input()
        print("enter updated quantity:",end=" ")
        quantity = int(input())
        cart[item_name]["quantity"] = quantity

    if option == 3:
        print("Item name to be remove:",end=" ")
        item_name = input()
        cart.pop(item_name)




    if option==4:

      for product_name,info in cart.items():
          print(product_name,"-",end="")
          print(" rs",info["price"],"*",info["quantity"],
                "=","rs",info["price"]*info["quantity"])

    if option==5:
        total_bill=0
        for product_name,info in cart.items():
            total_bill += info["price"]*info["quantity"]
        print("Total bill:",total_bill)
        break