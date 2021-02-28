# plan of attack
# import modules
# locate the file and read it? 
# has this format Date. Profit/Loss: Jan-2010,867884
# output needs to be succinct - PRINT AT THE END
# total months - goes over multiple years
# sum the profit losses column
# greatest increase in profits - one with highest value
# greatest decrease - lowest value
# need a .txt file at the end with the printed results


#need to import modules to get operating system tasks and csv reading
import os
import csv
import statistics

#path to the data
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

total_month = 0
total = 0

date = []
pro_loss = []
prof_change = []


#reading csv file

with open(budget_csv, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csvheader = next(csvreader)
    
    # first_row = next(csvreader)
    # first_profit = int(first_row.split(',')[1])

    #prev_change = first_profit
   # total_change = 0

    for row in csvreader:
        total_month += 1 # this loops for every row to add rows
        total += int(row[1]) #this loops for every and adds the contents of column 2 to the previous total

        date.append(row[0])
        pro_loss.append(int(row[1]))
    

    for i in range(1, len(pro_loss)): #how do we loop through the list and minus the next value from the previous one and then append that 
        prof_diff = pro_loss[i] - pro_loss[i-1]
        prof_change.append(prof_diff)
        avg_change = statistics.mean(prof_change)

    #min and max
    max_dec = min(prof_change)

    max_inc = max(prof_change)


    #with open(budget_csv, 'w') as csvfile:

        #csvwriter = csv.writer(csvfile, delimiter= ',')

        #prof_change_str = [str(x) for x in prof_change]

        #all = []

        #all.append(date)
        #all.append(pro_loss)
       # all.append(prof_change_str)

       # csvwriter.writerows(all)

    #for row in csvwriter:
        #if row[2] == "max_dec":
         #   max_dec_date = row[0]
       # elif row[2] == "max_inc":
         #   max_inc_date = row[0]  

    
    

       # monthly_change = int(row[1])-prev_change
       # prev_change = int(row[1])
       # total_change += monthly_change
       # avg_diff = total_change/total_month


# define the function and have it accept the data, so we can use the function on anything we chuck in
# these are just so you don't repeat yourself...DRY
#def  print_analysis(budget):

# PRINTS
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${total}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: (${max_inc})")
print(f"Greatest Decrease in Profits: (${max_dec})")
#print(f"{max_dec_date}")
#print(f"{max_inc_date}")
#print(prof_change_str)