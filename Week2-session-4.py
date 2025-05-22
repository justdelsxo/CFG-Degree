# Lists and dictionaries

# Lists
# List1 = [1,2,3,4,5]
# List2 = [Molly,Lena,Sylvan,Sarah]
#List3 = ["molly", "Lena" , "Sylvan", "Sarah"]
# Person = ["Jess", 32, True]

# Lists can be changed!

# food = ["Salmon", "Seabass", "Cake", "Cheese"]
# print(food[1])

# List function

# grades = [33,58,34,78,55]
# print(max(grades))
# print(min(grades))
# print(len(grades))
# print(sorted(grades))
# print(reversed(grades))

# numbers = [5,3,5,7,4,3]
# numbers.append(666)
# print(numbers)

# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
# total_cost = 0

# costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
#
# total_cost = 0
# for cost in costs:
#     total_cost += cost
#
# print("Total spent on lunch: £", round(total_cost, 2))

#Dictionaries
# Car1 = {colour: "red"
#         year: 2024
#         make: "ford"}


# Person = {"name": "Adele",
#           "language": "English",
#           "eyes": "brown",
#           "country": "Grenada",
#           "likes": ["music","sports", "gym", "tech"]
# }
#
# speak = Person["language"]
# print("What language do you speak? ", speak)
#
# hamed_car = {
#     "colour": "red",
#     "year": 2020,
#     "price": 300.25,
#     "is_still_working": True,
#     "condition_of_wheels": ["good", "okay", "bad", "DEAD"],
#     "current_location": {
#         "lat": 12.2323,
#         "lng": 63.222
#     }
# }
#
# location = hamed_car["current_location"]["lat"]
# print(location)

# fruits = [
#     {'name': 'apple', 'colour': 'red', 'price': 0.12},
#     {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
#     {'name': 'pear', 'colour': 'green', 'price': 0.19},
# ]
#
# total = 0
# for fruit in fruits:
#     print(fruit["price"])
#     total += fruit["price"]
#
# print(total)

# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     print(fruit)

# numbers = [10, 20, 30, 40]
# total=0
# for number in numbers:
#   total += number
#   print("Total",total)

# for i in range(1, 6):
#     print(i)

# nums = [2, 5, 8, 3, 10, 7]
#
# for num in nums [0:0:2]:

# numbers = [1, 2, 3, 4, 5]
#
# for number in numbers:
#     number *= 2
#     print(number)

# Your task: Print each number multiplied by 2

# Your task: Complete this code
# number = int(input("Enter a number: "))
# even = number % 2
# Write an if statement to check if it's even or odd

# if number = even:
#     print("Even")
# else:
#     print("Odd")

# Your task
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Access granted")
# else:
#     print("Access denied")

# Write the if/else statement here


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("positive")
elif num not % 2:
    print("negative")
elif num == 0:
    print("zero")
else:
    print("error")

# Write an if...elif...else statement to check if a number is positive, negative, or zero
# Write the conditions here