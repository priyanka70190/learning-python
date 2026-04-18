"""Ask the user to enter a password.using string methods and slicing print the following:
   total length of password
   password with all spaces removed
   first half of the password and second half of the password seperately(use slicing with len)
   a masked version of the password where only the first 2 and last 2 characters are visible
   and everything between is replaced by * (use string slicing and string repetition)
   """
print("Enter a password:")
password=input()
split_password=password.split()
nospace_password="".join(split_password)
print("No Space Password: ",nospace_password)
p_len=len(nospace_password)
print("Password Length: ",p_len)
#half=p_len//2
#print("Half of the Password: ",half)
print("First half of the Password: ",nospace_password[0:p_len//2])
print("Second half of the Password: ",nospace_password[p_len//2:p_len])

#Masked Password
first_2_char=nospace_password[0:2]
#print("First two char:",first_2_char)
last_2_char=nospace_password[p_len-2:p_len]
#print("Last 2 char:",last_2_char)
remaining_characters=len(nospace_password[2:p_len-2])
masked_password="".join([first_2_char,remaining_characters * "*",last_2_char])
print("Masked Password: ",masked_password)