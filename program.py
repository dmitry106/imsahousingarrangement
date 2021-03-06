import sys
import os
import csv
import numpy
from scipy.optimize import linear_sum_assignment
#from cement.core.foundation import CementApp
#from cement.core import hook
#from cement.core.controller import CementBaseController, expose
#from cement.utils.misc import init_defaults


#Not needed for anything as of now
class student:
    def __init__(self, ID, name, hall_friends_room, room_type, hall_choice, wing_1, wing_2, room_location):
        self.id = int(ID)
        self.name = name
        self.hall_friends_room = hall_friends_room
        self.room_type = room_type
        self.hall_choice = hall_choice
        self.wing_1 = wing_1
        self.wing_2 = wing_2
        self.room_location = room_location

class housingroom:
    def __init__(self, ID, hall, wing, room, room_type):
        self.id = int(ID)
        self.hall = hall
        self.wing = wing
        self.room = room
        self.room_type = room_type



#cost for 
roomtypecost = [5]
roomlocationcost = [5]
hallcost = [0,5,30,40] #NOTE: 2nd and 3rd cost needs to be high enough to offset the added cost for 2nd choice hall without getting preferred wing
wingcost = [0,5,10,15]
wing2cost = [10]


#NOTE: this function is for debugging purposes only
def is_squared(matrix):
    # Check that all rows have the correct length, not just the first one
    return all(len(row) == len(matrix) for row in matrix)

def pad_to_square(a, pad_value):
    m = a.reshape((a.shape[0], -1))
    padded = pad_value * numpy.ones(2 * [max(m.shape)], dtype=m.dtype)
    padded[0:m.shape[0], 0:m.shape[1]] = m
    return padded

def costfunction(choices, chosen, costlist):
    
    for i in range(0, len(choices)):
        if choices[i] == chosen:
            choice = i
            break
    return costlist[int(choice)]



def costofhousing (hall_friends_room,room_type,hall_choice,wing_1,wing_2,room_location,hall,wing,room,roomtype):
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
        score += roomtypecost[0]*roommultiplier



    return score


def main():
    #get the arguments passed to the program
    script = sys.argv[0]
    action = sys.argv[1]
    files = sys.argv[2:]
    #only 1 function, to calculate the optimised housing list
    assert action in ['--calc'], \
           'Need action --calc ' + action
    


    students = dict() #dict to iterate list of variables for the students
    housingrooms = dict() #same for the rooms

    maxnumberofstudent = 0

    costlist = []

    with open(sys.argv[2], newline='') as f1:
        has_header = csv.Sniffer().has_header(f1.read(1024)) #find that header and skip it
        f1.seek(0)   #rewind to start
        reader1 = csv.reader(f1)
        if has_header:
            next(reader1)

        for rowhousing in reader1:
            maxnumberofstudent = maxnumberofstudent + 1 #NOTE: This is for later to determine the maximum number of loops to do so you don't end up iterating over the null values to make the matrix square
            #assigning the values of the student preferences
            students[int(rowhousing[0])] = student(rowhousing[0],rowhousing[1],rowhousing[2],rowhousing[3],rowhousing[4],rowhousing[5],rowhousing[6],rowhousing[7])

            rowlist = []
            
            with open(sys.argv[3], newline='') as f2:
                has_header=csv.Sniffer().has_header(f2.read(1024)) #skip the header
                f2.seek(0)  #rewind to start
                reader2 = csv.reader(f2)
                if has_header:
                    next(reader2)
                
                for rowroom in reader2:
                    #Assign values for the room dict as well
                    housingrooms[int(rowroom[0])] = housingroom(rowroom[0],rowroom[1],rowroom[2],rowroom[3],rowroom[4])
                    #making the list that will be turned into a cost matrix
                    rowlist.append(costofhousing(rowhousing[2],rowhousing[3],rowhousing[4],rowhousing[5],rowhousing[6],rowhousing[7],rowroom[1],rowroom[2],rowroom[3],rowroom[4]))
            

            costlist.append(rowlist)
        
    #Convert the costlist into a numpy array for ease of manipulation
    costlist = numpy.asarray(costlist)

    #in order for the algorithm to optimise correctly it needs to be a square matrix
    costlist = pad_to_square(costlist, costlist.max())

    #print(is_squared(costlist)) NOTE: should result in affirmative in order for the rest to work


    resultmatrix = linear_sum_assignment(costlist) #the magic happens here
    row_ind, col_ind = resultmatrix
    tuplesofhousing = list(zip(row_ind,col_ind))
    housingassignmentarray = numpy.asarray(tuplesofhousing)
    #print(housingassignmentarray)

    housingassignmentarray = numpy.asarray(list(map(lambda x: x+1 ,housingassignmentarray)))

    #Getting a csv ready to write the output to
    with open(sys.argv[4], 'w', newline='') as writer1:
        writer = csv.writer(writer1)
        
        for row in housingassignmentarray:
            if row[0] > maxnumberofstudent: #NOTE:NOTE:NOTE:NOTE THIS TOTAL TRASH if STATEMENT IS A SAD SOLUTION FOR row[0] STUDENTS and I hate it
                break
            #print(students[row[0]].name,"to",housingrooms[row[1]].hall,housingrooms[row[1]].wing,housingrooms[row[1]].room)
            writer.writerow([students[row[0]].name,housingrooms[row[1]].hall,housingrooms[row[1]].wing,housingrooms[row[1]].room])

#bash/powershell convention
if __name__ == '__main__':
    main()
