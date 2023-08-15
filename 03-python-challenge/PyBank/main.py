# import os and csv modules
import os
import csv

# Set path for the budget_data.csv file located in Resources folder:
os.chdir(os.path.dirname(os.path.realpath(__file__)))
csv_path = os.path.join('Resources', "budget_data.csv")

#lists to store data, starting variables
NMonths = []
NPL =[]
ChangePL = []
TotProfit = 0
TotChange = 0
MinChange = 0
MaxChange = 0

#read csv
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
#read and store header row
    csv_header = next(csvreader)

#Loop to capture list of months NMonths, list of profitloss NPL, sum of total profit TotProfit, 
# calculate and create list of Change in PL, caputre max and min change and month
    counter = 0
    for line in csvreader:
        if counter ==0:
            PrevPL = int(line[1])
        NMonths.append(line[0])
        NPL.append(line[1])
        TotProfit = TotProfit + int(line[1])
        CurrentPL = int(line[1])
        CalcChange = CurrentPL-PrevPL
        ChangePL.append(CalcChange)
        TotChange = TotChange + CalcChange
        PrevPL = int(line[1])
        if CalcChange < MinChange:
            MinChange = CalcChange
            MinChangeMo = line[0]
        if CalcChange > MaxChange:
            MaxChange = CalcChange 
            MaxChangeMo = line[0]
        counter +=1

#average change calculated to correct for zero in ChangePL[0] for len(changePL)
AveChange = round(TotChange/(len(ChangePL)-1),2)

#print to terminal
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(len(NMonths)))
print('Total: ' + '$' + str(TotProfit))
print('Average Change: ' + '$' + str(AveChange))
print('Greatest Increase in Profits: ' + str(MaxChangeMo) + ' ($' + str(MaxChange) + ')')
print('Greatest Decrease in Profits: ' + str(MinChangeMo) + ' ($' + str(MinChange) + ')')

#writing to output text file
OutputFile = os.path.join("analysis","PyBankOutput.txt")
with open(OutputFile,"w") as datafile:
    datafile.writelines('Financial Analysis''\n')
    datafile.writelines('----------------------------''\n')
    datafile.writelines('Total Months: ' + str(len(NMonths)))
    datafile.writelines('\n''Total: ' + '$' + str(TotProfit))
    datafile.writelines('\n''Average Change: ' + '$' + str(AveChange))
    datafile.writelines('\n''Greatest Increase in Profits: ' + str(MaxChangeMo) + ' ($' + str(MaxChange) + ')')
    datafile.writelines('\n''Greatest Decrease in Profits: ' + str(MinChangeMo) + ' ($' + str(MinChange) + ')')