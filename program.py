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

#cost for 
roomtypecost = [5]
roomlocationcost = [5]
hallcost = [0,5,30,40] #NOTE: the hall cost for 3rd and 4th choice needs to be higher than the combined hall and wing costs
wingcost = [0,5,10,15]
wing2cost = [10]


    
def costfunction(choices, chosen, costlist):
    
    for i in range(0, len(choices)):
        if choices[i] == chosen:
            choice = i
            break
    return costlist[int(choice)]



def costofhousing (hall_friends_room,room_type,hall_choice,wing_1,wing_2,room_location,hall,wing,room,roomtype):
    #return hall_friends_room[:1]
    #hallmultiplier = 0
    #roommultiplier = 0
    score = 0
    # set the multiplier for preference of hall or room
    if int(hall_friends_room[:1]) > int(hall_friends_room[-1:]):
        hallmultiplier = 1 #hall multiplier is smaller because more cost is less preferential
        roommultiplier = 2
    elif int(hall_friends_room[:1]) < int(hall_friends_room[-1:]):
        hallmultiplier = 2
        roommultiplier = 1

    score += hallmultiplier*costfunction(hall_choice,hall,hallcost) #add hall choice cost

    if hall_choice[0] == hall: #if the 1st choice hall is chosen, then add the wing choices
        score += costfunction(wing_1,wing,wingcost)

    if (hall_choice[1] == hall) and (wing_2 != wing): #if the hall is 2nd choice check if it is the desired wing
        score += wing2cost[0]

    if room_type == roomtype:
        score += roomtypecost[0]

    #if room_location == roomlocation:
    #    score += roomlocationcost[0]
    


    #score += hallmultiplier*costfunction(hall_choice,hall,hallcost) + costfunction(wing_1,wing,wingcost)

    return score



students = dict() #dict to iterate list of variables

with open('MockHousingData.csv', newline='') as f1:
    has_header = csv.Sniffer().has_header(f1.read(1024))
    f1.seek(0)   #rewind to start
    reader1 = csv.reader(f1)
    if has_header:
        next(reader1)

    for rowhousing in reader1:

        students[rowhousing[0]] = student(rowhousing[0],rowhousing[1],rowhousing[2],rowhousing[3],rowhousing[4],rowhousing[5],rowhousing[6],rowhousing[7])

        rowlist = []

        with open('HallRoomData.csv', newline='') as f2:
            has_header=csv.Sniffer().has_header(f2.read(1024))
            f2.seek(0)  #rewind to start
            reader2 = csv.reader(f2)
            if has_header:
                next(reader2)
            for rowroom in reader2:
                print(rowhousing)
                print(rowroom)
                print(costofhousing(rowhousing[2],rowhousing[3],rowhousing[4],rowhousing[5],rowhousing[6],rowhousing[7],rowroom[1],rowroom[2],rowroom[3],rowroom[4]))
                rowlist.append(costofhousing(rowhousing[2],rowhousing[3],rowhousing[4],rowhousing[5],rowhousing[6],rowhousing[7],rowroom[1],rowroom[2],rowroom[3],rowroom[4]))
                print(rowlist)
        costlist.append(rowlist)
    

print(costlist)

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