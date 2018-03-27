
import csv
import numpy

class student:
    def __init__(self, ID, name, hall_friends_room, room_type, hall_choice, wing_1, wing_2, room_location):
        self.name = name
        self.hall_friends_room = hall_friends_room
        self.room_type = room_type
        self.hall_choice = hall_choice
        self.wing_1 = wing_1
        self.wing_2 = wing_2
        self.room_location = room_location


students = dict() #dict to iterate list of variables

with open('MockHousingData.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        students[row[0]] = student(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])



print(students['2'].name)