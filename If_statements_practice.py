#Ask for a score out of 100. Print the grade based on this scale:

# 90+ → A
# 80–89 → B
# 70–79 → C
# 60–69 → D
# Below 60 → Fail

# score = int(input("Enter your score (0–100): "))
#
# if score < 60:
#     print("fail")
# elif 60 <= score <= 69:
#     print("D")
# elif 70 <= score <= 79:
#     print ("C")
# elif 80 <= score <= 89:
#     print ("B")
# elif score >= 90:
#     print ("A")
# else:
#     print ("error")

# Ask the user for a number. Print:
#
# "FizzBuzz" if the number is a multiple of both 3 and 5,
# "Fizz" if it’s just a multiple of 3,
# "Buzz" if it’s just a multiple of 5,
# Otherwise, print the number.

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)

