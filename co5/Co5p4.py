import csv
with open('studentdetails.csv','r') as csv_f:
    csv_r =csv.DictReader(csv_f)
    print("RollNO  Name")
    print("---------------------------------")
    for line in csv_r:
        print(line['Roll No'],"",line['Student Name'])   
Give feedback
