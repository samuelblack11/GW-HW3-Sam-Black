# Allows us to create file paths across operating systems
import os
#import codecs

# Module for reading CSV files
import csv

# Define CSVPath of CSV
#csvpath = os.path.join('..', 'Desktop', 'GWDA', 'Homeworks', 'budgetdata.csv')
csvpath = 'budgetdata.csv'
#print(csvpath)

with open(csvpath, newline='') as csvfile:

#with open(csvpath, encoding ="utf8", errors = 'ignore', newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    #csvpath = codecs.open(csvpath,'rb','utf-16')
    csvreader = csv.reader(csvfile, delimiter=',')

    #initialize to begin file at top row
    linecount = 0

    #initialize line earinings and net earnings (sum of all lineearnings) to 0 
    netearnings = 0
    lineearnings = 0

    #To hold value of earnings from previous month
    prev = 0
   
   #Initialize to measure month to month change
    maxdelta = 0
    mindelta = 0

    # initialize month as int to avoid type str error
    month = 0

    # Initialize array for dates
    dates = []
    earningsbydate = []
    earningsbymonth = []
    rowdata = [] 
    fullindex = dict() 
    averagechange = []

    for row in csvreader:
        if linecount ==0:
            print(f'Column names are {",".join(row)}')
            linecount += 1
        else:
            #print(f'\t{row[0]} was the month I earned ${row[1]}')
            date = str({row[0]})
            dates.append(date)
            lineearnings = int(row[1])
            monthlydelta= lineearnings - prev
            averagechange.append(monthlydelta)
            if monthlydelta > maxdelta:
                maxdelta = monthlydelta
                maxdeltamonth = date
            if monthlydelta < mindelta:
                mindelta = monthlydelta
                mindeltamonth = date
            if date in fullindex:
                print ('error')
            else:
                fullindex[date]=lineearnings
            earningsbydate.append(lineearnings)
            rowdata.append(date)
            rowdata.append(lineearnings)
            prevdate = date
            prev = lineearnings
            linecount +=1
            netearnings += int(row[1])

    #Prints dictionary of Dates with corresponding profit/loss
    #print(fullindex)
   
    
#### Max & Min values of list, not of changes between months
    def maxandmin(earningsbydate):
        themax=max(earningsbydate)
        themin=min(earningsbydate)
        #themaximumincrease
        #themaximumdecrease
        return(f'Max: {themax} Min: {themin}')

    def monthcounter(dates):
        uniquemonths =[]
        for date in dates:
                # datedivider = csv.reader(csvfile, delimiter='/')
                # Divide dates into month,day,year where there is a '/'
                fulldate= date.split('-')
                # Returns Month with {' preceding it
                month = (fulldate[0])
                # Returns year with '} following it
                year = fulldate[1]
                uniquemonth = date
                #creates unique month/year combination, formatted as {'10 18'}
                if uniquemonth not in uniquemonths:
                    uniquemonths.append(uniquemonth)
                #return(f'{month}')
                monthcount = len(uniquemonths)

        return(f'Total Months: {monthcount}')
 
    counter= 0 
    def listbuilder(rowdata):
        for row in csvreader:
            if counter == 0:
                counter+=1
            else:
                rowdata.append(month)
                rowdata.append(day)
                rowadata.append(year)
                rowdata.append(uniquemonth)
                counter +=1

        return(f'Full Row: {rowdata}')



    # must be indented here otherwise file would be "closed"
    #print(listbuilder(rowdata))
   
#Print dates listed in file.       
#print(dates)

# Calculate Average Delta. Subtract 1 from linecount for header. 
averagedelta=int(sum(averagechange)/len(averagechange))
#averagedailydelta = int(netearnings /(linecount-1))



#Print total months
print(monthcounter(dates))
# Print net earnings
print(f'Total: ${netearnings}')
# Average Delta 
print(f'Average Delta: ${averagedelta}')
print(f'Max Increase: {maxdeltamonth} (${maxdelta})')
print(f'Max Decrease: {mindeltamonth} (${mindelta})')

output_path = 'pybankoutput.csv'

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow([monthcounter(dates)])
    csvwriter.writerow([f'Total: ${netearnings}'])
    csvwriter.writerow([f'Average Delta: ${averagedelta}'])
    csvwriter.writerow([f'Max Increase: {maxdeltamonth} (${maxdelta})'])
    csvwriter.writerow([f'Max Decrease: {mindeltamonth} (${mindelta})'])






#print(dailyearnings(dayearnings))
#print(maxandmin(earningsbydate))

