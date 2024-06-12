import pandas as aa # import pandas package
data = aa.read_csv("blood_pressure.csv") # import the csv file
print("The orignal data set is: ") # print the statement
print(data.head()) # print first five lines of the data
avg_systolic = data["Systolic"].mean()
print ("the mean of systolic is", avg_systolic)
med_systolic = data["Systolic"].median()
print ("The median of systolic is", med_systolic)
range_systolic = data["Systolic"].max() - data["Systolic"].min()
print ("The range of systolic is", range_systolic)
