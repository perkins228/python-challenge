import os
import csv

#import file
filepath = os.path.join("/PyBank/Resources/budget_data.csv")
total_months = 0
revenue = 0



with open(filepath) as csvfile:
    bankcsv = csv.reader(csvfile, delimiter = ",")
    next(bankcsv)
    revenue = revenue + 1

    for row in bankcsv:
        revenue = revenue + int(row[1])
    print(revenue)