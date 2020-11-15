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







print(khan_votes)
print(correy_votes)
print(li_votes)
print(otooley_votes)
