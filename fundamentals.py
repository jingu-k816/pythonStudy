# Print hello world
print("hello world")

# Variables
# Javascript usually uses camel case(myAge) but python mainly uses snake case (my_age)
a = 2 # an integer gets stored into a memory
b = 3
c = a + b
c = 1 # overwrites the top code
print(c)

# Booleans and strings
my_name = "Jingu"
print(my_name)

my_bool = True #first letter has to be a capital letter (True | False)
print(my_bool)


# Functions
def say_hello():
    print("hello how are you?")

say_hello()

# Parameters
def say_bye(message):
    print("Someone said:", message)

say_bye("Bye Jingu!")

def tax_calculator(income, tax_rate):
    return income * (tax_rate/100)

def addition(a, b):
    print(a + b)

def subtraction(a, b):
    print(a - b)

def multiplication(a, b):
    print(a * b)

def division(a, b):
    print(a / b)

def squared(base, exponent):
    print(base ** exponent)

squared(3, 3)

def pay_tax(tax):
    print("thank you for paying", tax)

amount_to_pay = tax_calculator(50000, 21)
pay_tax(amount_to_pay)

my_name = "Jingu"
my_age = 27
my_eye_color = "black"

# f-strings
print(f"Hello I'm {my_name}, I am {my_age} years old and my eye color is {my_eye_color}")

if 10 > 5 :
    print("Correct!")

winning_number = 10

if winning_number > 7:
    print("Winning number is greater than 7")
elif winning_number < 7:
    print("Winning number is less than 7")
else:
    print("Winning number is 10")
"""
age = int(input("how old are you?"))

if age < 18:
    print("you cannot drink")
elif age >= 18 and age <= 35:
    print("you drink beer!")
elif age == 60 or age == 70:
    print("Birthday Party!")
else:
    print("Go ahead!")
"""
# Casino Game
from random import randint
"""
user_choice = int(input("Choose a number: "))
computer_choice = randint(1, 50)

if user_choice == computer_choice:
    print("You won!")
elif user_choice > computer_choice:
    print("Lower! Computer chose:", computer_choice)
elif user_choice < computer_choice:
    print("higher! Computer chose:", computer_choice)
"""
# While
distance = 0

while distance < 20:
    print("I'm running:", distance, "km")
    distance = distance + 1

