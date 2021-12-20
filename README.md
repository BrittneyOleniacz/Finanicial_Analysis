# Finanicial Analysis using Python

## Objective:
* Create a Python script that analyzes the records to calculate each of the following:
  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * The average of the changes in "Profit/Losses" over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period

## Script
```ruby
import os
import csv
import sys  

with open("budget_data.csv") as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    total_months = 0
    net_pl = []
    previous_month = 867884
    change = 0
    change_list = []
    greatest_profit_month = ""
    most_profit = 0
    greatest_loss_month = ""
    most_loss = sys.maxsize
    average_change = 0
    total_amount = 0
      
    for row in csvreader:
        current_month = row["Profit/Losses"]
        change = float(current_month) - float(previous_month) 
    
        total_months = total_months + 1
         
        Date_find = row["Date"]
                
        net_pl.append(int(current_month))
        total_amount = sum(net_pl)
             
        previous_month = row["Profit/Losses"]   
                
        if change > most_profit:
            most_profit = change
            greatest_profit_month = Date_find
        if  change < most_loss:
            most_loss = change
            greatest_loss_month = Date_find
        
        change_list.append(change)  
            
average_change=float(sum(change_list)/(len(change_list) - 1))

output = f'''
    Financial Analysis
    ----------------------------
    Total Months: {total_months}
    Total: ${total_amount:.2f}
    Average  Change: ${average_change:.2f}
    Greatest Increase in Profits: {greatest_profit_month} (${most_profit:.2f})
    Greatest Decrease in Profits: {greatest_loss_month} (${most_loss:.2f})
    '''
print(output)
output_file = os.path.join("PyBankOutput.txt")
with open(output_file, 'w') as textfile:
    textfile.write(output)    
```

### Output

    Financial Analysis
    ----------------------------
    Total Months: 86
    Total: $38382578.00
    Average  Change: $-2315.12
    Greatest Increase in Profits: Feb-2012 ($1926159.00)
    Greatest Decrease in Profits: Sep-2013 ($-2196167.00)


