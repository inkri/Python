#variables and print
age=30
print("Age is:",age)

PI = 3.14159
RADIANS_TO_DEGREES = 180 / PI
print(RADIANS_TO_DEGREES)

#Numbers:
age=33  #Integers
PI=3.14  #float

math_operation=1+3*4/2-2
print(math_operation)
integer_division=13//5
print(integer_division)
remainder=13%5
print(remainder)
x=37
remainder=x%2
print(remainder)

#Strings
my_string="Hello,world!!"
print(my_string)
string1="Hello,it's me."
string2='He said,"How are you doing" in yesterday meeting.'

age=34
age_as_str=str(age)
#print("Your are " + age) #Error + for string only
print("Your are "+ age_as_str)
print(f"You are {age}")

name="abhi"
final_greeting="How are you, {}"
abhi_greeting=final_greeting.format(name)

print(abhi_greeting)
name="Jyoti"
jyoti_greeting=final_greeting.format(name)
print(jyoti_greeting)

#User Input
my_name="abhi"
your_name=input("Enter yourname:")
print(f"Hello {your_name}. My name is {my_name}.")

age=input("Enter your age: ")
age_int=int(age)
#age=int(input("Enter your age: "))
#months=age * 12
print(f"You have lived for {age_int * 12} months.")

user_name = input('Enter your name: ')
print('Hello, ' + user_name)

user_age = int(input('Enter your age: '))
print(user_age * 12)

#Booleans and comparisons
truthy= True
falsy= False

age=20
is_over_age=age >= 18

my_number=5
user_number=int(input("Enter a number:"))
matches= my_number == user_number
print(f"You got it right: {matches}.")


age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150

print(f"You can learn programming: {can_learn_programming}")age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150
print(f"You can learn programming: {can_learn_programming}")

age = int(input("Enter your age: "))
usually_not_working = age < 18 or age > 65
print(f"At {age}, you are usually not working: {usually_not_working}")

age = int(input("Enter your age: "))
usually_working = age > 17 and age < 66  # Notice the changes to the numbers!
print(f"At {age}, you are usually working: {usually_not_working}")


print(bool(35))
print(bool("Rolf"))
print(bool(0))
print(bool(""))

print("" or "Rolf")  # Rolf, because "" is falsy
print("" and "Rolf")  # "", because it is falsy
print("Rolf" or "")  # "Rolf", because it is truthy
print("Rolf" and "")  # "", because "Rolf" is not falsy


x1 = 0 or 35
x2= 35 or 0
y1= 0 & 35
y2=35 & 0

name=input("Enter your name:")
surname=input("Enter your surname:")
greeting= name or f"Mr. {surname}"
print(greeting)


#List
friends=["a","b","c","d"]
print(friends[0])
friends2=[["a",22],["b",23],["c",24]]
print(friends2[0][0])
friends2.remove(["a",23])

#Tuples
sam=(1,2,3,4,5)
sam2=("a","b")
sam3="c","d"

#sets
art_friends={"samy","anne"}
science_friends={"jen","charlie"}
art_friends.add("jen")
print(art_friends)
art_friends.remove("jen")

art_not_science=art_friends.difference(science_friends)
not_in_both=art_friends.symmetric_difference(science_friends)
art_and_science=art_friends.intersection(science_friends)
all_friends=art_friends.union(science_friends)

#Dictionaries
friends_Age={"abhi":29,"jyoti:26","Jay":30}
print(friends_Age["abhi"])
friends_Age["bob"]=32

friends= (
    {"name":"abhi jais","age":30},
    {"name":"sam","age":26},
    {"name":"jay","age":31}
)

print(friends[0]["name"])

friend2=[("sam",24),("jay",34)]
friend3=dict(friends)


grades = [80, 75, 90, 100]
grades = (80, 75, 90, 100)
grades = {80, 75, 90, 100}  # This one, because of no duplicates


total = sum(grades)
length = len(grades)

average = total / length

#Joins
friends = ["Rolf", "Anne", "Charlie"]
print(f"My friends are {friends}.")

friends = ["Rolf", "Anne", "Charlie"]
comma_separated = ", ".join(friends)
print(f"My friends are {comma_separated}.")


