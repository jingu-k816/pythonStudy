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
    print(income * tax_rate/100)

tax_calculator(50000, 21)

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