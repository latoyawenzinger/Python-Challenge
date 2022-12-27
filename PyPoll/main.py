#import os module
import os

#module for reading CSV
import csv

poll_csv = os.path.join("Resources", "election_data.csv")

with open(poll_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        print(row)
