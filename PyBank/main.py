import os

import csv

csvpath = "C:/Users/hilda/Desktop/Learn_Python/budget_data.csv"

with open(csvpath, newline='') as csvfile:

    csvread = csv.reader(csvfile, delimiter=',')

    Total_Months = 0 

    #print(csvread)
    next(csvread)

    for row in csvread:
        #print(row)
        Total_Months += 1


with open(csvpath, newline='') as csvfile:

    csvread = csv.reader(csvfile, delimiter=',')

    Total = 0 

    #print(csvread)
    next(csvread)

    for row in csvread:
        if row[1] != 0:
            Total += int(row[1])

#---------------------------------------------------------------

  
with open(csvpath, newline='') as csvfile:

    csvread = csv.reader(csvfile, delimiter=',')

    Pre_Value = 0 

    #print(csvread)
    next(csvread)
    First = next(csvread)

    Pre_Value = int(First[1])
    changes_list = []

    for row in csvread:
        Current = int(row[1])
        Change = Current - Pre_Value
        Pre_Value = Current
        changes_list.append(Change)

    Greatest_Increase = max(changes_list)
    Greatest_Decrease = min(changes_list)
    Average_Change = round(sum(changes_list)/int(len(changes_list)),2)

    Increase_Index = changes_list.index(Greatest_Increase)
    Decrease_Index = changes_list.index(Greatest_Decrease)

 
 #----------------------------------------------------------------------------

with open(csvpath, newline='') as csvfile:

    csvread = csv.reader(csvfile, delimiter=',')

    Pre_Value = 0 

    #print(csvread)
    next(csvread)  
    next(csvread)

    Date_List =[]

    for row in csvread:
        Date = row[0]
        Date_List.append(Date)

Increase_Date = Date_List.pop(Increase_Index)
Decrease_Date = Date_List.pop(Decrease_Index -1)




# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


print('Financial Analysis')
print('----------------------')
print('Total Months: ' + str(Total_Months))
print('Total: $'+ str(Total))
print('Average  Change: ' + str(Average_Change))
print('Greatest Increase in Profits: ' + Increase_Date + " " + str(Greatest_Increase))
print('Greatest Decrease in Profits: ' + Decrease_Date + " " + str(Greatest_Decrease))
