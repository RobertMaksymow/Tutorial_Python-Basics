# A simple program to practice data types

# Get user input (input is always a string)
name = input("Enter your name: ")
age_str = input("Enter your age: ")

# Convert age to an integer
age = int(age_str)

# Perform a simple calculation
years_to_100 = 100 - age
is_adult = age >= 18

# Create an output message using an f-string
output = f"""
--- User Information ---
Hello, {name}!
You are {age} years old.
You will be 100 years old in {years_to_100} years.
Are you an adult? {is_adult}
--- End of Report ---
"""

# Print the final result
print(output)