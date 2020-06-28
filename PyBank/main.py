##################################################################################
#  RUT-SOM-DATA-PT-06-2020-U-C                                      Douglas High #
#   Python Challenge                                               June 27, 2020 #
#      >PyBanker                                                                 #
#   - Read input csv file, tally monthly P&L and average change                  #
#   - produces output to txt file, summarizing data                              #
##################################################################################
#####################
####  I/O Setup  ####
#####################
import os
import csv
import numpy
os.chdir(os.path.dirname(os.path.abspath(__file__)))           # Set Directory
budget_raw = os.path.join("Resources","budget_data.csv")       # associate input file
budget_sum = os.path.join("Analysis","budget_summary.txt")     # associate output file

################################################
####  Define and Initialize Data Variables  ####
################################################
total_months = 0
net_total = 0
greatest_increase = ["Jan-1900",-999]
greatest_decrease = ["Jan-1900",9999]
month_hold = 0
monthly_change_list = []

###################################################################################
####  read input: accumulate P&L and monthly change, determine extreme months  ####
###################################################################################
with open(budget_raw) as infile:
    in_rec = csv.reader(infile, delimiter = ",")
    next(infile)
    for row in in_rec:
        total_months += 1
        net_total += int(row[1])
        if int(row[1]) > greatest_increase[1]:           # find greatest increse and decrese
            greatest_increase[0] = row[0]
            greatest_increase[1] = int(row[1])
        elif int(row[1]) < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = int(row[1])
        if total_months == 1:                            # if first record, set month hold
            month_hold = int(row[1])
        else:
            monthly_change_list.append(int(row[1]) - month_hold)   # accumulate list of monthly changes
            month_hold = int(row[1])
avg_chg = round(float(numpy.mean(monthly_change_list)),2)          # Calculate average monthly change in P&L

###################################################
####  Write output summary (pseudo-formatted)  ####
###################################################
with open(budget_sum,'w',newline='') as outfile:
    out_rec = csv.writer(outfile)
    out_rec.writerow(["             Financial Analysis"])
    out_rec.writerow(["-"*53])
    out_rec.writerow(["Total  number of Months     :  " + str(total_months)])
    out_rec.writerow(["Net Profit and Loss         : $ " + str(net_total)])
    out_rec.writerow(["Average change in Profits   : $    " + str(avg_chg)])
    out_rec.writerow(["Greatest Increase in Profits: $  " +  str(greatest_increase[1]) + "     " + greatest_increase[0]])
    out_rec.writerow(["Greatest decrease in Profits: $ " +  str(greatest_decrease[1]) + "     " + greatest_decrease[0]])

################################################################
####  Print above chart to screen (using fstring to format) ####
################################################################
print("\n          Financial Analysis")
print("-"*53)
print(f"Total  Number  of  Months   :  {total_months}")
print(f"Net Profit and Loss         : $ {net_total}")
print(f"Average change in Profits   : $    {avg_chg}")
print(f"Greatest Increase in Profits: $  {greatest_increase[1]}     {greatest_increase[0]}")
print(f"Greatest decrease in Profits: $ {greatest_decrease[1]}     {greatest_decrease[0]}\n")