"""a=9
b=8
c=sum((9,8))  #built in function
print("sum is",c)"""


"""def fn1():
    print("hello you are in fn 1")

fn1()
print(fn1())"""

def fn2(a,b):
    print("hello you are in fn 2",a+b)

fn2(5,7)


def fn3(a,b):
    """find average of two numbers"""
    avg=(a+b)/2
   # print("average is: ",avg)
    return avg

v=fn3(6,6)
print("avg is",v)

print(fn3.__doc__)