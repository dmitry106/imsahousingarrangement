
import csv
import numpy

class student:
    def __init__(self, ID, name, hallrating, friendsrating, roomrating, roomtype, hallchoice, wing1, wing2, roomlocation):
        self.name = name
        self.hallrating = hallrating
        self.friendsrating = friendsrating
        self.roomrating = roomrating
        self.roomtype = roomtype
        self.hallchoice = hallchoice
        self.wing1 = wing1
        self.wing2 = wing2
        self.roomlocation = roomlocation


students = dict() #dict to iterate list of variables




with open('MockHousingData.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        students[row[0]] = row
        print(students[row[0]])


print(students['2'])