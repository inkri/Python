#Functions:
# Let's create our own function. The building blocks are:
# def
# the name
# brackets
# colon
# any code you want, but it must be indented if you want it to run as part of the function.
def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

greet()
# Any variables declared inside the function are not accessible outside it.
print(name)  # ERROR!


#Arguments-and-parameters
# Imagine you've got some code that calculates the fuel efficiency of a car:

car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}

mpg = car["mileage"] / car["fuel_consumed"]
name = f"{car['make']} {car['model']}"
print(f"{name} does {mpg} miles per gallon.")

# You could put this in a function:


def calculate_mpg():
    car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}

    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")


calculate_mpg()

# But this is not a very reusable function since it only calculates the mpg of a single car.
# What if we made it calculate the mpg of "any" arbitrary car?

car = {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460}


def calculate_mpg(car_to_calculate):  # This can be renamed to `car`
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")


calculate_mpg(car)

# This means that given a list of cars with the correct data format, we can run the function for all of them!

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

for car in cars:
    calculate_mpg(car)


#Return-values-for-functions
def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg  # Ends the function, gives back the value


def car_name(car):
    return f"{car['make']} {car['model']}"


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name} does {mpg} miles per gallon.")
    # Returns None by default, as all functions do


cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

for car in cars:
    print_car_info(car)
    # try print(print_car_info(car)), you'll see None


# -- Multiple returns --


def divide(x, y):
    if y == 0:
        return "You tried to divide by zero!"
    else:
        return x / y


print(divide(10, 2))  # 5
print(divide(6, 0))  # You tried to divide by zero!


#Default-parameter-values
def add(x, y=3):  # x=2, y is not OK
    total = x + y
    print(total)


add(5)
add(2, 6)
add(x=3)
add(x=5, y=2)

# add(y=2)  # ERROR!
# add(x=2, 5)  # ERROR!
# -- More named arguments --

print(1, 2, 3, 4, 5, sep=" - ")  # default is " "
# You can use almost anything as a default parameter value.
# But using variables as default parameter values is discouraged, as that can introduce difficult to spot bugs
default_y = 3


def add(x, y=default_y):
    sum = x + y
    print(sum)

add(2)  # 5
default_y = 4
print(default_y)  # 4
add(2)  # 5
# Be careful when using lists or dictionaries as default parameter values. Unlike integers or strings, these will update if you modify the original list or dictionary.
# This is due to a language feature called mutability. It's not important to understand this now, but just know that they behave differently to integers and strings behind the scenes when you change them.



#Lambda-functions
divide = lambda x, y: x / y

def divide(x, y):
    return x / y

print(divide(15, 3))

result = (lambda x, y: x + y)(15, 3)
print(result)

# Here's an example. Instead of this:


def average(sequence):
    return sum(sequence) / len(sequence)


students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))

# Since the average function just takes inputs and returns an output, we could re-define it as a lambda function.

average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))


#First-class-and-higher-order-functions
# In Python, functions are first class citizens. That means that, just like any other value, they can be passed as arguments to functions or assigned to variables. Here's a simple (yet not terribly useful) example to illustrate it:


def greet():
    print("Hello!")


hello = greet  # hello is another name for the greet function now.

hello()


# And, you can also pass it to a function:


# `before_and_after` is a higher-order function. That just means it's a function which has another function as a parameter.
def before_and_after(func):  # func is a function passed
    print("Before...")
    func()
    print("After...")


# greet, not greet(). That's because we're passing the function, not the result of calling the function.
before_and_after(greet)


# Let's move on to a more useful example.
# Here, you can see how we can store functions inside a dictionary—just as we could do with numbers, strings, or any other type of data.

operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),  # could just be `sum`
    "top": lambda seq: max(seq),  # could just be `max`
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    print(operations[operation](grades))

# As we learn more about Python and we cover more advanced content, this will become more useful!
