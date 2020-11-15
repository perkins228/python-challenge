import os
import csv

#import file
filepath = os.path.join("./Resources/budget_data.csv")
total_months = 0
revenue = 0
change = []
dates = []
increase = 0
increace_month = 0
decrease = 0
decrease_month = 0




with open(filepath) as csvfile:
    bankcsv = csv.reader(csvfile, delimiter = ",")
    csv_header = next(bankcsv)
    row = next(bankcsv)
    prior_profit = int(row[1])
    total_months = 1
    date = 1
    revenue = int(row[1])
    increase = 0
    decrease = int(row[1])
    increase_month = row[0]
    decrease_month = row[0]
    
    for row in bankcsv:
        total_months = total_months + 1
        revenue = revenue + int(row[1])
        changes = int(row[1]) - prior_profit
        prior_profit = int(row[1])
        change.append(changes)
        dates.append(row[0])

        if changes > increase:
            increase = changes
            increase_month = row[0]

        if changes < decrease:
            decrease = changes
            decrease_month = row[0]

        
avg_profit =round(sum(change)/len(change),2)




print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${revenue}")
print(f"Average Change: ${avg_profit}")
print(f"Greatest Increase in Profits: {increase_month} (${increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${decrease})")
print("------")

textfile = os.path.join("./Resources/budget_data.text")
with open(textfile, "w") as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${revenue}\n")
    txtfile.write(f"Average Change: ${avg_profit}\n")
    txtfile.write(f"Greatest Increase in Profits: {increase_month} (${increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {decrease_month} (${decrease})\n")
    txtfile.write("------\n")