def greet():
    """
    Prints a basic greeting
    :return: None
    """

    print("Hello, what a lovely day!")
    print("I love walking in the part")

def greet_name(name):
    """
    Prints a basic greeting to a certain person
    :param name: the name of the person to greet
    :return: None
    """
    print(f"Hello {name}, nice to meet you!")

def average(a,b):
    """
    Calculates the average of a and b
    :param a: first number
    :param b: second number
    :return: None
    """
    print(f"The average of {a} and {b} is {(a + b) / 2}")

def average2(a,b):
    """
    Calculates the average of a and b
    :param a: first number
    :param b: second number
    :return: returns a float
    """
    return (a+b)/2

def average_multiple(a, b, c=0):
    """
    Calculates the average of 2 or 3 numbers
    :param a:
    :param b:
    :param c:
    :return: the average of 2 or 3 numbers
    """
    if c == 0:
        return average2(a,b)
    return (a+b+c)/3

#to see something, we need to "call" the function!
for i in range(10):
    greet()

greet_name("Josefine Epstein Luytens")

num1 = 10
num2 = 20
average(num1, num2)
print(f"I calculated 2 averages: {num1}, {num2}")

a2 = average_multiple(10, 20)
a3 = average_multiple(10, 20, 30)
print(f"I calculated 2 averages: {a2,a3}")

