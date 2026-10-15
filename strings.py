name = "Krutika" # Strings are immutable
# name1 = 'Krutika'
# name2 = """Krutika"""  multi-line

name_slice = name[1:4] #start from index 0 till 3 (excluding 3)
print(name_slice)
print(len(name_slice))

print(name[-4:len(name)])
print(name[3:len(name)])

print(name[:4])  # is same as print(name[0:4])
print(name[1:])  # is same as print(name[1:7])
print(name[-4:-1]) 
print(name[3:6]) # same as -4:-1 in positive
print(name[::-1])  #[start:stop:step]

print(name[1:6:2]) #rtk