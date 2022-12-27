#import os module
import os

#module for reading CSV
import csv

bank_csv = os.path.join("Resources", "budget_data.csv")



with open(bank_csv) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    
#skip header to avoid being counted
    headers = next(csvreader)

   
#array containing and profit/loss values
    months = []
    profit_loss = []

#looping through Date column to get total number of rows   
    for row in csvreader:
        #count each month 
        months.append(row[0])

        #sum of all profit/loss of entire period
        profit_loss.append(int(row[1]))

    total_months = len(months)
    sum = sum(profit_loss)
    


    


        




    


        
        
    



        




        #total_months += 1
        #print("Total Months: " + str(total_months))





    
   

