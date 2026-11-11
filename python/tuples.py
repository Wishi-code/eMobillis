# they use rounded brackets
students = ("James", "Mary", "Peter", "Ann")

print(students)
# Characteristics of tuples
# Tuples have the following characteristics:
# - Ordered: Items maintain their original positions.
# - Immutable: Items cannot be changed after creation.
# - Allow duplicates: The same value can appear more than once.
# - Allow different data types: A tuple can store strings, integers, floats and booleans.

#looping through tuples

for student in students:
    print (student)

    #using while loop
    
i=0
while i< len(students):
    print(students [i])
    i+= 1

    #converting lists to tuples
    fruits = ["Mango", "Apple", "Banana"]

new_fruits = tuple(fruits)

print(new_fruits)