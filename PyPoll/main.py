import os
import csv

filepath = os.path.join("./Resources/election_data.csv")

with open(filepath) as csvfile:
    election_csv = csv.reader(csvfile)
    csv_header = next(election_csv)
    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    candidates = []

    for row in election_csv:
        total_votes = total_votes + 1

        if row [2] == "Khan":
            khan_votes = khan_votes + 1
        
        if row [2] == "Correy":
            correy_votes = correy_votes + 1
        
        if row [2] == "Li":
            li_votes = li_votes + 1
        
        if row [2] == "O'Tooley":
            otooley_votes = otooley_votes + 1

    khan_per = round(khan_votes/total_votes,2)
    correy_per = round(correy_votes/total_votes,2)
    li_per = round(li_votes/total_votes,2)
    otooley_per = round(otooley_votes/total_votes,2)




print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")
print(f"Khan: {khan_per:.3%} ({khan_votes})")
print(f"Correy: {correy_per:3%} ({correy_votes})")
print(f"Li: {li_per:.3%}% ({li_votes})")
print(f"O'Tooley: {otooley_per:.3%}% ({otooley_votes})")
