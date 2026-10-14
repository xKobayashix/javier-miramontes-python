# Section 1: Variables and Types - Declaring one variable of each of the four basic types below, one can print each variable along with its type 
name = "Javier"
age = 21
height = 5.5
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# Section 2: User Input and Math: This is my code for this section

name = input("What is your name? ")
birth_year = int(input("What year were you born in? "))

age = int(input("What is your age? "))

print(name, type(name))
print("Hi, everyone! This is", name + "! He is", age, "years old.")

# Section 3 and 4: Type Conversion and f-strings and Formatted Receipt

# Store items 

item_name = "Binder"
price = 5.60
quantity = 10

# Computing the total amount
total = price * quantity 

print("======== RECEIPT ========")
print(f"Item:       {item_name}")
print(f"Price:      ${price:.2f}")
print(f"Quantity:   {quantity}")
print("-------------------------")
print(f"Total:      ${total:.2f}")
print("=========================")

# Section 5: Mini-Project - Profile Card

# This is my code for the professional profile card

name = input("What is your name? ")
hometown = input("Where is your hometown? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input("Tell me one fun fact about yourself: ")
birth_year = int(input("What year were you born in? "))

current_year = 2026
age = current_year - birth_year
print(f"age       {age}")

print()

print("=" * 40)
print("               PROFILE CARD            ")
print("=" * 40)
print(f"Name:                           {name}")
print(f"Age:                            {age}")
print(f"Hometown:                       {hometown}")
print(f"Hobby:                          {hobby}")
print(f"Fun fact:                       {fun_fact}")
print("=" * 40)
