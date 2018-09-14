# Allows us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Define CSVPath of CSV
csvpath = 'employeedata.csv'

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    linecount = 0


    dobyearlist =[]
    dobmonthlist=[]
    dobdaylist=[]
    fullnamelist=[]
    firstnamelist=[]
    lastnamelist=[]
    finalformatter = dict()
    output_path = 'pybossoutput.csv'

    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

    with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

        for row in csvreader:
            if linecount ==0:
                print(f'Column names are {",".join(row)}')
                linecount += 1
            else:
                    empid = row[0]
                    name = row[1]
                    fullname=name.split(' ')
                    fullnamelist.append(fullname)
                    firstname = fullname[0]
                    firstnamelist.append(firstname)
                    lastname = fullname[1]
                    lastnamelist.append(lastname)
                    bday = row[2]
                    dob = bday.split('-')
                    dobyear=dob[0]
                    dobyearlist.append(dobyear)
                    dobmonth=dob[1]
                    dobmonthlist.append(dobmonth)
                    dobday=dob[2]
                    dobdaylist.append(dobday)
                    formatteddob=(f"{dobmonth}/{dobday}/{dobyear}")
                    ssn = row[3]
                    ssn = list(ssn)
                    ssn[0]= '*'
                    ssn[1]= '*'
                    ssn[2]= '*'
                    ssn[3]= '*'
                    ssn[4] = '*'
                    formattedssn=(f"{ssn[0]}{ssn[1]}{ssn[2]}-{ssn[3]}{ssn[4]}-{ssn[7]}{ssn[8]}{ssn[9]}{ssn[10]}")
                    state=row[4]
                    stateabbrev = us_state_abbrev.get(state)
                    finalformatter = empid,firstname,lastname,formatteddob,formattedssn, stateabbrev
                    print(finalformatter)
                    csvwriter.writerow(finalformatter)
                    linecount+=1


