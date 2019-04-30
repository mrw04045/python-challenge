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

    raw_votes = []

    # candidate_data = {}
    for row in csvreader:
        raw_votes.append(row[2])

    #-----------------------------------------------------------------------
    # Calculate total votes
    total_votes = len(raw_votes)

        # if row[2] not in candidate_data:
        #     candidate_data["candidate"] = row[2]

    c = Counter(raw_votes)
    tally = dict(c)
    winner = max(tally, key=tally.get)
    print(winner)

    #-----------------------------------------------------------------------
    #Calculate total votes for each candidate
    candidates = [*tally.keys()]
    votes_per_candidate = [*tally.values()]
    
    # votes = list(votes_per_candidate.values())
    # print(votes)

    percent_votes = []
    for x in votes_per_candidate:
        percent = '{:.3%}'.format(x/total_votes)
        percent_votes.append(percent)
    
    # winner = max(votes_per_candidate)
    # print(winner)
    # print(candidates)
    # print(votes_per_candidate)
    # print(percent_votes)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {percent_votes[i]} ({votes_per_candidate[i]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")





    # candidate_data = {}
    # for candidate in candidates:
    #     candidate_data["Name"] = candidate
    #     print(candidate_data)

    # #-----------------------------------------------------------------------
    # tally = dict.fromkeys(["candidate","% votes","total votes"])

    # print(tally)


#     # Create list for votes and candidates
#     votes = []
#     candidates = []
#     for row in csvreader:
#         votes.append(row[2])
#         if row[2] not in candidates:
#             candidates.append(row[2]) 

   

#     #-----------------------------------------------------------------------
#     # # Calculate total votes for each candidate
#     # c = Counter(votes)
#     # votes_per_candidate = dict(c)
#     # print(votes_per_candidate)
#     # votes = list(votes_per_candidate.values())
#     # print(votes)






