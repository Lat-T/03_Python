
#------------------------------------
# Import the csv file
#------------------------------------
import os
import csv
csv_path = os.path.join("./PyBank_data.csv")



#------------------------------------
# Create lists to store data
#------------------------------------
Source_Date = []
Source_Amount = []


#------------------------------------
# append the values within the csv file to the previously created lists
#------------------------------------
with open(csv_path, newline = "") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csvfile, delimiter=',')

    print(csv_reader)
    
    #1st row is the header
    header = next(csv_reader)
    
    #Read each row of data after the header
    for row in csv_reader:
        
        #Assign the Date column from the csv file ==> String
        Source_Date.append(str(row[0]))
        
        #Assign the Profit/Loss column from the csv file ==> Integer
        Source_Amount.append(int(row[1]))


#--------------------------------------
# DATA CLEANSING
#--------------------------------------

#------------------------------------
# Cleanse data ==> remove value = 'Date' because it's a header
# print dates
#------------------------------------
if Source_Date[0] == "Date":
    Source_Date.remove("Date")
print(Source_Date)


#------------------------------------
# cleanse data ==> remove value = 'Profit/Losses' because it's a header
# ==> Used the "pop" method this time to delete
# print amount
#------------------------------------
if Source_Amount[0] == "Profit/Losses":
    Source_Amount.pop(0)
print(Source_Amount)


#--------------------------------------
# FIND THE NUMBER OF RECORDS (LENGTH)
#--------------------------------------

#------------------------------------
# find the number of records 
# ==> length for Date (should be the same as for amount)
# print dates
#------------------------------------
Length_Date = len(Source_Date)
print(Length_Date)


#------------------------------------
# find the number of records 
# ==> length for Amount (should be the same as for date)
# print dates
#------------------------------------
Length_Amount = len(Source_Amount)
print(Length_Amount)



#--------------------------------------
# CALCULATIONS
#--------------------------------------

#--------------------------------------
# Calculate the SUM for the Source_Amount
Sum_Source_Amount = sum(Source_Amount)
print(Sum_Source_Amount)

#--------------------------------------
# Calculate the difference between the next amount and the curent amount
# The do not calculate for the last value of the list
#--------------------------------------

Difference = []

for i in range(len(Source_Amount)-1):
    Change = Source_Amount[i+1] - Source_Amount[i]
    Difference.append(Change)
print(Difference) 


#--------------------------------------
# Calculate the average difference by doing SUM of Difference / (Length of Difference)
#--------------------------------------
Average_Change = sum(Difference) / int(len(Difference))
print(Average_Change)


#--------------------------------------
# Find the greatest increase
#--------------------------------------
Greatest_Increase = max(Difference)
#--------------------------------------
# Find the INDEX for greatest increase
#--------------------------------------
Difference.index(max(Difference))
#--------------------------------------
# Find the month of the greatest increase Month+1
#--------------------------------------
Month_Increase = Source_Date[24+1]


#--------------------------------------
# Find the greatest decrease
#--------------------------------------
Greatest_Decrease = min(Difference)
#--------------------------------------
# Find the INDEX for greatest decrease
#--------------------------------------
Difference.index(min(Difference))
#--------------------------------------
# Find the month of the greatest decrease Month+1
#--------------------------------------
Month_Decrease = Source_Date[43+1]


#--------------------------------------
# Final output
#--------------------------------------
print("Financial Analysis")
print(str("-----------------------------------------"))
print(f"Total Months:{Length_Amount}")
print(f"Total: $ {Sum_Source_Amount}")
print(f"Average Change: $ {Average_Change}")
print(f"Greatest Increase in Profits: {Month_Increase}" + " " + "(" + "$" + f"{Greatest_Increase}" + ")")
print(f"Greatest Decrease in Profits: {Month_Decrease}" + " " + "(" + "$" + f"{Greatest_Decrease}" + ")")



#--------------------------------------
#Export final output
#--------------------------------------
# Dependencies
# import os
# import csv

# Specify the file to write to
#==> The below does not work
#output_path = os.path.join("..", "output", "new.csv")
output_path = os.path.join("./PyBank_Output.csv")


# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (title)
    csvwriter.writerow(["Financial Analysis"])

    csvwriter.writerow([str("-----------------------------------------")])
    csvwriter.writerow([f"Total Months:{Length_Amount}"])
    csvwriter.writerow([f"Total: $ {Sum_Source_Amount}"])
    csvwriter.writerow([f"Average Change: $ {Average_Change}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {Month_Increase}" + " " + "(" + "$" + f"{Greatest_Increase}" + ")"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {Month_Decrease}" + " " + "(" + "$" + f"{Greatest_Decrease}" + ")"])



















































