#If statements
friend="Abhi"
user_name=input("Enter your name: ")

if user_name.lower() == friend.lower():
    print("Hello, friend.")
else:
    print("Hello, stranger!")


friends = ['rajan','raja','sam']
family = ['ashu','ash','sri']
user_name=input("Enter your name: ")

if user_name.lower() in friends:
    print("Hello, friend.")
elif user_name.lower() in family:
    print("Hello, family!")
else:
    print("Hello, stranger!")


#While loops:
is_learning = True

while is_learning:
    print("You are learning.")
    is_learning = False

user_input=input("Do you wish to run the program?(yes/no):")
while user_input == "yes":
    print("You are learning.")
    user_input = input("Do you wish to run the program?(yes/no):")
    is_learning = user_input == "yes"

# Let's begin by asking the user to type either 'p' or 'q':
user_input = input('Enter q or p: ')
# Now we must repeat until they type 'q':
while user_input != 'q':
    # Inside our loop, check if they typed 'p'. If they did, print "Hello"
    if user_input == 'p':
        print("Hello")
    # Now we must ask the user for their input again—otherwise we would be in an infinite loop!
    user_input = input('Enter q or p: ')


#For loop:
friends = ['rajan','raja','sam']
for friend in friends:
    print(friend)

elements=[0,1,2,3,4,5,6,7,8,9]
for index in elements:
    print("Hello Abhi & Jyoti")

for index in range(10):
    print("Hello Abhi & Jyoti")

students = [
    {"name":"Ashu","grade":70},
    {"name":"Abhi","grade":80},
    {"name":"Ash","grade":85},
    {"name":"Sri","grade":90},
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has a grade of {grade}.")


#Destructuring syntax:
currencies = 0.8,1.2
usd,eur=currencies

friends=[("Ashu",35),("Abhi",32),("Ash",30),("Sri",28)]
for name,age in friends:
    print(f"{name} is {age} years old.")


#Iterating over dictionary:
friend_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

for name in friend_ages:
    print(name)

for age in friend_ages.values():
    print(age)

for name, age in friend_ages.items():
    print(f"{name} is {age} years old.")



# -- break --
# Exits out of the loop, so that no more iterations occur.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break

    print(f"This car is {status}.")

# -- continue --
# Terminates the current iteration and moves onto the next one.

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue

    print(f"This car is {status}.")
    print("Shipping new car to customer!")

# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)