#Importing modules and file
import os
import csv
file = os.path.join( os.getcwd(),'Resources','budget_data.csv')

#Defining variables

months = 0; 
totalpl = 0; 
initialv = 0;
dif = 0; 
maxdif = 0;
mindif = 0; 


#Loading csv file

with open(file, newline='') as csvfile:
     filereader = csv.reader(csvfile, delimiter=',')
     csv_header = next(filereader)
    
     for a in filereader:
        date = a[0]
        value = int(a[1])
        
        dif = value - initialv
        
        if (maxdif<dif):
            maxdif = dif
            daxdifd = date
            
        if (mindif>dif):
            mindif = dif
            mindifd = date 
            
        initialv = value
        months = months + 1
        totalpl = totalpl + value

# Print results

print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months : {months}')
print(f'Total: $ {totalpl}')
print(f'Greatest Increase in Profits: {daxdifd} : ($ {maxdif})')
print(f'Greatest Decrease in Profits: {mindifd} : ($ {mindif})')

# Exporting results to txt file

with open("Analysis.txt", "w") as text_file:

     print(f'Financial Analysis', file=text_file)
     print(f'----------------------------', file=text_file)
     print(f'Total Months : {months}', file=text_file)
     print(f'Total: $ {totalpl}', file=text_file)
     print(f'Greatest Increase in Profits: {daxdifd} : ($ {maxdif})', file=text_file)
     print(f'Greatest Decrease in Profits: {mindifd} : ($ {mindif})', file=text_file)
