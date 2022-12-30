#import os module
import os

#module for reading CSV
import csv

poll_csv = os.path.join("Resources", "election_data.csv")

with open(poll_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #skip header to avoided being counted
    header = next(csvreader)

    #creating variable lists to store specified data
    votes_count = []
    name1 = "Charles Casper Stockham" 
    name2 = "Diana DeGette"
    name3 = "Raymon Anthony Doane"
    CCS = []
    DD = []
    RAD = []
    candidates = []
    

    for row in csvreader:
        #add candidate name in a list each time they are voted on
        candidates.append(row[2])
        #calculate total votes overall
        votes_count.append((row[0]))
        #if ballot says Charles, then add to CCS lit
        if row[2] == name1:
            CCS.append(row[2])
        #else, if ballot says Diane, add to DD list 
        elif row[2] == name2:
                DD.append(row[2])
        #else, if ballot say Raymon, add to RAD list
        elif row[2] == name3:
                RAD.append(row[2])

    #calutate the percentage of votes each candidate won
    CCS_PerVotes = len(CCS) / len(votes_count)
    C_Percentage = "{:.3%}".format(CCS_PerVotes)
    DD_PerVotes = len(DD) / len(votes_count)
    D_Percentage = "{:.3%}".format(DD_PerVotes)
    RAD_PerVotes = len(RAD) / len(votes_count) 
    R_Percentage = "{:.3%}".format(RAD_PerVotes)

    #find the candidate with longest ballot list
    popular = max(len(CCS), len(DD), len(RAD))

    if popular == len(CCS):
        winner = name1

    elif popular == len(DD):
        winner = name2

    elif popular == len(RAD):
        winner = name3

#print analysis in terminal
print("Election Results")
print("-------------------------")

print(f'Total Votes: {len(votes_count)}')

print("-------------------------")

print(f'{name1}: {C_Percentage} ({len(CCS)})')

print(f'{name2}: {D_Percentage} ({len(DD)})')

print(f'{name3}: {R_Percentage} ({len(RAD)})')

print("-------------------------")

print(f'Winner: {winner}')

#convert script to text file and export it to Analysis folder
analysis_file = os.path.join("Analysis", "poll_analysis.txt")
with open(analysis_file,"w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")

    outfile.write(f'Total Votes: {len(votes_count)}\n')

    outfile.write("-------------------------\n")

    outfile.write(f'{name1}: {C_Percentage} ({len(CCS)})\n')

    outfile.write(f'{name2}: {D_Percentage} ({len(DD)})\n')

    outfile.write(f'{name3}: {R_Percentage} ({len(RAD)})\n')

    outfile.write("-------------------------\n")

    outfile.write(f'Winner: {winner}\n')  

    outfile.write("-------------------------")