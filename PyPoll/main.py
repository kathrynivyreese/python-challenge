import csv

# Specify the path to the CSV file
file_path = './Resources/election_data.csv'

# Initialize some variables
total_count = 0
count_dict = {}

# Open the CSV file
with open(file_path, 'r') as file:
    with open ("./Analysis/analysis.txt", "w") as output:
        reader = csv.reader(file)
        #skip header 
        next(reader)

        print ("Election Results")
        output.write("Election Results\n")

        # Iterate over each row in the CSV file
        for row in reader:
            candidate_row = row[2]
            total_count += 1
            if candidate_row in count_dict:
                count_dict[candidate_row] += 1
            else:
                count_dict[candidate_row] = 1

        # print all the info
        print(f"Total votes: {total_count}")
        print(count_dict)
        most_common_value = max(count_dict, key=count_dict.get)
        print(f"Winner: {most_common_value}")
        #format txt
        output.write(f"Total votes: {total_count}\n")
        output.write(str(count_dict))
        output.write('\n')
        output.write(f"Winner: {most_common_value}\n")


#Saving for future reference, this is another way to find the unique candidate names.      
#candidate_names = set()
#candidate_names.add(candidate_row)
#print(candidate_names)