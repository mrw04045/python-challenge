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
    c = Counter(raw_votes)
    tally = dict(c)
    winner = max(tally, key=tally.get)
  
    #-----------------------------------------------------------------------
    #Calculate total votes for each candidate
    candidates = [*tally.keys()]
    votes_per_candidate = [*tally.values()]
    
    percent_votes = []
    for x in votes_per_candidate:
        percent = '{:.3%}'.format(x/total_votes)
        percent_votes.append(percent)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for i in range(len(candidates)):
        print(f"{candidates[i]}: {percent_votes[i]} ({votes_per_candidate[i]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
    
#-------------------------------------------------- 
# Open new file(f) 'output.txt' to write output to
f = open("output.txt",'w')

# Write output(Financial Analysis) to file(f)
f.writelines(f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------\n''')

for i in range(len(candidates)):
        f.writelines(f"{candidates[i]}: {percent_votes[i]} ({votes_per_candidate[i]})\n")

f.writelines(f'''-------------------------
Winner: {winner}
-------------------------''')