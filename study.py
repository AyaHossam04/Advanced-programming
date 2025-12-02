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

import pymysql

connection = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    db='database_name' )

cursor = connection.cursor()

sql = """
    CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) ) """
cursor.execute(sql)
connection.commit()
# Print the results
print("Table created successfully.")
# Close the connection
connection.close()