# Task 2: Variables, Data Types & Type Conversion

# 1. Create variables of different data types
age = 20                 # int
height = 5.9             # float
name = "Kapilan"         # string
is_student = True        # boolean

# 2. Print values and their data types
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print("Name:", name, "Type:", type(name))
print("Is Student:", is_student, "Type:", type(is_student))

print("\n--- Type Conversion ---")

# 3. String input from user
user_age = input("Enter your age: ")
print("User age type before conversion:", type(user_age))

# 4. Convert string to integer
user_age_int = int(user_age)
print("User age after conversion:", user_age_int)
print("Type after conversion:", type(user_age_int))

# 5. Convert integer to float
user_age_float = float(user_age_int)
print("Age as float:", user_age_float, "Type:", type(user_age_float))

# 6. Arithmetic operation using converted values
next_year_age = user_age_int + 1
print("Your age next year will be:", next_year_age)

print("\n--- Dynamic Typing Demo ---")

# 7. Dynamic typing demonstration
value = 10
print("Value:", value, "Type:", type(value))

value = "Ten"
print("Value:", value, "Type:", type(value))

value = 10.5
print("Value:", value, "Type:", type(value))
