##################################################################################
#  RUT-SOM-DATA-PT-06-2020-U-C                                      Douglas High #
#   Python Challenge                                               June 27, 2020 #
#      >PyPoll                                                                   #
#   - Read input csv file and create list of candidates, then accumulate votes.  #
#   - calculate candidates percentage of votes and winner.                       #
#   - produce output to txt file and display to screen.                          #
##################################################################################
#####################
####  I/O Setup  ####
#####################
import os
import csv
#import operator
#import numpy
os.chdir(os.path.dirname(os.path.abspath(__file__)))           # set directory
election_data = os.path.join("Resources","election_data.csv")  # associate input file
election_sum = os.path.join("Analysis","election_summary.txt")            # associate output file

#################################
####  Define Data Variables  ####
#################################
total_votes = 0
candidates = []
votes = []
per_votes = []

########################################################################################
####  read file once to get unique set of candidate names and fill candidates list  ####
########################################################################################
with open(election_data) as infile:
    in_rec = csv.reader(infile, delimiter = ",")
    next(infile)
    for row in in_rec:
        if row[2] not in candidates: 
                candidates.append(row[2])        # fill candidates list
                votes.append(int(row[0]))        # initialize votes buckets
for x in range(len(votes)):                      # zero out buckets for votes
    votes[x] = 0

###################################################################
####  read file again to accumulate votes and fill votes list  ####
###################################################################
with open(election_data) as infile:
    in_rec = csv.reader(infile, delimiter = ",")
    next(infile)
    for row in in_rec:
        total_votes += int(row[0])                # accumulate total votes for all candidates
        for x in range(len(candidates)):
            if row[2] == candidates[x]:
                votes[x] += int(row[0])           # accumulate votes for each candidate

#####################################################################################
####  Determine winner(assuming no tie) and calculate and fill percentage array  ####
#####################################################################################
winner = votes.index(max(votes))
for x in range(len(votes)):                                         
    per_votes.append(round((votes[x]/total_votes) * 100,2))  

#########################################################################
####  Write output file with summary information (pseudo-formatted)  ####
#########################################################################
with open(election_sum,"w",newline='') as outfile:
    out_rec = csv.writer(outfile)
    out_rec.writerow (["        Election Results"])
    out_rec.writerow (["-"*34])
    out_rec.writerow (["Total Votes : " + str(total_votes)])
    out_rec.writerow (["-"*34])
    for x in range(len(votes)):
        out_rec.writerow ([candidates[x] +"  " + str(per_votes[x]) + "%   (" + str(votes[x]) + ")"])
    out_rec.writerow (["-"*34])
    out_rec.writerow (["Winner : " + candidates[winner]])
    out_rec.writerow (["-"*34])         

#######################################
####  Print above chart to screen  ####
#######################################
print("\n       Election Results")
print("-"*34)
print("Total Votes : " + str(total_votes))
print("-"*34)
for x in range(len(votes)):
    print(candidates[x] +"  " + str(per_votes[x]) + "%   (" + str(votes[x]) + ")")
print("-"*34)
print("Winner : " + candidates[winner])
print("-"*34 + "\n")