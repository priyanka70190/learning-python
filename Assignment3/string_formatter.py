"""Ask the user to enter a raw product entry in the following messy format:
   "PRODUCT NAME : PRODUCT_CODE : PRICE"
    USING STRING METHODS AND SLICING:
    1 strip all leading and trailing spaces
    2 split the entry by a colon(:) seperator
    3 extract the product name
    extract the product code
    extract the price seprately
  4 clean each value using strip to remove extra spaces
  5 print the product name in the titlecase
  6 print the product code in uppercase
  7 print the price formatted to 2 decimal places
  8 print a final formatted receipt line as : Product:<name>|Code<code>|Price:$<price>"""

print("Enter Product Entry: ")
product_entry=input()
stripped_product_entry=product_entry.strip()
print("Stripped Product Entry: ", stripped_product_entry)
#split
splited_product_entry=stripped_product_entry.split(":")
print("split Product Entry: ", splited_product_entry)
print("Product Name: ", splited_product_entry[0].strip())
print("Product Code: ", splited_product_entry[1].strip())
print("Price: ", splited_product_entry[2].strip())
print("product name in title case: ",splited_product_entry[0].strip().title())
print("product code in upper case: ",splited_product_entry[1].strip().upper())
print("price formatted to 2 decimal places: ",round(float(splited_product_entry[2].strip()),2))
print("Product:",splited_product_entry[0].strip(),"|","Code: ",splited_product_entry[1].strip(),"|",
      "Price: $",splited_product_entry[2].strip())
