import os

import csv

csvpath = "C:/Users/hilda/Desktop/Learn_Python/election_data.csv"

with open(csvpath, newline='') as csvfile:

    csvread = csv.reader(csvfile, delimiter=',')

    Total_Votes = 0
    K_Votes = 0
    C_Votes = 0
    L_Votes = 0
    O_Votes = 0

    #print(csvread)
    next(csvread)

    for row in csvread:
        #print(row[2])
        Total_Votes += 1


with open(csvpath, newline='') as csvfile:

    csvread = csv.reader(csvfile, delimiter=',')

    next(csvread)

    for row in csvread:
        if row[2] == "Khan":
            K_Votes += 1

        if row[2] == "Correy":
            C_Votes += 1

        if row[2] == "Li":
            L_Votes += 1

        if row[2] == "O'Tooley":
            O_Votes += 1
    
    if max(K_Votes,C_Votes,L_Votes,O_Votes) == K_Votes:
        Winner = "Khan"

    if max(K_Votes,C_Votes,L_Votes,O_Votes) == C_Votes:
        Winner = "Correy"

    if max(K_Votes,C_Votes,L_Votes,O_Votes) == L_Votes:
        Winner = "Li"
    
    if max(K_Votes,C_Votes,L_Votes,O_Votes) == C_Votes:
        Winner = "O'Tooley"
            



# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

print('Election Results')
print('-------------------')
print("Total votes: " + str(Total_Votes))
print(" ")
print('Khan: ' + str(round((K_Votes/Total_Votes)*100)) + "% " + str(K_Votes))
print('Correy: ' + str(round((C_Votes/Total_Votes)*100)) + "% " + str(C_Votes))
print('L1: ' + str(round((L_Votes/Total_Votes)*100)) + "% " + str(L_Votes))
print("O'Tooley: " + str(round((O_Votes/Total_Votes)*100)) + "% " + str(O_Votes))
print(" ")
print('Winner: ' + Winner)
