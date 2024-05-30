# Write a program to input the age of a user and let them know if they have diabetes risk or not. 
#Use case is that a user with age more than or equal to 65 is at risk else not.
age = 55
if age >= 65
  print("Risky") 
else
  print("Not Risky") 

# WAP to calculate the GST of two products, apple and pie
# apple has 10% GSt and pie has 8%
# Apple gross sale is $75, pie gross is $100
# GST for apple is .10 * 75
# Gst for pie is .08 * 100\

apple = 75
pie = 100
gst_apple = 0.1 * apple
gst_pie = 0.08 * pie
print(gst_apple)
print(gst_pie)

# WAP to calculate the minis in the maxis
# total maxis is 2.5 * minis
# 1 minis is 5000
# calculate how much is 4.5 maxis

minis = 5000
maxis = 2.5 * minis
print(" The require value is:", 4.5*2.5*minis)
\

bits = 1
bytes = 8*bits
kilo_bytes = 1024*bytes
mega_bytes = 1024*kilo_bytes
giga_bytes = 1024*mega_bytes
tera_bytes = 1024*giga_bytes
print("the memory allocation units are as follows: ")
print("1.", bits, "2.", bytes, "3.", kilo_bytes, "4.", mega_bytes, "5.", giga_bytes, "6.", tera_bytes)


# Write a program to find the area of a circle
Input radius of a circle, radii
pi = 3.14
Area = pi * (radii)^2
Display Area

# Ask the user to enter the projected amount of total sales
total_sales = float(input("Enter the projected amount of total sales: "))

# Calculate the profit
profit_percentage = 0.23
profit = total_sales * profit_percentage

# Display the profit
print(f"The projected profit is: ${profit:.2f}")


# Constant for the number of square feet in one acre
SQUARE_FEET_PER_ACRE = 43560

# Ask the user to enter the total square feet in a tract of land
total_square_feet = float(input("Enter the total square feet in the tract of land: "))

# Calculate the number of acres
number_of_acres = total_square_feet / SQUARE_FEET_PER_ACRE

# Display the number of acres
print(f"The number of acres in the tract of land is: {number_of_acres:.2f}")




# Set Value for the sales tax rate
tax_rate = 0.07

# Ask the user for the price of each item
p1 = float(input("Enter the price of first product: "))
p2 = float(input("Enter the price second product: "))
p3 = float(input("Enter the price of third product: "))
p4 = float(input("Enter the price of fourth product: "))
p5 = float(input("Enter the price of fifth product: "))

# Calculate the subtotal
subtot = p1 + p2 + p3 + p4 + p5

# Calculate the sales tax
tax = subtot * tax_rate

# Calculate the total
total = subtot + tax

# Display the results
print(f"Subtotal: ${subtot:}")
print(f"Sales Tax: ${tax:}")
print(f"Total: ${total:}")
