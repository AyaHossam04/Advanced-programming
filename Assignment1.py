#1 clean data
products = [" LAPTOP", "phone ", " Tablet", "CAMERA "]
clean_products = list(map(lambda x: x.strip().title(), products))
print(clean_products)

#2 temprature
cel = [0, 10, 20, 30, 40]
fahr = list(map(lambda x: (x * 9/5) + 32, cel))
print(fahr)

#3 multiple
nums = [1, 2, 3, 4, 5]
transformed = list(map(lambda x: x*x + 10, nums))
print(transformed)

#4 first and last char
words = ["python", "lambda", "programming", "map", "function"]
first_last = list(map(lambda x: (x[0] , x[-1]), words))
print(first_last)

#5 nested map
marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]
new_marks = list(map(lambda row: list(map(lambda x: round(x * 1.05), row)), marks))
print(new_marks)

#6 normalize
nums = [10, 20, 30, 40, 50]
max_num = max(nums)
min_num = min(nums)
normalized = list(map(lambda x: (x - min_num) / (max_num - min_num), nums))
print(normalized)

#7 length of word
sentences = [
    ["Hello", "world"],
    ["Python", "is", "fun"],
    ["Map", "and", "Lambda"]
]
lengths = list(map(lambda s: list(map(lambda w: len(w), s)), sentences))
print(lengths)
