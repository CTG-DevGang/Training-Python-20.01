#List in python
#Syntax:
#Create a list
list1 = []

#Add an element to the end of the list
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list1.append(3)
print(list1)
#Get the length of the list
print(len(list1))
#Remove an element from the list
#print(list1.pop())
#Get the index of the first occurence of an element
print(list1.index(3))
#Remove the first occurence of an element
list1.remove(3)
#Remove the element at a specific index
list1.pop(0)
#Remove all elements from the list
#list1.clear()
#Reverse the list
list1.reverse()
#Sort the list
list1.sort()
print(list1)