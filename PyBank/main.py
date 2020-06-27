#####################
####  I/O Setup  ####
#####################
import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))           # Set Directory
budget_raw = os.path.join("Resources","budget_data.csv")       # associate input file
budget_sum = os.path.join("Analysis","budget_summary.txt")                # associate output file

################################################
####  Define and Initialize Data Variables  ####
################################################
total_months = 0
net_total = 0
greatest_increase = ["Jan-1900",0]
greatest_decrease = ["Jan-1900",9999]

################################################################
####  read input: accumulate P&L, determine extreme months  ####
################################################################
with open(budget_raw) as infile:
    in_rec = csv.reader(infile, delimiter = ",")
    next(infile)
    for row in in_rec:
        total_months += 1
        net_total += int(row[1])
        if int(row[1]) > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = int(row[1])
        elif int(row[1]) < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = int(row[1])

avg_chg = round(net_total/total_months,2)         # Calculate average monthly P&L

###################################################
####  Write output summary (pseudo-formatted)  ####
###################################################

with open(budget_sum,'w',newline='') as outfile:
    out_rec = csv.writer(outfile)
    out_rec.writerow(["Financial Analysis"])
    out_rec.writerow(["-"*30])
    out_rec.writerow(["Total Months : " + str(total_months)])
    out_rec.writerow(["Net P&L      : " + str(net_total)])
    out_rec.writerow(["Greatest Increase in Profits: $ " +  str(greatest_increase[1]) + "     " + greatest_increase[0]])
    out_rec.writerow(["Greatest decrease in Profits: $" +  str(greatest_decrease[1]) + "     " + greatest_decrease[0]])
    out_rec.writerow(["Average change in Profits   : $  " + str(avg_chg)])

################################################################
####  Print above chart to screen (using fstring to format) ####
################################################################

print("\nFinancial Analysis")
print("-"*30)
print(f"Total Months :  {total_months}")
print(f"Net P&L      : $ {net_total}")
print(f"Greatest Increase in Profits: $ {greatest_increase[1]}     {greatest_increase[0]}")
print(f"Greatest decrease in Profits: ${greatest_decrease[1]}     {greatest_decrease[0]}")
print(f"Average change in Profits   : $  {avg_chg}\n")