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
