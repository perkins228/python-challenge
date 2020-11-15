import os
import csv

#import file
filepath = os.path.join("/PyBank/Resources/budget_data.csv")
total_months = 0
revenue = 0



with open(filepath) as csvfile:
    bankcsv = csv.reader(csvfile, delimiter = ",")
    next(bankcsv)
    total_months = total_months + 1
    revenue = revenue + 1

    for row in bankcsv:
        total_months = total_months + 1
        revenue = revenue + int(row[1])
        print(revenue)