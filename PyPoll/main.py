#allows us to to go through the files without issues
import os

#will be needed to calculate the mean easier 
# import pandas as pd 

#allow us to work with the csv file with budget_data
import csv
pollcsv = os.path.join('Resources', 'election_data.csv')


#setting the counters
pollcounter = 0
incomesum = 0
incomeavg = 0
pandl = []
Khancounter = 0
CorreyCounter = 0
LiCounter = 0
OTooleyCounter = 0




#counting the rows
#creating a condition that will only count if the candidates names shows up on column 3
with open(pollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}") #i just want to see the headers
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
        

 #showing total votes       
totalvotes = pollcounter
# print(totalvotes)

#capturing each candidates total votes and their Percentages (Khan)
#the whole print() will be disabled when i turned this in. Its just for debugging purposes
totalKhan = Khancounter
Khanpercent = totalKhan / totalvotes
KPerform = format(Khanpercent, ".2%")
# print(totalKhan)
# print(Khanpercent)
# print(KPerform)

#capturing each candidates total votes and their Percentages (Correy)
#the whole print() will be disabled when i turned this in. Its just for debugging purposes
totalCorrey = CorreyCounter
Corpercent = totalCorrey / totalvotes
CPerform = format(Corpercent, ".2%")
# print(Corpercent)
# print(totalCorrey)
# print(KPerform)

#capturing each candidates total votes and their Percentages (Li)
#the whole print() will be disabled when i turned this in. Its just for debugging purposes
totalLi = LiCounter
Lipercent = totalLi / totalvotes
LPerform = format(Lipercent, ".2%")
# print(Lipercent)
# print(totalLi)
# print(LPerform)

#capturing each candidates total votes and their Percentages (O'Tool)
#the whole print() will be disabled when i turned this in. Its just for debugging purposes.
totalOtooley = OTooleyCounter
Otoolpercent = totalOtooley / totalvotes
OPerform = format(Otoolpercent, ".2%")
# print(Otoolpercent)
# print(totalOtooley)
# print(Otoolpercent)


#creating a dictionary to show each candidates total votes 
# Will disable the print(votedict) on the final release.       
votedict = {"Khan": totalKhan,
            "Correy": totalCorrey,
            "Li": totalLi,
            "O Tooley": totalOtooley,
}
print(votedict)


#will disable the print('highestvote', 'lowestvote') at the final version
#creating a zip to merge the documents to find the candidate with the highest vote
pollzip1 = zip(votedict.values(), votedict.keys())
highestvote = max(pollzip1)
print(highestvote)

#creating another zip to merge the documents to find the candidate with the lowest vote
pollzip2 = zip(votedict.values(), votedict.keys())
lowestvote = min(pollzip2)
print(lowestvote)

VoteStatement = ("There was a total of ", totalvotes, " counted for all candidates.")
KhanStatement = ("Khan had ", totalKhan, " votes. Taking ", KPerform, " of the votes")
CorreyStatement = ("Khan had ", totalCorrey, " votes. Taking ", CPerform, " of the votes")
LiStatement = ("Khan had ", totalLi, " votes. Taking ", LPerform, " of the votes")
OToolStatement = ("Khan had ", totalOtooley, " votes. Taking ", OPerform, " of the votes")
HighestStatement = ("The Winning Candidate with the highest vote count: ", highestvote)
LowestStatement = ("Candidate with the lowest vote: ", lowestvote)
print(VoteStatement)
print(KhanStatement)
print(CorreyStatement)
print(LiStatement)
print(OToolStatement)


Outputtxt = open("analysis/PollAnalysis.txt","w")
Outputtxt.write(str(VoteStatement))
Outputtxt.write("\n")
Outputtxt.write(str(KhanStatement))
Outputtxt.write("\n")
Outputtxt.write(str(CorreyStatement))
Outputtxt.write("\n")
Outputtxt.write(str(LiStatement))
Outputtxt.write("\n")
Outputtxt.write(str(OToolStatement))
Outputtxt.write("\n")
Outputtxt.write(str(LowestStatement))
Outputtxt.write("\n")
Outputtxt.write(str(HighestStatement))
Outputtxt.write("\n")
Outputtxt.close()
