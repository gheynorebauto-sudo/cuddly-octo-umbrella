# Task 1: The Basic Calculator

# Assign two different variables a and b
a = 67
b = 5

# Basic arithmetic operations
print("a =", a, ", b =", b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Floating-Point Division:", a / b)
print("Integer Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Task 2: The Order of Operations Challenge

# Expressions
result1 = 7 + 2 * 2 ** 2
result2 = (5 + 2) * 2 ** 2
result3 = 8 % 3 + 5 * 3

# Display results
print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)

# Task 3: Unit Conversion Challenge

inches = int(input("Enter the number of inches: "))

feet = inches // 12
remain = inches % 12

print(inches, "inches is equal to", feet, "feet and", remain, "inches.")

# Task 4: The Movie Ticket Price Decider

age = int(input("Enter your age: "))
is_student = input("Are you a student? (True/False): ")

# Convert input to boolean
is_student = is_student == "True"

price = 12  # base price

# Apply only the best discount
if age <= 12:
    price -= 3
elif age >= 65:
    price -= 4
elif is_student:
    price -= 2

print("Your ticket price is $", price, sep="")

# Task 5: Secure System Login Simulator

# Correct login details
username = "Gheynor"
password = "gheynor123"
is_2fa_enabled = True
correct_2fa_code = "123456"

# User inputs
input_username = input("Enter username: ")
input_password = input("Enter password: ")
input_2fa = input("Is 2FA enabled? (y/n): ")

# Convert user's answer to boolean
user_has_2fa = input_2fa.lower() == "y"

# If 2FA is enabled, ask for the code
if user_has_2fa:
    input_2fa_code = input("Enter 2FA code: ")
else:
    input_2fa_code = ""

# Login condition
if (input_username == username and
    input_password == password and
    (not is_2fa_enabled or input_2fa_code == correct_2fa_code)):
    print("Login successful!")
else:
    print("Login failed!")

    # Bonus Challenge Problem: The Shipping Cost Calculator with Rules

# User inputs
weight = float(input("Weight (lbs): "))
destination = input("Destination (domestic/international): ").lower()
membership = input("Membership (standard/premium): ").lower()

# Base shipping cost
cost = 10
details = "Base $10"

# Add $5 if weight is over 20 lbs
if weight > 20:
    cost += 5
    details += " + Overweight $5"

# Check for international shipping
if destination == "international":
    if membership != "premium":  # standard members pay double
        cost *= 2
        details += ", International fee applied"
    else:
        details += ", International fee waived"

# Apply premium discount
if membership == "premium":
    discount = cost * 0.20
    cost -= discount
    details += ", Premium 20% discount applied"

# Display final result
print(f"Final Shipping Cost: ${cost:.2f}")
print("(Details:", details + ".)")

    