
import csv

with open('MockHousingData.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


