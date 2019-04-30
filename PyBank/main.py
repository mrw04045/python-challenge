# Import modules
import os
import csv

# Define path to budget_data.cvs
csvpath = os.path.join("Resources", "budget_data.csv")

#-----------------------------------------------------------------------
# Open budget_data.csv as datafile 
with open(csvpath, newline='') as datafile:
    # Create csvreader to read datafile based on "," separating indexes
    csvreader = csv.reader(datafile, delimiter = ",")
    
    #-----------------------------------------------------------------------
    # Move down a line in datafile
    next(datafile)

    #-----------------------------------------------------------------------
    # Create empty lists to hold date, profit and losses, and change in Profit and Losses
    date = []
    ProfitLoss = []
    change_PL = []

    #-----------------------------------------------------------------------
    # Loop through csvreader 
    for row in csvreader:
        # Append date (found at index 0) to the list 'date'
        date.append(row[0])
        # Append ProfitLoss (found at index 1) to the list 'ProfitLoss'
        ProfitLoss.append(int(row[1]))

    #-----------------------------------------------------------------------
    # Calculate total months by finding length of the list 'date'
    total_months = len(date)

    #-----------------------------------------------------------------------
    # Calculate net total of "Profit/Losses" over the entire period 
    net_total = sum(ProfitLoss)

    #-----------------------------------------------------------------------   
    # ????Calculate the changes in "Profit/Losses" over the entire period
    for x in range(1, len(ProfitLoss)):
        change_PL.append(int(ProfitLoss[x] - ProfitLoss[x-1]))

    # Calculate average change (sum of change_PL list/ length of change_PL list) and round to 2 decimals
    average_change = round(sum(change_PL) / len(change_PL), 2)
 
    #----------------------------------------------------------------------- 
    # Find greatest increase (ie. max) in profits (date and amount) over the entire period
    max_increase = max(change_PL)
    # Find date associated with max_increase
    index_max = change_PL.index(max_increase)
    max_date = date[index_max +1]

    #----------------------------------------------------------------------- 
    # Find greatest decrease (ie. min) in losses (date and amount) over the entire period
    max_decrease = min(change_PL)
    # Find date associated with max_decrease
    index_min = change_PL.index(max_decrease)
    min_date = date[index_min +1]

#----------------------------------------------------------------------- 
# Print out Financial Analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {min_date} (${max_decrease})")
