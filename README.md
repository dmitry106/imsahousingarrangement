# IMSA Housing program development

## IMSA Housing
Fix housing by using the solution for the assignment problem to automate housing choice for the RCs with extension to the Stable marriage problem for increased happiness-rating.



## Background and Context:
https://en.wikipedia.org/wiki/Assignment_problem

http://www.math.harvard.edu/archive/20_spring_05/handouts/assignment_overheads.pdf







## Usage
https://mockaroo.com/ for the random data

Install python 3: https://www.python.org/downloads/release/python-365/

CLICK add to PATH checkbox on first options screen

Numpy: pip install numpy

Scipy: pip install scipy

run in powershell or cmd: python .\program.py --calc .\<csv of all students being housed> .\<csv of all availiable rooms they can be housed in> .\<whatever output csv file for the assignments>

Example that will work in the directory of this: python .\program.py --calc .\MockHousingData.csv .\HallRoomData.csv .\output.csv

## Details of how to exclude quads and leadership
YOU MUST EXCLUDE ANY QUADS AND ALL LEADERSHIP HOUSINGS FROM THE PROGRAM OR THE WORLD WILL END

Do this by:
1) decide on housing for leadership and quads
2) go into the csv of the students being housed and remove the entry for the room pair that will be housed
3) go into the csv of the hall room data and remove the room that you decided to house them in
4) run program as normally, it will not take into account that roommate pair or their room

Example: removing student1 and housing him manually into 07D13 with the github example files

1) decide to house Haydon in 07D13
2) go to MockHousingData.csv and remove the row for Haydon completely
3) go to HallRoomData.csv and remove the row for 07 D 13
4) run the program as normally


