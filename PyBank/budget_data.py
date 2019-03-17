# budget_data.py

''' Description:
  Script for analyzing the financial records of a company, read from a
  CSV file (PyBank/Resources/budget_data.csv). The dataset is composed 
  of two columns: `Date` and `Profit/Losses`. 

  * This script will analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

  * Example of the output:
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
'''
import csv

# Open the CSV file and read the data into a dictionary (bd)
# bd will hold a list of the dictionaries read

with open('./Resources/budget_data.csv') as csvfile:
    bd = list(csv.DictReader(csvfile))
    
    bd_tmp =bd

# Function to update the dictioanries with the data we want to track 
# that will be used to generate to output report
def updateDict(d, total, cnt):
    global bd

    profitLoss = float(d['Profit/Losses'])
    current_date = d['Date']
    total += profitLoss
    
    if cnt == 0:
        d['PlDiff'] = 0
        d['PlGrtIncr'] = 0
        d['PlGrtIncrMonth'] = None
        d['PlGrtDecrMonth'] = None
        d['PlGrtDecr'] = 0
        d['PlDiffSum'] = 0
        d['AvgDiff'] = 0
        d['PlTotal'] =  profitLoss
        total = profitLoss 
    else:
        d['PlTotal'] = total
        PlDiff = profitLoss - float(bd_tmp[cnt-1]['Profit/Losses'])
        PlDiffSum = float(bd[cnt-1]['PlDiffSum']) + PlDiff
        PlGrtIncr = float(bd[cnt-1]['PlGrtIncr'])
        PlGrtIncrMonth = bd[cnt-1]['PlGrtIncrMonth']
        PlGrtDecr = float(bd[cnt-1]['PlGrtDecr'])
        PlGrtDecrMonth = bd[cnt-1]['PlGrtDecrMonth']
        
        if (PlDiff > PlGrtIncr):
            d['PlGrtIncr'] = PlDiff
            d['PlGrtIncrMonth'] = current_date
        else:
            d['PlGrtIncr'] = PlGrtIncr
            d['PlGrtIncrMonth'] = PlGrtIncrMonth
        if (PlDiff < PlGrtDecr):
            d['PlGrtDecr'] = PlDiff
            d['PlGrtDecrMonth'] = current_date
        else:
            d['PlGrtDecr'] = PlGrtDecr
            d['PlGrtDecrMonth'] = PlGrtDecrMonth
            
        d['PlDiff'] = str(PlDiff)
        d['PlDiffSum'] = PlDiffSum
        d['AvgDiff'] = PlDiffSum/cnt
        
        
    return(total)
 
total_months = len(bd)
plTotal = 0.0

# call UpdateDict for each dictionary entry in the list read above       
for i in range(total_months):
    plTotal = updateDict(bd[i], plTotal, i)
    #print("Total: " + str(plTotal))
    


print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(total_months))
print("Total: " + "${:.{}f}".format(plTotal, 2))
print("Average Change : " + "${:.{}f}".format(bd[total_months-1]['AvgDiff'], 2))
print("Greatest Increase in Profits : " + bd[total_months-1]['PlGrtIncrMonth'] + " (${:.{}f})".format(bd[total_months-1]['PlGrtIncr'], 2))
print("Greatest Decrease in Profits : " + bd[total_months-1]['PlGrtDecrMonth'] + " (${:.{}f})".format(bd[total_months-1]['PlGrtDecr'], 2))

reportFile = open('./financial_analysis.txt', "w")
reportFile.write("Financial Analysis\n")
reportFile.write("--------------------\n")
reportFile.write("Total Months: " + str(total_months) + "\n")
reportFile.write("Total: " + "${:.{}f}".format(plTotal, 2) + "\n")
reportFile.write("Average Change : " + "${:.{}f}".format(bd[total_months-1]['AvgDiff'], 2) + "\n")
reportFile.write("Greatest Increase in Profits : " + bd[total_months-1]['PlGrtIncrMonth'] + " (${:.{}f})".format(bd[total_months-1]['PlGrtIncr'], 2) + "\n")
reportFile.write("Greatest Decrease in Profits : " + bd[total_months-1]['PlGrtDecrMonth'] + " (${:.{}f})".format(bd[total_months-1]['PlGrtDecr'], 2) + "\n")
reportFile.close()

    

