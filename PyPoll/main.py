#allows us to to go through the files without issues
import os

#will be needed to calculate the mean easier 
# import pandas as pd 

#allow us to work with the csv file with budget_data
import csv
pollcsv = os.path.join('Resources', 'election_data.csv')

#defining the data in budget_data.csv

pollcounter = 0
incomesum = 0
incomeavg = 0
pandl = []
Khancounter = 0
CorreyCounter = 0
LiCounter = 0
OTooleyCounter = 0


# def ProfitLoss(budget_data):
#     month = str(budget_data[0])
#     income = float(budget_data[1])
#     print(f"There are {TotalMonths} months in the budget")

with open(pollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
   #  print(f"CSV Header: {csv_header}")
    for row in csvreader:
      pollcounter += 1 
      if row[2] == ("Khan"):
          Khancounter += 1
      if row[2] == ("Correy"):
         CorreyCounter += 1
      if row[2] == ("Li"):
         LiCounter += 1
      if row[2] == ("O'Tooley"):
         OTooleyCounter += 1
 
      # incomesum += int(row[1])



        
        
totalvotes = pollcounter
print(totalvotes)

totalKhan = Khancounter
Khanpercent = totalKhan / totalvotes
print(Khanpercent)
print(totalKhan)

totalCorrey = CorreyCounter
Corpercent = totalCorrey / totalvotes
print(Corpercent)
print(totalCorrey)

totalLi = LiCounter
Lipercent = totalLi / totalvotes
print(Lipercent)
print(totalLi)

totalOtooley = OTooleyCounter
Otoolpercent = totalOtooley / totalvotes
print(Otoolpercent)
print(totalOtooley)
        
votedict = {"Khan votes": totalKhan,
            "Correy votes": totalCorrey,
            "Li votes": totalLi,
            "O Tooley Votes": totalOtooley,
}
print(votedict)


pollzip1 = zip(votedict.values(), votedict.keys())

highestvote = max(pollzip1)
print(highestvote)

pollzip2 = zip(votedict.values(), votedict.keys())
lowestvote = min(pollzip2)
print(lowestvote)


Outputtxt = open("analysis/PollAnalysis.txt","w")
Outputtxt.write("There are a total ", totalvotes, " votes")
Outputtxt.close()