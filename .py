# greeting.py
print("Hello! My name is shiva sai.")
print("Welcome to learning Python.")


# my_script.py

# This line prints my name
print("My name is Alex")

# This line prints a custom message
print("I am learning Python today!")


# rectangle.py

length = 10
width = 5

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)



# compare.py

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater.")
elif a < b:
    print("Second number is greater.")
else:
    print("Both numbers are equal.")  



# leap_year.py

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")




# concatenate.py

first_name = "Shiva"
last_name = "Sai"
full_name = first_name + " " + last_name

print("Full name:", full_name)

