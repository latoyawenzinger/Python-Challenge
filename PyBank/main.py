#import os module
import os

#module for reading CSV
import csv

#import statitics module to calculate avagerage with simple function
import statistics

bank_csv = os.path.join("Resources", "budget_data.csv")

with open(bank_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    
#skip header to avoid being counted
    headers = next(csvreader)   

#creating variable lists to store specified data
    months = []
    profit_loss = []
    month_to_month = []
    

#looping through each row  
    for row in csvreader:
        #count each month in data column and add to the array
        months.append(row[0])
        #add each profit/loss value of the entire year into the profit/loss array
        profit_loss.append(int(row[1]))   
        

    #obtain the lenth of items in the months list
    total_months = len(months)
    #totaling each profit/loss value in the list to get total
    sum = sum(profit_loss)

    
    for i in range(len(profit_loss)-1):
        #calculate difference between current value and the next
        profit_changes = profit_loss[i+1] - profit_loss[i]
        #add each 'difference' value to a list
        month_to_month.append(profit_changes)
        #find max and min of the list
        maxchange = max(month_to_month)
        minchange = min(month_to_month)
        #find average of the list
        x = round(statistics.mean(month_to_month),2)

    #find the max/min value in the list and return its corresponding month
    j = month_to_month.index(maxchange)
    bestmonth = months[j+1]

    k = month_to_month.index(minchange)
    worstmonth = months[k+1]
   
#print analysis in terminal             
print("Financial Analysis")
print("----------------------------")  

print(f"Total Months: {total_months}")
print(f"Total: ${sum}")
print(f"Average Change: ${x}")
print(f"Greatest Increase in Profits:  {bestmonth}  (${maxchange})")
print(f"Greatest Decrease in Profits:  {worstmonth}  (${minchange})")
            

#convert script to text file and export it to Analysis folder
analysis_file = os.path.join("Analysis", "budget_analysis.txt")
with open(analysis_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")  
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${sum}\n")
    outfile.write(f"Average Change: ${x}\n")
    outfile.write(f"Greatest Increase in Profits:  {bestmonth}  (${maxchange})\n")
    outfile.write(f"Greatest Decrease in Profits:  {worstmonth}  (${minchange})")