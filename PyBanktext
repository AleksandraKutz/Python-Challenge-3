import os
import csv

csvpath = os.path.join("/Users/aleksandrakrysiuk/Desktop/Python-Challenge-3/PyBank/Resources/budget_data.csv")

all_months = 0
all_profit_losses = 0
last_profit_loss = 0
monthly_changes = []
greatest_increase_amount = 0
greatest_increase_date = ""
greatest_decrease_amount = 0
greatest_decrease_date = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        all_months += 1
        profit_loss = int(row[1])  
        all_profit_losses += profit_loss

        if all_months > 1:
            monthly_change = profit_loss - last_profit_loss
            monthly_changes.append(monthly_change)

            if monthly_change > greatest_increase_amount:
                greatest_increase_amount = monthly_change
                greatest_increase_date = row[0]

            if monthly_change < greatest_decrease_amount:
                greatest_decrease_amount = monthly_change
                greatest_decrease_date = row[0]

        last_profit_loss = profit_loss


average_change = sum(monthly_changes) / len(monthly_changes)

print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {all_months}")
print(f"Total: ${all_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")