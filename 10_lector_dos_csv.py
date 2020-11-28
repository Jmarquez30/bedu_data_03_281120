import csv 

filename = 'employees.csv'

with open(filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        #print(row['Salary']) solo estar seguros ques existe salary
        s = row.get('Salary')
        n = row.get('Name')
        print(f'{n} earns {s}')