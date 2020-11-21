#allows us to to go through the files without issues
import os

#will be needed to calculate the mean easier 
# import pandas as pd 

#allow us to work with the csv file with budget_data
import csv
budgetcsv = os.path.join('Resources', 'budget_data.csv')

#defining the data in budget_data.csv

monthcounter = 0
incomesum = 0
incomeavg = 0
pandl = []

# def ProfitLoss(budget_data):
#     month = str(budget_data[0])
#     income = float(budget_data[1])
#     print(f"There are {TotalMonths} months in the budget")

with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        pandl.append(row[1])
        monthcounter += 1 # monthcounter - mounthcounter + 1
        incomesum += int(row[1])
        print(row)
        


print('months total: ', monthcounter)
TotalIncome = incomesum 
print(TotalIncome)
incomeavg = TotalIncome / monthcounter
print(incomeavg)
MaximumIncome = max(pandl)
MinimunIncome = min(pandl)

Total = {'Months': monthcounter, "Total Income":TotalIncome, "Income Average": incomeavg, "Maximum Income": MaximumIncome, "Minimum Income": MinimunIncome }
print(Total)

Outputtxt = open("analysis/PybankAnalysis.txt","w")
Outputtxt.write(str(Total))
Outputtxt.close()

