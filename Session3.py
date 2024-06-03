# The if else statement
wthr = input("What's the weather like today (Hot, Cold): ") # get input from the user
if wthr == "Hot": # check the user input comparing with a string
    print("Stay home and have cold drinks") # If the above condition is satisfied, print the result
else:
    print("Put on some clothes") # If the check condition is not satisfied, print the result

# The if else statement
wthr = input("What's the weather Outside (Cloudy, Foggy): ") # get input from the user
if wthr == "Cloudy": # check the user input comparing with a string
    print("It's going to rain) # If the above condition is satisfied, print the result
else:
    print("Be safe while driving") # If the check condition is not satisfied, print the result

#Nested Decision Structures (if-elif-else)
Score = int(input("Enter your score: ")) #take input from the user
if score < 50: # Compare the input with first condition
    print("You've failed") # if the condition above is satisfied, print the result
elif score <= 65: # if the first condition is not satisfied, check this condition
    print("You've got the pass grade") # if second condition is satisfied, print the result
elif score <=75:  # if the first and secod condition is not satisfied, check this condition
    print("You've got the credit grade") # if third condition is satisfied, print the result
elif score <= 85:  # if the first, second and third condition is not satisfied, check this condition
    print("You've got a distinction") # if fourth condition is satisfied, print the result
else:
    print(Congratulations !! You've got high distinction")  #if the the above conditions are not satisfied, print the result

# logical operators
a_stdnt = input("Are you a student (True or False): ") # ask the user to get input if he is a student
an_id = input("Do you have an ID (True or False): ") # ask the user if he has an ID
if a_stdnt and an_id: # use logical operator and to check the condition
    print("You can get concessions") # print the statement if the above condition is satisfied

c =1
while c <=5:
    print(f"Counting...{c}")
    c += 1

# The For loop
contis = ["asia", "Australia", "Antartica", "north america", "south america", "Europe","africa"]
for conti in contis:
    print(f"I like to go to {conti}!")


# The For loop
contis = ["asia", "Australia", "Antartica", "north america", "south america", "Europe","africa"]
imfrom = ["asia"]
for conti in contis:
    print(f"I like to go to {imfrom}!")

# Calculating a running total
total = 0
for num in range(1,50):
    total += num
    print(f"current total: {total}")


