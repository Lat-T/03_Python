
#------------------------------------
# Import the csv file
#------------------------------------
import os
import csv
csv_path = os.path.join("./PyPoll_data.csv")



#------------------------------------
# Create lists to store data
#------------------------------------
Source_Voter_ID = []
Source_County = []
Source_Candidate = []



#------------------------------------
# Append the values within the csv file to the previously created lists
#------------------------------------
with open(csv_path, newline = "") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')

    print(csv_reader)
    
    #1st row is the header
    header = next(csv_reader)
    
    #Read each row of data after the header
    for row in csv_reader:
        
        #Assign the Voter ID column from the csv file ==> String
        Source_Voter_ID.append(str(row[0]))
        
        #Assign the County column from the csv file ==> Integer
        Source_County.append(str(row[1]))
        
        #Assign the Candidate column from the csv file ==> Integer
        Source_Candidate.append(str(row[2]))


#------------------------------------
# Total number of votes = length of the total votes 
#------------------------------------
Total_Number_Votes = len(Source_Candidate)
print(Total_Number_Votes)



#------------------------------------
# Who are the candidates????????
#------------------------------------
# Create an empty list
Candidate_List = [] 
      
# Loop 
for i in Source_Candidate:
        
    # check if exists in unique_list or not 
    if i not in Candidate_List:
        
        #append the values to the empty list
        Candidate_List.append(i) 



#------------------------------------
# The list of candidates
#------------------------------------
print(Candidate_List)


#------------------------------------
# Who voted for KHAN????????
#------------------------------------
# Create an empty list & a pre-defined list
Khan_Candidate = ["Khan"] 
Khan_Votes = []
      
# loop 
for i in Source_Candidate:
        
    # check if exists in unique_list or not 
    if i in Khan_Candidate :
        
        #append the values to the empty list
        Khan_Votes.append(i)

Total_Khan_Votes = len(Khan_Votes)
Total_Khan_Votes
Percent_Khan = (Total_Khan_Votes / Total_Number_Votes)*100
print(Percent_Khan)


#------------------------------------
# Who voted for CORREY????????
#------------------------------------
# intilize a null list 
Correy_Candidate = ["Correy"] 
Correy_Votes = []
      
# traverse for all elements 
for i in Source_Candidate:
        
    # check if exists in unique_list or not 
    if i in Correy_Candidate :
        Correy_Votes.append(i)

Total_Correy_Votes = len(Correy_Votes)
Total_Correy_Votes
Percent_Correy = (Total_Correy_Votes / Total_Number_Votes)*100.00
print(Percent_Correy)


#------------------------------------
# Who voted for LI????????
#------------------------------------

# intilize a null list 
Li_Candidate = ["Li"] 
Li_Votes = []
      
# traverse for all elements 
for i in Source_Candidate:
        
    # check if exists in unique_list or not 
    if i in Li_Candidate :
        Li_Votes.append(i)


Total_Li_Votes = len(Li_Votes)
Total_Li_Votes
Percent_Li = (Total_Li_Votes / Total_Number_Votes)*100
print(Percent_Li)


#------------------------------------
# Who voted for O'TOLLEY????????
# I must say that I took a shortcut by subtracting.
# Because I could not find how to include the special character of O'Tolley :)
#------------------------------------

OTolley_Votes = Total_Number_Votes - Total_Khan_Votes - Total_Correy_Votes - Total_Li_Votes
print(OTolley_Votes)
Percent_OTolley = (OTolley_Votes / Total_Number_Votes)*100
print(Percent_OTolley)



#------------------------------------
# Final Output
#------------------------------------

print("Elections Results")
print(str("-----------------------------------------"))
print(f"Total Votes: {Total_Number_Votes}")
print(str("-----------------------------------------"))

print(f"Khan:{Percent_Khan}% " + "(" + f"{Total_Khan_Votes}" + ")")
print(f"Correy: {Percent_Correy}% " + "(" +  f"{Total_Correy_Votes}" + ")")
print(f"Li: {Percent_Li}% " + "(" +  f"{Total_Li_Votes}" + ")")
print(f"O'Tooley:{Percent_OTolley}% " + "(" +  f"{OTolley_Votes}" + ")")
print(str("-----------------------------------------"))
print(f"Winner : Khan")
print(str("-----------------------------------------"))


#--------------------------------------
#Export final output
#--------------------------------------
# Dependencies
# import os
# import csv

# Specify the file to write to
#==> The below does not work
#output_path = os.path.join("..", "output", "new.csv")
output_path = os.path.join("./PyPoll_Output.csv")


# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (title)
    csvwriter.writerow(["Elections Results"])

    csvwriter.writerow([str("-----------------------------------------")])
    csvwriter.writerow([f"Total Votes: {Total_Number_Votes}"])
    csvwriter.writerow([str("-----------------------------------------")])
    csvwriter.writerow([f"Khan:{Percent_Khan}% " + "(" + f"{Total_Khan_Votes}" + ")"])
    csvwriter.writerow([f"Correy: {Percent_Correy}% " + "(" +  f"{Total_Correy_Votes}" + ")"])
    csvwriter.writerow([f"Li: {Percent_Li}% " + "(" +  f"{Total_Li_Votes}" + ")"])
    csvwriter.writerow([f"O'Tooley:{Percent_OTolley}% " + "(" +  f"{OTolley_Votes}" + ")"])
    csvwriter.writerow([str("-----------------------------------------")])
    csvwriter.writerow([f"Winner : Khan"])
    csvwriter.writerow([str("-----------------------------------------")])
















