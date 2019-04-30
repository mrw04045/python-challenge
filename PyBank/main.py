# Import modules
import os
import csv

#-----------------------------------------------------------------------
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
    # Calculate the changes in "Profit/Losses" over the entire period
    for x in range(1, len(ProfitLoss)):
        change_PL.append(int(ProfitLoss[x] - ProfitLoss[x-1]))

    # Calculate average change (sum of change_PL list/ length of change_PL list) and round to 2 decimals
    average_change = round(sum(change_PL) / len(change_PL), 2)
 
    #----------------------------------------------------------------------- 
    # Find greatest increase (ie. max) in profits (date and amount) over the entire period
    max_increase = max(change_PL)
    # Find the index associated with the max increase
    index_max = change_PL.index(max_increase)
    # Find date associated with the max increase 
    # use +1 because we have no change in PL for first date
    max_date = date[index_max +1] 

    #----------------------------------------------------------------------- 
    # Find greatest decrease (ie. min) in losses (date and amount) over the entire period
    max_decrease = min(change_PL)
    # Find the index associated with the max decrease
    index_min = change_PL.index(max_decrease)
    # Find date associated with max_decrease
    # use +1 because we have no change in PL for first date
    min_date = date[index_min +1] 

#----------------------------------------------------------------------- 
# Create variable 'output' as multiple line string containing Financial Analysis 
output = (f'''
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change}
Greatest Increase in Profits: {max_date} (${max_increase})
Greatest Decrease in Profits: {min_date} (${max_decrease})
''')

# Print output (Financial Analysis)
print(output)

#----------------------------------------------------------------------- 
# Open new file(f) 'output.txt' to write output to
f = open("output.txt",'w')

# Write output(Financial Analysis) to file(f)
f.write(output)

