students =["Natal", "Lordy", "Leence", "John"]
print (students)
print (students[0])
print (students[-1])
print (students[-3])
print (students[1:3])

students[1] = "Menelik"

#adding items to the list
students.append("Nerelle")

#add an item at a specific position
students.insert (1,"Wishie")
print (students)
#extend... adding multiple items from another 
more_students=["Mich","Nasher"]
students.extend(more_students)
print(students)

#removing items from a list
students.remove("Nerelle")
print(students)

# pop() removes a item using its index, if you dont provide the index it removes the last index
# clear removes all items fro the list
# len function returns the number of items in a list
print (len(students))

#looping through a list to access all the items of a list
for student in students:
    print (student)