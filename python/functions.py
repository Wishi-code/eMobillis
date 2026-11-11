def greet():
    print("Hello there!")
    print("Welcome to programming.")

greet()

#parameters and arguments
def greet(name):
    print ("hello", name)
greet ("Mary")
#default parameters
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Mary")
#keyword arguments
#sending arguments with the key = value syntax. This way the order of the arguments does not matter.
def my_function(animal, name):
    print ("I have a",animal)
    print("My", animal, "name is", name)
my_function(animal="dog",name="Buddy" )    


def calculate(a, b):
    addition = a + b
    subtraction = a - b

    return addition, subtraction


result1, result2 = calculate(20, 10)

print("Addition:", result1)
print("Subtraction:", result2)

#high order functions
#accepting other functions as arguments and returns functions as output. A function that takes another function as an argument is called a higher-order function.
def greet():
    return "Hello there!"
def execute_function(func):
    result=func()
    print(result)
execute_function(greet)   

#filter function
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(number):
    return number % 2 == 0

result = filter(is_even, numbers)

print(list(result))

#combining functions in a real world application
def calculate_average(marks):
    return sum(marks) / len(marks)


def determine_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "E"


def display_results(name, average, grade):
    print("Student:", name)
    print("Average:", average)
    print("Grade:", grade)


def main():
    name = input("Enter student name: ")

    marks = [75, 80, 65, 90]

    average = calculate_average(marks)
    grade = determine_grade(average)

    display_results(name, average, grade)


main()