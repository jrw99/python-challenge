import os
import csv
import statistics

budget_data_csv = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("analysis", "budget_data_analysis.txt")
budget_dict = {}
monthCount = 0
totalProfit = 0
previousProfitLoss = 0 
    
# =============================================================================
# Function that takes in a known dicitonairy for budget ananlysis and prints 
# the results to screen    
# =============================================================================
def printToScreen(results_dict):
    print("")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {results_dict['totalMonths']}")
    print(f"Total: ${results_dict['totalProfitLoss']}")
    print(f"Average  Change: ${results_dict['averageChange']}")
    print(f"Greatest Increase in Profits: {results_dict['greatestIncreaseDate']} (${results_dict['greatestIncrease']})")
    print(f"Greatest Decrease in Profits: {results_dict['greatestDecreaseDate']} (${results_dict['greatestDecrease']})")


# =============================================================================
# Function that takes in a known dictionairy for budget ananlysis and prints
# the results to a file
# =============================================================================
def printToFile(output_file, results_dict):

    #  Open the output file and write the results
    with open(output_file, "w", newline="") as outfile:
        
        outfile.write("\n")
        outfile.write("Financial Analysis\n")
        outfile.write("----------------------------\n")
        outfile.write(f"Total Months: {results_dict['totalMonths']}\n")
        outfile.write(f"Total: ${results_dict['totalProfitLoss']}\n")
        outfile.write(f"Average  Change: ${results_dict['averageChange']}\n")
        outfile.write(f"Greatest Increase in Profits: {results_dict['greatestIncreaseDate']} (${results_dict['greatestIncrease']})\n")
        outfile.write(f"Greatest Decrease in Profits: {results_dict['greatestDecreaseDate']} (${results_dict['greatestDecrease']})\n")


with open(budget_data_csv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')       
    csv_header = next(csvreader)    
    budget_dict = {rows[0]:int(rows[1]) for rows in csvreader}

# determine how many months are in the set. The set is ordered
# sequentially, with all months existing in each year tracked.
# now that the date is the key in the dictionary, we know it's a
# valid count because each month/year combo is unique
monthCount = len(budget_dict)

# calculate the total profit/loss for the dataset. Losses are 
# stored as negative values
totalProfit = sum(budget_dict.values())    


# =============================================================================
# Calculate the changes between the current and previous month for the 
# profit/loss in the entire set
# =============================================================================
budget_list = list(budget_dict.items())
budgetChange_dict = {}

for i in range(len(budget_list)-1):   
    budgetChange_dict.update({budget_list[i+1][0]: (budget_list[i+1][1] - budget_list[i][1])})

avgChange = round(statistics.mean(budgetChange_dict.values()), 2)
maxChange = max(budgetChange_dict.values())
minChange = min(budgetChange_dict.values())
maxChangeDate = max(budgetChange_dict, key=budgetChange_dict.get)
minChangeDate = min(budgetChange_dict, key=budgetChange_dict.get)

results_dict = {'totalMonths': monthCount, 
                'totalProfitLoss': totalProfit, 
                'averageChange': avgChange, 
                'greatestIncreaseDate': maxChangeDate, 
                'greatestIncrease': maxChange, 
                'greatestDecreaseDate': minChangeDate, 
                'greatestDecrease': minChange }

# =============================================================================
# Print the results to both the screen and a file
# =============================================================================
printToScreen(results_dict)

printToFile(output_file, results_dict)

    
        