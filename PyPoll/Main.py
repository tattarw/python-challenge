#Importing modules and file

import os
import csv
file = os.path.join(os.getcwd(),'Resources','election_data.csv')


#Defining variables

voterid = []
county = []
candidates = []

khan = []
correy = []
li = []
otooley = []

#Loading csv file

with open(file, newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',')
    csv_header = next(filereader)

    for a in filereader:
        voterid.append(a[0])
        county.append(a[1])
        candidates.append(a[2])

    total = (len(voterid))

#Calculating the number of votes 

    for candidate in candidates:
        
        if candidate == "Khan":
            khan.append(candidate)
            k_votes = len(khan)
            
        elif candidate == "Correy":
            correy.append(candidate)
            c_votes = len(correy)
            
        elif candidate == "O'Tooley":
            otooley.append(candidate)
            o_votes = len(otooley)
            
        else:
            li.append(candidate)
            l_votes = len(li)
            
    
#Percentage of votes for each candidate

    khan_p = round(((k_votes / total) * 100), 2)
    correy_p = round(((c_votes / total) * 100), 2)
    li_p = round(((l_votes / total) * 100), 2)
    otooley_p = round(((o_votes / total) * 100), 2)
    
#Determining the winner 

    if khan_p > max(correy_p, li_p, otooley_p):
        winner = "Khan"
        
    elif correy_p > max(khan_p, li_p, otooley_p):
        winner = "Correy"  
        
    elif li_p > max(correy_p, khan_p, otooley_p):
        winner = "Li"
        
    else:
        winner = "O'Tooley"


# Printing the results to the screen 

print(f'Election Results')
print(f'----------------------------')
print(f'Total votes: {total}')
print(f'Khan: {khan_percent}% ({k_votes})')
print(f'Correy: {correy_percent}% ({c_votes})')
print(f'Li: {li_percent}% ({l_votes})')
print(f'OTooley: {otooley_percent}% ({o_votes})') 
print(f'-----------------------------------')
print(f'Winner: {winner}')
print(f'-----------------------------------')

# Exporting results to txt file

with open("Winner.txt", "w") as text_file:

    print(f'Election Results', file=text_file)
    print(f'----------------------------', file=text_file)
    print(f'Total votes: {total}', file=text_file)
    print(f'Khan: {khan_percent}% ({k_votes})', file=text_file)
    print(f'Correy: {correy_percent}% ({c_votes})', file=text_file)
    print(f'Li: {li_percent}% ({l_votes})', file=text_file)
    print(f'OTooley: {otooley_percent}% ({o_votes})', file=text_file)
    print(f'-----------------------------------', file=text_file)
    print(f'Winner: {winner}', file=text_file)
    print(f'-----------------------------------', file=text_file)

