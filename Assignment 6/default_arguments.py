"""PROBLEM STATEMENT: Create a function called introduce() that takes 3 arguments:
name
city
hobby (default value = "coding")
The function should print an introduction sentence using all 3 values. Call the function in the following 3 ways:
Passing all 3 arguments
Passing only name and city
Passing only the name"""

def introduce(name,city="London",hobby="coding"):
    print("Hi,I am ",name," . I Live in ",city," and i enjoy ",hobby,".")


introduce("Ram","India","Dancing")
introduce("Sham","Pakistan")
introduce("Geeta")