student = {
    "name": "James",
    "age": 20,
    "course": "Software Engineering"
}

# Characteristics of dictionaries
# - Dictionaries store data in key-value pairs.
# - They are changeable (mutable).
# - Keys must be unique.
# - Values can be duplicated.
# - Keys are case-sensitive.
# - Values can have different data types.
# - Dictionaries preserve insertion order.


student = dict(name="Mary", age=21, course="Computer Science")
student = {
    "name": "James",
    "age": 20,
    "course": "Software Engineering"
}

print(student["name"])
print(student["age"])
print(student["course"])
#adding items to the dictionary
student ["secondName"] ="Wish"

#looping through keys in a dictionary
for key, value in student.items():
    print(key, ":", value)

    #nested dictionary
    students = {
    "student1": {
        "name": "James",
        "age": 20,
        "course": "Software Engineering"
    },

    "student2": {
        "name": "Mary",
        "age": 21,
        "course": "Computer Science"
    }
}
    print(students["student1"]["name"])