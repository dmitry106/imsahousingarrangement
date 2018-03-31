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



costlist = []

selectioncost = [0,5,10]
hallcost = [0,5,10,15]
wingcost = [0,5,10,15]
wing2cost = [20]



def costofhousing (hall_friends_room,room_type,hall_choice,wing_1,wing_2,room_location,hall,wing,room,roomtype):
    #return hall_friends_room[:1]
    return hallcost[int(hall_friends_room[:1])-1]



students = dict() #dict to iterate list of variables

with open('MockHousingData.csv', newline='') as f1:
    has_header = csv.Sniffer().has_header(f1.read(1024))
    f1.seek(0)   #rewind to start
    reader1 = csv.reader(f1)
    if has_header:
        next(reader1)

    for rowhousing in reader1:

        testlist = []
        students[rowhousing[0]] = student(rowhousing[0],rowhousing[1],rowhousing[2],rowhousing[3],rowhousing[4],rowhousing[5],rowhousing[6],rowhousing[7])

        with open('HallRoomData.csv', newline='') as f2:
            has_header=csv.Sniffer().has_header(f2.read(1024))
            f2.seek(0)
            reader2 = csv.reader(f2)
            if has_header:
                next(reader2)
                
            for rowroom in reader2:
                print(rowhousing)
                print(rowroom)
                #testlist.append(costofhousing())
                


        
        
        print(costofhousing(rowhousing[2],rowhousing[3],rowhousing[4],rowhousing[5],rowhousing[6],rowhousing[7],1,1,1,1))
        
        #costlist.append([])



#print(students['2'].name)
#
#imput_array = numpy.array([[1,2,3]])
#append_array = [2,3,4,5]
#
#costlist.append(append_array)
#costlist.append(append_array)
#costlist.append(append_array)
#costlist.append(append_array)
#
##print(costlist)
#
#costlistarray = numpy.array(costlist)
#print(costlistarray)