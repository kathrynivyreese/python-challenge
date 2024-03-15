import csv

# Specify the path to the CSV file
file_path = './Resources/election_data.csv'

# Initialize some variables
total_count = 0
candidate_names = set()

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
            candidate_names.add(row[2])
            total_count += 1
    print(f"Total votes: {total_count}")
    print(candidate_names)
    #output.write("Total votes: {total_count}\n")

    
    
    # Extract the value from the desired column (e.g., column index 2)
    #value = row[2]









        # Add the value to the set to keep only unique values
    #unique_values.add(value)

# Print the unique values
#for value in unique_values:
    #print(value)

    #create another loop to find the unique names of candidates, and their total votes
    #for i in range(2, len(data_points)):
        #if data_points[i] != data_points[i-1]:
            #candidate_name = (i, 2).value
            #print(f"{candidate_name}")
        #end if

            
    















##import csv

# Read the CSV file
#election_data = './Resources/election_data.csv'
#with open(election_data, 'r') as file:
#unique_values = set()
    #with open ("./Analysis/analysis.txt", "w") as output:
        #reader = csv.reader(file)
    
        # Skip the header row
        #next(reader)
        
        #for row in reader:
        # Extract the value from the desired column (e.g., column index 2)
        #value = columns[2]
        # Add the value to the set to keep only unique values
        #unique_values.add(value)

        # Print the unique values
    #For value in unique_values:
    #print("{value}")



            # Extract name values from the third column
            #candidate_names = [row[2] for row in reader]

            #Find total number of votes cast, votes in column 1 
            #total_votes = len(list(reader))
            #print ("Total Votes: {total_votes}")
            # These next functions can run in the same loop?
            #List the candidates who recieved votes
            #percentage of votes per candidate
            #number of votes per candidate
            #print ("{name}: {percent_won} ({vote_count})")
            
            
            #winner of the election
            #












#print ("Winner: {name_of_winner}")

