# Your task is to create a Python script that analyzes the records to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

# CSV FILE ASSUMPTIONS:
# Date data is in MON-RR format and ordered in ascending one-month intervals
# Profit/Losses data is signed int

# import os for filepaths, csv
import os
import csv

# constants for readability
DATE_COL = 0
PROFIT_LOSS_COL = 1

# create path to csv
csvPath = os.path.join('Resources', 'budget_data.csv')

# open file for reading
with open(csvPath) as csvFile:
    # create reader with "," delimiter
    csvReader = csv.reader(csvFile, delimiter=',')
    # eat the header
    csvHeader = next(csvReader)

    #initialize trackers
    totalMonths = 0
    budgetChanges = {}
    prevRowDate = ""
    prevRowProLoss = 0
    totalNet = 0

    for row in csvReader:
        # if prevRowDate has not been set, this is first row
        if not prevRowDate:
            # so store date and profit/loss to begin tracking changes
            prevRowDate = row[DATE_COL]
            prevRowProLoss = int(row[PROFIT_LOSS_COL])
        else:
            # store the change under the current date's entry
            budgetChanges[row[DATE_COL]] = int(row[PROFIT_LOSS_COL]) - prevRowProLoss
        # increment month tracker and net tracker
        totalMonths += 1
        totalNet += int(row[PROFIT_LOSS_COL])
        # prep "previous" markers for next iteration
        prevRowDate = row[DATE_COL]
        prevRowProLoss = int(row[PROFIT_LOSS_COL])

    # calculate average by summing budgetChanges.values() to only return the profits/losses
    # convert len() to float for decimal values. need to convert before division to maintain decimals
    averageChange = sum(budgetChanges.values()) / float(len(budgetChanges))

    # create tracking variables for min/max
    maxChange = 0
    maxDate = ""
    minChange = 0
    minDate = ""

    # loop thru dates + change pairs in dictionary
    for date, change in budgetChanges.items():
        if change > maxChange:
            maxChange = change 
            maxDate = date
        elif change < minChange:
            minChange = change
            minDate = date

    # print results
    print("Financial Analysis\n----------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalNet}")
    print(f"Average Change: ${averageChange:.2f}")
    print(f"Greatest Increase in Profits: {maxDate} (${maxChange})")
    print(f"Greatest Decrease in Profits: {minDate} (${minChange})")