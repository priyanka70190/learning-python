grocery=["apple","banana","mango",56]
print(grocery)
print(len(grocery))
print(grocery[3])
numbers=[2,9,7,11,3]
print(numbers)
print(numbers[2])
print(numbers.sort()) # sort reverse change the original list
print(numbers)
numbers.reverse()
print(numbers)
#List Slicing   but slicing will not impact the old list
print(numbers[0:5])
print(numbers[ : ])
print(numbers[1:4])

#Extended Slicing
print(numbers[: : 1])
print(numbers[ : : 2]) #skip 1 value
print(numbers[ : : 3]) #skip 2 values

#negative Slicing
print(numbers[ : :-2]) #ist reverse the list then 1 gap
print(numbers[ : : -3])# ist reverse then gap 2 values
print(numbers[ : :-1]) # reverse the list

print(numbers[1:5:-3]) #blank output try to take only -1 not any other number
print(numbers[1:5:-1]) # blank output
numbers1=[4,7,9,10,16,18]
print(numbers1[1:5:2])
print(max(numbers1))
print(min(numbers1))
#Append
numbers.append(77)  # it will insert number at last
print(numbers)
numbers2=[]
numbers2.append(5)
numbers2.append(8)
numbers2.append(78)
print(numbers2)

#insert it will insert number at particular location
numbers2.insert(1,90)
print(numbers2)
numbers2.remove(90)
print(numbers2)
numbers2.pop()
print(numbers2)

#tuples that are immutable but list is mutable

tp=(1,2,3)
print(tp)
#tp[1]=8 error bcz tuple is immutable
print(tp)
#to store one element in tuple
tp=(1,)
print(tp)


#swap 2 numbers in general way
a=8
b=19
temp=a
a=b
b=temp
print(a,b)

#swap 2 numbers in python

a,b=b,a
print(a,b)



