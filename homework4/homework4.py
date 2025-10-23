# File: homework4.py

# -------------------------------------------------
# 1. DEBUGGING EXAMPLES
# -------------------------------------------------
print("Hello, World!")

"""
Error Example 1:
TypeError: can only concatenate str (not "int") to str
I tried: print("Number: " + 5)
Fixed by converting 5 -> str(5)
"""

# print("Number: " + 5)  # ❌ causes error
print("Number: " + str(5))  # ✅ fixed

"""
Error Example 2:
IndexError: list index out of range
I used my_list[10] on a list with only 5 items.
Fixed by checking length with len(my_list)
"""

my_list = [1, 2, 3, 4, 5]
if len(my_list) > 10:
    print(my_list[10])
else:
    print("Index too large!")  # ✅ fixed with condition

"""
Error Example 3:
NameError: name 'numbres' is not defined
I spelled 'numbers' wrong.
Fixed by using correct variable name.
"""

# numbres = [1, 2, 3]
numbers = [1, 2, 3]  # ✅ fixed


# -------------------------------------------------
# 3.1 LIST OPERATIONS
# -------------------------------------------------
foods = ["pizza", "cheeseburger", "pasta", "sandwich", "fruit"]

# 1. Print second food
print(foods[1])

# 2. Print last food using negative indexing
print(foods[-1])

# 3. Add new food
foods.append("burrito")

# 4. Insert "apple" at the start
foods.insert(0, "apple")

# 5. Remove third item
del foods[2]

# 6. Print length
print("List length:", len(foods))

# 7. Loop through list in uppercase
for food in foods:
    print(food.upper())

# 8. New list with first and last food
newfood = [foods[0], foods[-1]]
print("First and last foods:", newfood)

# 9. Check for "potato"
if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")


# -------------------------------------------------
# 3.2 SLICING AND STRIDING
# -------------------------------------------------
numbers = list(range(0, 21))

def get_first_15(numbers):
    return numbers[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    reversed_list = lst[::-1]
    return reversed_list[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

print("get_first_15:", step1)
print("get_every_5th:", step2)
print("reverse_and_stride:", step3)


# -------------------------------------------------
# 3.3 NESTED LISTS
# -------------------------------------------------
numbers_nested = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 1. Print third row
print(numbers_nested[2])

# 2. Print second item in second row
print(numbers_nested[1][1])

# 3. Add [10, 11, 12]
numbers_nested.append([10, 11, 12])
print(numbers_nested)

# 4. Sum all numbers
def sum_nested(lst):
    total = 0
    for row in lst:
        for num in row:
            total += num
    return total

print("sum_nested:", sum_nested(numbers_nested))


# -------------------------------------------------
# 3.4 CREATE 5x5 LIST
# -------------------------------------------------
def make_5x5():
    grid = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        grid.append(row)
    return grid

five_by_five = make_5x5()
print("5x5 List:", five_by_five)

def replace_multiples_of_3(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] % 3 == 0:
                lst[i][j] = "?"
    return lst

updated_grid = replace_multiples_of_3(five_by_five)
print("Grid with ? for multiples of 3:", updated_grid)

def sum_not_question(lst):
    total = 0
    for row in lst:
        for item in row:
            if item != "?":
                total += item
    return total

sum_result = sum_not_question(updated_grid)
print("Sum of non-? items:", sum_result)


# -------------------------------------------------
# 4. DICTIONARIES
# -------------------------------------------------
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

# 1. Print Katie's age
print("Katie's age:", ages["Katie"])

# 2. Change Mira's age to 100
ages["Mira"] = 100

# 3. Add Milana
ages["Milana"] = 52

# 4. Remove Mariam
del ages["Mariam"]

# 5. Print each person's name and age
for name, age in ages.items():
    print(name, "is", age, "years old")


# -------------------------------------------------
# 5. FAVORITE FUNCTION CALL (for VS Code screenshot)
# -------------------------------------------------
print("\n--- Favorite Function Example ---")
print("Sum of nested list:", sum_nested(numbers_nested))
