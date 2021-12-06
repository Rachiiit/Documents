import csv
file = open('test_file.csv')

csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)

data = [ row for row in csvreader  ]
print(data)


#writing to a file
#1. create file
filename = open('Students_Data.csv','w',newline="")
csvwriter = csv.writer(filename) ## 2. create a csvwriter object
csvwriter.writerow(header) # 3. write the header
csvwriter.writerows(data) # 4. write the rest of the data

file.close()
filename.close()