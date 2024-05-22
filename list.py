"""
List - collection of values seperated by comma
     - mutable datatype - we can change value after storing
     - allows duplicate values
     - order and indexed 
     - [] bracket is used


"""

citylist=[]

n=int(input("How many values ? "))
for x in range(n):
    name=input("Enter city name :")
    citylist.append(name)    

print(citylist)

# create and initialize list

mylist=[10,20,30,40,10,50]
print(mylist)
print(mylist[3])

# copy list
newlist=mylist.copy()
print("After copy : ",newlist)

mylist.reverse()
print("reverse list : ",mylist)

mylist.sort()
print("sort : ",mylist)

for x in mylist:
    print(x)

print("Length : " , len(mylist))

search=int(input("Enter no : "))
if search in mylist:
    print("Found")
else:
    print("Not Found")

# update list value
mylist[0]=11
print("After update : ",mylist)

# Add new value at end of the list
mylist.append(90)
print(mylist)

# add at specific position
mylist.insert(2,77)
print(mylist)

# remove specific value
mylist.remove(77)
print(mylist)

# remove last value
mylist.pop()
print(mylist)

# remove all values
mylist.clear()
print(mylist)

del mylist








