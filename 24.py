import csv

fields = ["Name","Branch","Year","Score"]

rows = [['Nikhil', 'COE', '2', '9.0'],['Sanchit', 'COE','2','9.1'],[ 'Saurabh', 'COE', '2', '9.2'],['Siddharth', 'COE', '2', '9.3'],['Sagar','SE','2','9.4']]

filename = "university_records.csv"

with open(filename, "w") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(rows)
