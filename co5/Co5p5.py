import csv

student =[{'No':1,'name':'Haseena','role':'student'}]
csv_f =open('Name.csv','w')
field_name= list(student[0].keys())

csv_w  =csv.DictWriter(csv_f,fieldnames=field_name)
csv_w.writeheader()+
csv_w.writerows(student)
csv_f.close()
