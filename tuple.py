a = (1,2,3,4,3)
b = (1)
print(type(b)) # int
c = (2,)
print(type(c)) #tuple 
print(a)
print(type(a))  #tuple are immutable

num = a.count(3)  #count of the number in tuple
print(num)

d = a.index(4)  #returns index of that number
print(d)

slice = a[0:4]
print(slice)

