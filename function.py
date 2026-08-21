
# 1. FUNCTION WITHOUT ARGUMENTS AND WITHOUT RETURN VALUE


def greet():
    print("Hello, World!")


greet()



# 2. FUNCTION WITH ARGUMENTS AND WITHOUT RETURN VALUE


def greet_user(name):
    print("Hello", name)


greet_user("Rahul")



# 3. FUNCTION WITHOUT ARGUMENTS BUT WITH RETURN VALUE

def get_number():
    return 100


number = get_number()
print(number)


# 4. FUNCTION WITH ARGUMENTS AND WITH RETURN VALUE


def add(a, b):
    return a + b


result = add(10, 20)
print(result)

# 5. FUNCTION WITH DEFAULT ARGUMENT


def welcome(name="User"):
    print("Welcome", name)


welcome()
welcome("Rahul")


# 6. FUNCTION WITH MULTIPLE ARGUMENTS


def add_three_numbers(a, b, c):
    return a + b + c


result = add_three_numbers(10, 20, 30)
print(result)


# 7. POSITIONAL ARGUMENTS


def student(name, age):
    print("Name:", name)
    print("Age:", age)


student("Rahul", 20)


# 8. KEYWORD ARGUMENTS


def student_info(name, age):
    print("Name:", name)
    print("Age:", age)


student_info(age=20, name="Rahul")



# 9. *args - VARIABLE LENGTH POSitional ARGUMENTS

def add_all(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


print(add_all(10, 20))
print(add_all(10, 20, 30))
print(add_all(1, 2, 3, 4, 5))


# 10. **kwargs - VARIABLE LENGTH KEYWORD ARGUMENTS


def show_details(**details):
    for key, value in details.items():
        print(key, ":", value)


show_details(
    name="Rahul",
    age=20,
    city="Pune"
)


# 11. *args AND **kwargs TOGETHER


def display(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


display(
    10,
    20,
    30,
    name="Rahul",
    age=20
)


# 12. FUNCTION RETURNING MULTIPLE VALUES


def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


add_result, sub_result, mul_result = calculate(10, 5)

print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)


# 13. RECURSIVE FUNCTION


def factorial(n):

    # Base condition
    if n == 0:
        return 1

    # Function calls itself
    return n * factorial(n - 1)


print("Factorial:", factorial(5))

# 14. LAMBDA FUNCTION


square = lambda x: x * x

print("Square:", square(5))


multiply = lambda a, b: a * b

print("Multiplication:", multiply(5, 4))



# 15. NESTED FUNCTION
#    Function inside another function


def outer():

    print("Outer function")

    def inner():
        print("Inner function")

    inner()


outer()

# 16. FUNCTION PASSED AS AN ARGUMENT
#    Higher-Order Function

def square_number(x):
    return x * x


def calculate_value(function, number):
    return function(number)


result = calculate_value(square_number, 5)

print("Result:", result)


# 17. FUNCTION RETURNING ANOTHER FUNCTION


def outer_function():

    def inner_function():
        print("Hello from inner function")

    return inner_function


my_function = outer_function()

my_function()

# 18. GENERATOR FUNCTION
#    Uses yield instead of return


def generate_numbers():

    yield 1
    yield 2
    yield 3


for number in generate_numbers():
    print("Generated:", number)


# 19. FUNCTION WITH TYPE HINTS


def add_numbers(a: int, b: int) -> int:
    return a + b


result = add_numbers(10, 20)

print("Type hint result:", result)


# 20. FUNCTION WITH DOCSTRING


def subtract(a, b):
    """
    This function subtracts b from a.
    """

    return a - b


print("Subtraction:", subtract(20, 5))

print(subtract.__doc__)


# 21. FUNCTION USING pass
#    Used when function implementation is not ready


def future_function():
    pass


# Function can be called without doing anything

# 22. ASYNCHRONOUS FUNCTION
#    Uses async def


import asyncio


async def async_greet():
    print("Hello from async function")


asyncio.run(async_greet())

# 23. POSITIONAL-ONLY ARGUMENTS
#    Arguments before / must be positional


def positional_only(a, b, /):
    return a + b


print(
    "Positional only:",
    positional_only(10, 20)
)

# 24. KEYWORD-ONLY ARGUMENTS
#    Arguments after * must be keyword arguments


def keyword_only(name, *, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)


keyword_only(
    "Rahul",
    age=20,
    city="Pune"
)


# 25. POSITIONAL-ONLY + NORMAL + KEYWORD-ONLY


def all_argument_types(a, b, /, c, *, d, e):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)
    print("e =", e)


all_argument_types(
    1,
    2,
    3,
    d=4,
    e=5
)

# 26. FUNCTION WITH LOCAL VARIABLE


def local_example():

    
    message = "I am local"

    print(message)


local_example()


# 27. FUNCTION WITH GLOBAL VARIABLE


global_message = "I am global"


def global_example():

    print(global_message)


global_example()


# 28. FUNCTION MODIFYING A GLOBAL VARIABLE


count = 0


def increase_count():

    global count

    count = count + 1


increase_count()
increase_count()

print("Count:", count)



# 29. FUNCTION WITH EXCEPTION HANDLING


def divide(a, b):

    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero"


print(divide(10, 2))
print(divide(10, 0))



# 30. FUNCTION WITH LIST AS ARGUMENT


def print_list(items):

    for item in items:
        print(item)


numbers = [10, 20, 30, 40]

print_list(numbers)



# 31. FUNCTION WITH DICTIONARY AS ARGUMENT


def print_dictionary(data):

    for key, value in data.items():
        print(key, ":", value)


student = {
    "name": "Rahul",
    "age": 20,
    "city": "Pune"
}

print_dictionary(student)



# 32. FUNCTION WITH ANOTHER FUNCTION


def double(x):
    return x * 2


def apply_function(func, value):
    return func(value)


result = apply_function(double, 10)

print("Double:", result)



# 33. FUNCTION USING lambda WITH map()


numbers = [1, 2, 3, 4, 5]

squares = list(
    map(lambda x: x * x, numbers)
)

print("Squares:", squares)



# 34. FUNCTION USING lambda WITH filter()


numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print("Even numbers:", even_numbers)

















