# File: homework1.py

# --- Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # float, decimal number

c = 3j
print(c)
print(type(c)) # complex number

d = "hello"
print(d)
print(type(d)) # string, sequence of characters

e = [1, 2, 3]
print(e)
print(type(e)) # list, ordered collection

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # dictionary, key-value pairs

g = (1, 2)
print(g)
print(type(g)) # tuple, immutable ordered collection

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # list, collection of words

i = True
print(i)
print(type(i)) # boolean, conditional statement

j = None
print(j)
print(type(j)) # NoneType, represents no value

k = [True, "blue", 12]
print(k)
print(type(k)) # list with mixed data types

l = str(14)
print(l)
print(type(l)) # string, str() converts integer to string

m = 1e4
print(m)
print(type(m)) # float, scientific notation

# Questions:
# 1. There are 9 different data types.
# 2. int, float, complex, str, list, dict, tuple, bool, NoneType
# 3. e, h, and k are the same. d and l are the same. b and m are the same
# 4. l is a string, because str() converts 14 into "14", so it is no longer just an integer
# 5. Example of another type:
n = {1, 2, 3}
print(n)
print(type(n)) # set of unique values


# --- Booleans ---

print(10 > 9)  # True, 10 is greater than 9
print(10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not less than 9
print(bool("abc")) # True, non-empty string
print(bool(123)) # True, non-zero number
print(bool(["apple", "cherry", "banana"])) # True, non-empty list
print(bool(True)) # True
print(bool(False)) # False
print(bool(0)) # False because it is zero
print(bool("")) # False, empty string
print(bool(" ")) # True, space counts as a character
print(bool(())) # False, empty tuple
print(bool([])) # False, empty list
print(bool({})) # False, empty dictionary
print(bool(True and False)) # False because it cannot be True anymore
print(bool(True and True)) # True because both are True
print(bool(False and False)) # False because both are False
print(bool(True or False)) # True because it has an option to be True
print(bool(True or True)) # True, only option
print(bool(False or False)) # False, only option
print(bool(not(False))) # True, cancels out
print(bool(not(True))) # False, no longer True

# Questions:
# I noticed that non-empty values are True while empty or zero values are False.
# It was surprising to see bool(" ") was True, but it makes sense because space is still a character.
# print(5 < 10) # True, because 5 is less than 10
# print(100 < 50) # False, because 100 is not less than zero


# --- Operators ---

# Arithmetic Operators
print(10 + 5)  # 15, + performs addition
print(10 - 5)  # 5, performs subtraction
print(2 * 4)   # 8, performs multiplication
print(6 / 3)   # 2.0, performs division
print(5 % 2)   # 1, gives remainder
print(3 ** 2)  # 9, exponent
print(15 // 2) # 7, floor division, leaving out remainder

# Comparison Operators
print(5 == 2)  # False, 5 is not equal to 2
print(10 != 10) # False, evaluates if two values are equal
print(2 < 5)   # True, 2 is less than 5
print(12 > 5)  # True, 12 is greater than 5
print(5 <= 6)  # True, 5 is less than or equal to 6
print(1 >= 10) # False, 1 is not greater than or equal to 10

# Assignments Operators
x = 5
x += 5
print(x) # 10, add two values and assign the sum to variable
x -= 4
print(x) # 6, subtract from value and assign to variable
x *= 3
print(x) # 18, multiply value and assign to variable

# Logical Questions:
# 1.  and returns True if both sides are True
print(True and True) # True
print(True and False) # False

# 2.  or returns True if at least one side is True
print(True or False) # True
print(False or False) # False

# 3. not reverses True and False
print(not False) # True
print(not True)  # False

# More Questions:
# 1. / gives float division, while // gives integer (whole number) division
# 2. % gives the remainder, and // gives the quotient
# 3. You would use % to calculate remainder, 10 % 3 = 1
# 4. Assignment operators use the variable previously given and update the variable in place


# --- Strings ---
my_string = "hello"
print(my_string)       # Prints: hello
print(my_string[0])    # Prints: h, first letter of string
print(my_string[1])    # Prints: e, second letter of string
print(my_string[2])    # Prints: l, third letter of string
print(my_string[3])    # Prints: l, fourth letter
print(my_string[4])    # Prints: o, fifth letter
print(my_string[-1])   # Prints: o, sixth letter
print(my_string[1:3])  # Prints: e, second and third letters
print(my_string[0:5:2]) # Prints: hlo, every other letter
print(len(my_string))  # Prints: 5, length of string
print(my_string + "goodbye") # Prints: hellogoodbye, adds to the string
print(my_string * 7)   # Prints: hellohellohellohellohellohellohello, repeats it 7 times

# Questions:
# 1. Slicing is taking a part of a sequence using the start, end, and step. We sliced using [1:3] and [0:5:2]

# 2.
name = "Oski"
print("Hello, my name is", name) # prints with space: Hello, my name is Oski

# 3.
name = "Oski"
print(f"Hello, my name is {name}") # prints f-string: Hello, my name is Oski

# The difference is that f-strings are formatted directly inside the string


# --- Terminal Commands ---

# 1. cd 
# changes directories, use it to move from one folder to another
# Example: cd Desktop

# 2. ls 
# lists files
# Example: ls 

# 3. ls -a 
# lists all files, including hidden files
# Example: sls -a

# 4. mkdir 
# makes directory
# Example: mkdir test

# 5. cat 
# prints contents of file
# Example: cat homework1.py

# 6. pwd 
# prints working directory
# Example: pwd

# 7. cd .. 
# moves up one folder
# Example: cd ..

# 8. cd . 
# stay in same directory
# Example: cd .

# 9. cd ~ 
# go to home directory
# Example: cd ~

# 10. cp 
# copies file
# Example: cp file1.py file2.py

# 11. mv
# move/rename file
# Example: mv file1.py file2.py

# 12. rm 
# remove file
# Example: rm file.py

# 13. clear
# clear terminal screen
# Example: clear

# 14. grep 
# search text inside file
# Example: grep "hello" homework1.py

# Questions:
# 1.
#  1) touch - creates empty file, call: touch newfile.py
#  2) head - shows first lines of file, call: head homework1.py
#  3) tail - shows last lines of file, call: tail homework1.py
#
# 2. The difference between ls and ls -a is that ls -a shows hidden files.

# 3. A hidden file is a filename starting with a "."
#
# 4.
# 1) ls -l is a long listing format with file details, call: ls -l
# 2) ls -h is human-readable sizes so file sizes show in KB, MB, etc, call: ls -lh
# 3) rm -r is recursive delete for a folder and deletes everything inside of it, call: rm -r folder