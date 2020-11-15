import os
import csv

#import file
filepath = os.path.join("./Resources/budget_data.csv")
total_months = 0
revenue = 0
change = []
dates = []



with open(filepath) as csvfile:
    bankcsv = csv.reader(csvfile, delimiter = ",")
    next(bankcsv)
    prior_rev = 0

    for row in bankcsv:
        total_months = total_months + 1
        prior_rev = int(row[1])
        revenue = revenue + int(row[1])
        change.append(int(row[1]) - prior_rev )
        




print(f"Total Months: {total_months}")
print(f"Total: ${revenue}")
print(change)