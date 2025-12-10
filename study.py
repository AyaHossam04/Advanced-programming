# class Person:
#     def __init__(self, name="Esmak", age="senak"):
#         self.name = name
#         self.age = age
        
# p1 = Person("Aya", 21)
# print(p1.name,",", p1.age)


# class Operator:
#     def __init__(self, value1, value2):
#         self.value1 = value1
#         self.value2 = value2
#     def __mul__(self):
#         return self.value1 * self.value2 
#     def __str__(self):
#         return str(self.__mul__())
    
# x = Operator(2, 3)
# print(x)


# def __mul__(self, other):
#     return self * other
# x = 5
# result = x.__mul__(2)
# print(result)

# ages = [5, 12, 17, 18, 24, 32]
# adults = list(filter(lambda x : x >= 18, ages))
# print(adults)

# def number_generator(n):
#     for i in range(n):
#         yield i
# gen = number_generator(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def decorator(func):
#     def wrapper():
#         print("Before function execution")
#         func()
#         print("After function execution")
#     return wrapper
# # def greet():
# #     print("Hello!")
# # result = decorator(greet)
# # result()
# @decorator
# def greet():
#     print("Hello!")
# greet()


# import re

# text = "The price of the item is $20.99"
# pattern = r'\d+'
# matches = re.findall(pattern, text)
# print(matches)

# text = "The quick brown fox jumps over the lazy dog"
# pattern = r'\bthe\b'
# matches = re.findall(pattern, text, re.IGNORECASE)
# print(matches)

# text = "The quick brown fox jumps over the lazy dog"
# pattern = r'\bfox\b'
# match = re.search(pattern, text)
# if match:
#     print(f"Found '{match.group()}' starting at position {match.start()}")
# else:
#    print("No match found")

# text = "The quick brown fox jumps over the lazy dog"
# pattern = r'\s+'
# words = re.split(pattern, text)
# print(words)

# text = "The quick brown fox jumps over the lazy dog"
# pattern = r'\bthe\b'
# new_text = re.sub(pattern, 'a', text, count=2, flags=re.IGNORECASE)
# print(new_text) 


# import pandas as pd

# data = [1, 2, 3, 4, 5]
# series_from_list = pd.Series(data)
# print(series_from_list)
# data = {'a': 1, 'b': 2, 'c': 3}
# series_from_dict = pd.Series(data)
# print(series_from_dict)
# data = [1, 2, 3, 4, 5]
# index = ['a', 'b', 'c', 'd', 'e']
# series_custom_index = pd.Series(data, index=index)
# print(series_custom_index)

# data = {'Name': ['John', 'Alice', 'Bob'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'LosAngeles', 'Chicago']}
# df = pd.DataFrame(data)
# print(df)
# data = [['John', 25, 'New York'],
#     ['Alice', 30, 'Los Angeles'],
#     ['Bob', 35, 'Chicago']]
# columns = ['Name', 'Age', 'City']
# df = pd.DataFrame(data, columns=columns)
# print(df)

# import pymysql

# connection = pymysql.connect(
#     host='localhost',
#     user='username',
#     password='password',
#     db='database_name' )

# cursor = connection.cursor()

# sql = """
#     CREATE TABLE users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     email VARCHAR(255) ) """
# cursor.execute(sql)
# connection.commit()
# # Print the results
# print("Table created successfully.")
# # Close the connection
# connection.close()


# print("Bytecode : ")

# def square(x):
#     return x * x

# def multiply(a, b):
#     return a * b

# def add(a, b):
#     return a + b

# print(f"square(5) = {square(5)}")
# print(f"multiply(3, 4) = {multiply(3, 4)}")
# print(f"add(2, 3) = {add(2, 3)}")



# print()
# print("Dynamic typing: ")

# data = 42
# print(f"First, data = {data} (it's an {type(data)})")

# data = [1, 2, 3]
# print(f"Now, data = {data} (it's a {type(data)})")

# def my_func():
#     pass

# data = my_func
# print(f"Finally, data = {data} (it's a {type(data)})")



# print()
# print("Mutability and object identity: ")

# my_list = [10, 20, 30]
# print(f"my list now: {my_list}")

# first_address = id(my_list)
# print(f"Memory address: {first_address}")

# my_list.append(40)
# print(f"Adding 40: {my_list}")

# second_address = id(my_list)
# print(f"Memory address now: {second_address}")

# if first_address == second_address:
#     print("✓ Same address! Lists keep their home when you add items.")
# else:
#     print("✗ Different address!")
# print()


# PART 1: Vector3D Class
print("Vector3D Class:")

class Vector3D:    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

print("Creating two vectors:")
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
print(f"v1 = {v1}")
print(f"v2 = {v2}")

print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * v2 = {v1 * v2}")


# PART 2: Positive Number Descriptor
print()
print("Positive Number Descriptor: ")

class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance 
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            print("ERROR: Balance can't be negative!")
        else:
            self._balance = value
    
    def withdraw(self, amount):
        if self._balance - amount < 0:
            print(f"ERROR: Can't withdraw ${amount}. Only ${self._balance} available.")
        else:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")

account = BankAccount(100)
print(f"Starting balance: ${account.balance}")
account.withdraw(50)  
account.withdraw(60)  
account.balance = -20 


# # PART 3: Point Class with _slots_
print()
print("Point Class with __slots__: ")

class Point:
    __slots__ = ('x', 'y') 
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

print("Creating a point at (3, 4):")
p = Point(3, 4)
print(f"Point: {p}")
print(f"p.x = {p.x}")
print(f"p.y = {p.y}")

try:
    p.z = 5
    print("Successfully added z attribute!")
except AttributeError as e:
    print(f"Failed to add z: {e}")
    print("Why? Because _slots_ restricts us to only x and y!")
    

# # PART 4: Disassembling Functions
print()
print("Disassembling a simple function: ")

def calculate_sum(a, b):
    return a + b

print(f"sum of 2 and 3 is {calculate_sum(2, 3)}")
print("Function: calculate_sum(a, b)")
print("What it does: returns a + b")

import dis

print("\n(bytecode):")
dis.dis(calculate_sum)
print(f"calculate_sum(5, 3) = {calculate_sum(5, 3)}")

print("\nWhat the bytecode means:")
print("- LOAD_FAST: Loads a variable onto the stack (like getting a value ready)")
print("- BINARY_ADD: Takes two values from stack, adds them, puts result back")
print("- RETURN_VALUE: Returns the result from the function")


