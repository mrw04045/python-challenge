# Import modules
import os
import csv
from collections import Counter

# Define path to election_data.cvs
csvpath = os.path.join("Resources", "election_data.csv")

#-----------------------------------------------------------------------
# Open election_data.csv as datafile 
with open(csvpath, newline='') as datafile:
    # Create csvreader to read datafile based on "," separating indexes
    csvreader = csv.reader(datafile, delimiter = ",")
    
    #-----------------------------------------------------------------------
    # Move down a line in datafile
    next(datafile)

    #-----------------------------------------------------------------------
    # Create list of all votes (candidate name only)
    raw_votes = []
    for row in csvreader:
        raw_votes.append(row[2])

    #-----------------------------------------------------------------------
    # Calculate total votes
    total_votes = len(raw_votes)

    #-----------------------------------------------------------------------
    # Calculate total votes for each candidate

    # Create dictionary (tally) using counter (c) to retrieve {'candidate': 'number of votes'}
    c = Counter(raw_votes)
    tally = dict(c)
    
    # Retrieve the key (candidate name) associated with the max number of votes
    # Set it equal to a variable called 'winner'
    winner = max(tally, key=tally.get)
  
    #-----------------------------------------------------------------------
    # Create lists 'candidates', 'votes_per_candidate', and 'percent_votes'

    # Create list of candidates using the keys from the dictionary 'tally'
    candidates = [*tally.keys()]

    # Create list of votes_per_candidate using the values from the dictionary 'tally'
    votes_per_candidate = [*tally.values()]

    # Create empty list called percent_votes
    percent_votes = []
    # Loop through list 'votes_per_candidate'
    for x in votes_per_candidate:
        # find percent by taking votes per candidate/total_votes. Format as percent and keep 3 decimal places.
        percent = '{:.3%}'.format(x/total_votes) 
        # Append percent found to the list 'percent_votes'
        percent_votes.append(percent)

#-----------------------------------------------------------------------
# Print Election Results to terminal

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# Loop through all indexes given the length of candidates list
for i in range(len(candidates)):
        # Print index i of 'candidates', 'percent votes', and 'votes_per_candidate'
        print(f"{candidates[i]}: {percent_votes[i]} ({votes_per_candidate[i]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
    
#-------------------------------------------------- 
# Open new file(f) 'output.txt' to write output to
f = open("output.txt",'w')

#-------------------------------------------------- 
# Write output(Financial Analysis) to file(f)
f.writelines(f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n''')
# Loop through all indexes given the length of candidates list
for i in range(len(candidates)):
        # Write lines to file using index i of 'candidates', 'percent votes', and 'votes_per_candidate'
        f.writelines(f"{candidates[i]}: {percent_votes[i]} ({votes_per_candidate[i]})\n")
# Continue writing lines to file (f)
f.writelines(f'''-------------------------
Winner: {winner}
-------------------------''')