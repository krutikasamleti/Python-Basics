# lst = ["Apple","Banana", 8, 90.9, True,"Anushka","Krutika"]
# lst[0] = "Orange" # Lists are mutable 
# print(lst)
# print(lst[1:4]) #slicing

# lst.append("hehehe")  #Add at the end
# print(lst)

# lst2 = [2,4,1,6,3,7]
# lst2.sort()
# lst2.reverse()
# lst2.insert(2,23333)  #insert(index,value)
# print(lst2.pop(2))  #pop(index) 
# print(lst2.remove(3))  #remove(element)
# print(lst2)



fruits = []
f1 = input("enter fruit name")
fruits.append(f1)

f2 = input("enter fruit name")
fruits.append(f2)

f3 = input("enter fruit name")
fruits.append(f3)

f4 = input("enter fruit name")
fruits.append(f4)

f5 = input("enter fruit name")
fruits.append(f5)

f6 = input("enter fruit name")
fruits.append(f6)

f7 = input("enter fruit name")
fruits.append(f7)

print(fruits)

fruits.sort()
print(fruits)