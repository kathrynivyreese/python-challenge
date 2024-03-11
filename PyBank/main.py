import os
import csv

data_csv = os.path("./Resources/budget_data.csv")
with open (data_csv, 'r') as file:
    reader = csv.reader(file, delimeter=",")
    #skip header
    header = next(file)

Print ("Financial Analysis")

#find total number of months
#variable to store month info
num_months = 0
    for row in reader 
        num_months += 1
Print (f"Total Months: {num_months}")

#net profit or loss 

total_sum = 0
    for row in reader
    Value = int(row[1]) 
    total_sum += Value
    print (f"Total: {total_sum}")
    break

# calculate average change
    data_points = [float(row[1]) for row in reader]
    changes = [data_points[i] - data_points[i-1] for i in range(1, len(data_points)) ]

    average_change = sum(changes) / len(changes)
    print("Average Change: ${average_change}")

average_change = [abs(x - y) for x in data_points for y in data_points]

# Remove zero distances (distance between the same point)
distances = [dist for dist in distances if dist != 0]
average_distance = np.mean(distances)

print("Average distance between data points:", average_distance)

# calculate greatest increase
greatest_increase = 0
for i in range(1, len(data)):
    increase = data[i] - data [i - 1]
    if increase > greatest_increase:
        greatest_increase = increase
    break
#we need something here to print the corresponding month as well. Maybe the enumerator function?
print(f"Greatest Increase in Profits: (${greatest_increase})")

#greatest decrease in profits
greatest_decrease = 0
for j in range(1, len(data))
    decrease = data[j] - data [j-1]
    if decrease < greatest_decrease:
        greatest_decrease = decrease
    break
Print(f"Greatest Decrease in Profits: (${greatest_decrease})")

