"""write 2 fn celcius to fahrenheit and fahrenheit to celcius,each with a multiline docstring
   describing the fn and its parameter and its return value.Call both fns and print their results
   along with their docstrings"""

def cel_to_fahr(cel):
    """
    converting temperature from celcius to fahrenheit
    parameters:
    temprature in celcius in float type
    return:
    temperature in fahrenheit in float type
    """
    f=(9*cel)/5+32
    return f


def fahr_to_cel(fahr):
    """
       converting temperature from fahrenheit to celcius
       parameters:
       temprature in fahrenheit in float type
       return:
       temperature in celcius in float type
       """
    c=(fahr-32)*(5/9)
    return c

print("Enter the temperature in celcius:",end="")
cel=float(input())
print("Enter the temperature in fahrenheit:",end="")
fahr=float(input())
print(cel_to_fahr.__doc__)
fahr=cel_to_fahr(cel)
print(f"{cel}C={fahr}F")

print(fahr_to_cel.__doc__)
cel=fahr_to_cel(fahr)
print(f"{fahr}F = {cel}C")
