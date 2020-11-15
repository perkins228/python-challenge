import os
import csv

#import file
filepath = "./Resources/budget_data.csv"

with open(filepath) as csvfile:
    bankcsv = csv.reader(csvfile, delimiter = ",")
    next(bankcsv)
    total_months = 0
    revenue = 0
    total_months = len(list(bankcsv))
    print(total_months)
    for row in bankcsv:
        revenue = revenue + float(row[1])
    print(revenue)