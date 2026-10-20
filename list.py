lst = ["Apple","Banana", 8, 90.9, True,"Anushka","Krutika"]
lst[0] = "Orange" # Lists are mutable 
print(lst)
print(lst[1:4]) #slicing

lst.append("hehehe")  #Add at the end
print(lst)

lst2 = [2,4,1,6,3,7]
lst2.sort()
lst2.reverse()
lst2.insert(2,23333)  #insert(index,value)
print(lst2.pop(2))  #pop(index) 
print(lst2.remove(3))  #remove(element)
print(lst2)

