# File: Homework 3.py 

# --------------------------------------------------------
# 3. Print Functions
# --------------------------------------------------------

def say_goodbye(name):
    #Prints a goodbye message
    print("Goodbye,", name)

def area_of_circle(radius):
    # Prints the area of a circle given its radius
    pi = 3.14
    area = pi * radius ** 2
    print(f"The area of a circle with radius {radius} is {area}.")


# --------------------------------------------------------
# 4. Return Functions
# --------------------------------------------------------

def subtract(a, b):
    # Subtracts a number from another
    return a - b

def multiply(a, b):
    #Multiplies two numbers
    return a * b

def divide(a, b):
    #Divides a number by another
    return a / b


# --------------------------------------------------------
# 5. Conditionals
# --------------------------------------------------------

def min_and_max(temperatures):
    # Returns a tuple from a temperature list
    return (min(temperatures), max(temperatures))

def is_weekend(day_number):
    # Returns True if it's the weekend, False otherwise.
    # Monday = 1, ..., Sunday = 7
    if day_number == 6 or day_number == 7:
        return True
    else:
        return False

def fuel_efficiency(distance, fuel_used):
    # Returns fuel efficiency
    if fuel_used == 0:
        return "Fuel used cannot be zero"
    return distance / fuel_used

def secret_code(number):
    #Moves the last digit of an integer to the front
    last_digit = number % 10
    remaining = number // 10
    encrypted = int(str(last_digit) + str(remaining))
    return encrypted


# --------------------------------------------------------
# 6. Loops
# --------------------------------------------------------

def power(x, y):
    #Computes x raised to the power of y
    result = 1
    for i in range(y):
        result *= x
    return result

def min_for_loop(numbers):
    #Finds the minimum value in a list
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def max_for_loop(numbers):
    #Finds the maximum value in a list 
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def min_while_loop(numbers):
    #Finds the minimum value in a list
    i = 0
    minimum = numbers[0]
    while i < len(numbers):
        if numbers[i] < minimum:
            minimum = numbers[i]
        i += 1
    return minimum

def max_while_loop(numbers):
    #Finds the maximum value in a list
    i = 0
    maximum = numbers[0]
    while i < len(numbers):
        if numbers[i] > maximum:
            maximum = numbers[i]
        i += 1
    return maximum

def sum_of_digits(n):
    #Returns the sum of digits of an integer
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


number = 36912
result = secret_code(36912) #Moves last digit to the front of the number
print(f"The result of Secret Code (5.4) with number = {number} is {result}.")