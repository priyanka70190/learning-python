"""Ask the user to enter a product name ,unit price and quantity.
   Use an F-string to print a formatted bill showing the total cost,
   with the price formatted to 2 decimal places."""

print("product name:")
name=input()
print("unit price:")
price=float(input())
print("quantity:")
quantity=int(input())
print(f"Bill Summary:{quantity} * {name} @{price} each = {price*quantity:.2f}rs")