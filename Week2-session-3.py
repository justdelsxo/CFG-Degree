# If statements

# Simple true/false if statements
name= "Kate"

if name == "Kate":
    print("Hello Kate")

if name == "Jenny":
    print("Access denied!")

# Temp example to show comparative operators
temp = 30
print(temp>20)

is_sunny = True

go_to_the_beach = (temp > 30) and is_sunny

print("Should i go to the beach: ", go_to_the_beach)

 Should i go to the beach:  False

if (temp >= 30) or is_sunny:
    print(go_to_the_beach)

 If statement challenge -

    age = int(input("How old are you?"))
    if age >= 13:
        print("Access granted")
    else:
        print("Access denied")

#if-elif-else handles multiple conditions
# check first condition with if
# check additional conditions with elif
#optional "else" for when no conditions are true

# weather recomendations app: what to wear for diff temps

temperatures=10
if 0 <= temperatures < 10:
    print("Its cold ; wear big jacket")
elif 10 <= temperatures < 20:
    print("It's chilly; wear light jacket")
elif 20 <= temperatures < 30:
    print("It's pretty warm; T-shirt away")
elif 30 <= temperatures <= 50:
    print("It's TOO HOT; Don't go out!!")
else:
   print("I have no idea what you should wear")

# Weather Activity Recommender
#
# Create a program that:
# 1. Asks the user for today's weather (sunny, rainy, or snowy)
# 2. Uses if-else to recommend an appropriate activity
# 3. Tells the user to have a great day
#
# This provides a practical, relatable example for if-else statements.
# """

# Instructions for students:
# 1. Ask the user for the current weather
# 2. Based on their input, recommend a suitable activity
# 3. Handle invalid inputs with a default message

weather = input("Whats is the weather like? ")
if weather.lower() == "sunny":
    print("Go for a swim")
elif weather.lower() == "rainy":
    print("Stay inside")
elif weather.lower() == "snowy":
    print("Go outside and make snow angels")
else:
    print("I dont understand, please try inputting something else")

#Meal Recommendation System

#Create a program that recommends what to eat based on the time of day.
#The program will:
#1. Ask the user for the current time (in hours, using 24-hour format)
#2. Recommend a meal or snack based on the time
#3. Add a friendly message with the recommendation

# Instructions for students:
# 1. Ask the user for the current time in hours (0-23)
# 2. Convert the input to an integer
# 3. Use if-elif-else to recommend different meals based on time ranges
# 4. Include a default option for unusual times

# Solution HERE

time = int(input("What time isit? "))
if 0 <= time < 10:
    print("Maybe have some cereal or oats")
elif 10 <= time < 15:
    print("Its lunchtime! maybe have a burrito bowl")
elif 15 <= time < 20:
    print("It's dinnertime! I suggest protein and veggies")
else:
    print("Its too late to eat")

#palindrome check