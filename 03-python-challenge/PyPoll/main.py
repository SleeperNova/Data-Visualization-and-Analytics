# import os and csv modules
import os
import csv

# Set path for the budget_data.csv file located in Resources folder:
os.chdir(os.path.dirname(os.path.realpath(__file__)))
csv_path = os.path.join('Resources', "election_data.csv")

#lists to store data, starting variables
TotVotes = 0
Candidates =[]
CandVotes = []
PercentVotes = []

#read csv
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')

#read and store header row
    csv_header = next(csvreader)
#Loop to capture csv info 

#counter = 0
    for line in csvreader:
        TotVotes += 1
        if line[2] not in Candidates:
            Candidates.append(line[2])
            CandVotes.append(0)
            PercentVotes.append(0)
        CurrentCand = line[2]
        CurrentCandIndex = Candidates.index(CurrentCand)
        CandVotes[CurrentCandIndex] +=1

#create percentage list
    for i in range(0,len(PercentVotes)):
        PercentVotes[i] =round((CandVotes[i]/TotVotes)*100,3)

#Determine winner
    MaxVotes = CandVotes[0]
    for i in range(0,len(CandVotes)):
        if CandVotes[i] > MaxVotes:
            MaxVotes = CandVotes[i]
            MaxVotesIndex = CandVotes.index(MaxVotes)
            Winner = Candidates[MaxVotesIndex]

# print to terminal
print('Election Results')
print('----------------------------')
print('Total Votes: ' + str(TotVotes))
print('----------------------------')
for i in range(0,len(Candidates)):
    print(str(Candidates[i]) + ': ' + str(PercentVotes[i]) + '% ' + '(' + str(CandVotes[i])) + ')'
print('----------------------------')
print('Winner: ' + str(Winner))
print('----------------------------')


# writing to output text file
OutputFile = os.path.join("analysis","PyPollOutput.txt")
with open(OutputFile,"w") as datafile:
    datafile.writelines('Election Results''\n')
    datafile.writelines('----------------------------''\n')
#    datafile.writelines(f"Total Votes: {TotVotes}""\n")
#    datafile.writelines("----------------------------""\n")
#    for i in range(0,len(Candidates)):
#        datafile.writelines(f"{Candidates[i]}: {PercentVotes[i]}% ({CandVotes[i]})""\n")
#    datafile.writelines("----------------------------""\n")
#    datafile.writelines(f"Winner: {Winner}""\n")
#    datafile.writelines("----------------------------""\n")