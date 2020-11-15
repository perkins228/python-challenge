import os
import csv

filepath = os.path.join("./Resources/election_data.csv")

with open(filepath) as csvfile:
    election_csv = csv.reader(csvfile)
    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    for row in election_csv:
        total_votes = total_votes + 1

    print(total_votes)