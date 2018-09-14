
# Allows us to create file paths across operating systems
import os
#import codecs


# Module for reading CSV files
import csv

# Define CSVPath of CSV
#csvpath = os.path.join('..', 'Desktop', 'electiondata.csv')
csvpath = os.path.join('electiondata.csv')
print(csvpath)

with open(csvpath, newline='') as csvfile:

#with open(csvpath, encoding ="utf8", errors = 'ignore', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    #csvpath = codecs.open(csvpath,'rb','utf-8')
    csvreader = csv.reader(csvfile, delimiter=',')

    linecount = 0
    #initialize to begin file at top row
    linecounter = []
    khancount=int(0)
    correycount=int(0)
    licount=int(0)
    otooleycount=int(0)
    othercandidate =0
    #def totalvotes(linecounter):
    for row in csvreader:
        countpercandidate = [{khancount}, {correycount}, {licount}, {otooleycount}]
        if linecount ==0:
            print(f'Column names are {",".join(row)}')
            linecount += 1
        else:
            voterchoice = str({row[2]})
            votechoice=voterchoice[2:-2]
            linecount +=1
            linecounter.append(linecount)
            if votechoice == "Khan":
                khancount+=1
            elif votechoice == "Correy":
                correycount+=1
            elif votechoice == "Li":
                licount+=1
            elif votechoice == "O'Tooley":
                otooleycount+=1
            else:
                othercandidate+=1
        #return(f'Total Votes: {len(linecounter)}')    

    khanper = ('{0:.3f}%'.format((khancount/linecount)*100))
    correyper =('{0:.3f}%'.format((correycount/linecount)*100))
    liper = ('{0:.3f}%'.format((licount/linecount)*100))
    otooleyper = ('{0:.3f}%'.format((otooleycount/linecount)*100))
    
    themax = max(countpercandidate)
    winner = 'the winner'
    def whowon(winner):
        if themax == {khancount}:
            winner = 'Khan'
        elif themax == {correycount}:
            winner = 'Correy'
        elif themax == {licount}:
            winner = 'Li'
        elif themax ==  {otooleycount}:
            winner = "O'Tooley"
        return(f'Winner: {winner}')

 

    # Print total votes
    #print(totalvotes(linecounter))

    print(f'Total Votes: {linecount}')
    print(f'Khan: {khanper} {khancount}')
    print(f'Correy: {correyper} {correycount}')
    print(f'Li: {liper} {licount}')
    print(f'O\'Tooley: {otooleyper} {otooleycount}')
    print(f'Other Candidates: {othercandidate}')
    print(whowon(winner))



    output_path = 'pypolloutput.csv'

    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([f'Total Votes: {linecount}'])
        csvwriter.writerow([f'Khan: {khanper} {khancount}'])
        csvwriter.writerow([f'Correy: {correyper} {correycount}'])
        csvwriter.writerow([f'Li: {liper} {licount}'])
        csvwriter.writerow([f'OTooley: {otooleyper} {otooleycount}'])
        csvwriter.writerow([f'Other Candidates: {othercandidate}'])
        csvwriter.writerow([whowon(winner)])




