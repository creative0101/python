# Replace every number divisible by 3 with Fizz and 5 with Buzz in a range of 100

for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
