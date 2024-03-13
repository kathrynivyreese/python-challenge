#import os
import csv

data_csv = "./Resources/budget_data.csv"
with open (data_csv, 'r') as file:
    with open ("./Analysis/analysis.txt", "w") as output:
        reader = csv.reader(file)
        #skip header
        next(reader)

        print ("Financial Analysis")
        output.write("Financial Analysis\n")

        #find total number of months
        #loop the total in the same sequence
        #variable to store month info
        data_points = []
        num_months = 0
        total_sum = 0
        for row in reader:
            num_months += 1
            Value = int(row[1]) 
            total_sum += Value
            data_points.append (Value)
        print (f"Total Months: {num_months}")
        print (f"Total: ${total_sum}")
        output.write(f"Total Months: {num_months}\n")
        output.write(f"Total: ${total_sum}\n")

        # calculate average change
        changes = [data_points[i] - data_points[i-1] for i in range(1, len(data_points)) ]
        average_change = sum(changes) / len(changes)
        rounded = round(average_change, 2)
        print(f"Average Change: ${rounded}")
        output.write(f"Average Change: ${rounded}\n")

        # calculate greatest increase
        greatest_increase = 0
        for i in range(1, len(data_points)):
            increase = data_points[i] - data_points [i - 1]
            if increase > greatest_increase:
                greatest_increase = increase
        #we need something here to print the corresponding month. Maybe the enumerator function?
        print(f"Greatest Increase in Profits: (${greatest_increase})")
        output.write(f"Greatest Increase in Profits: ${greatest_increase}\n")
        
        #greatest decrease in profits
        greatest_decrease = 0
        for j in range(1, len(data_points)):
            decrease = data_points[j] - data_points[j-1]
            if decrease < greatest_decrease:
                greatest_decrease = decrease
        print(f"Greatest Decrease in Profits: (${greatest_decrease})")
        output.write(f"Greatest Decrease in Profits: ${greatest_decrease}\n")
