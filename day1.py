import sys
import time

directions = ["U", "R", "D", "L"]
axes = [1, 0, 1, 0]
weights = [1, 1, -1, -1]

currentdirection = "U"
currentcoord = [0,0]
currentsteps = ""

traversed = []
seen_repeat = False

def move(coord, direction, step, seen_repeat):
    axis = axes[directions.index(direction)]
    weight = weights[directions.index(direction)] 
    
    for i in range (step):   
        coord[axis] += weight
        if checkHistory((coord[0], coord[1]), traversed) and seen_repeat == False:
            print ("Repeat coordinates: ", (coord[0], coord[1]))
            seen_repeat = True
        traversed.append((coord[0], coord[1]))        
                                                
    return coord, seen_repeat

def changeDirection(directions, current, change):
    if change == "R":
        current = directions[(directions.index(current) + 1)%len(directions)]
    elif change == "L":
        current = directions[(directions.index(current) - 1)%len(directions)]    
    return current

def checkHistory(coord, traversed):
    return coord in traversed
    
if __name__ == "__main__":
    input = sys.argv[1]

    f = open(input, "r")
    for line in f.read():  
        if line == "R" or line == "L":
            currentdirection = changeDirection(directions, currentdirection, line)
        elif line == "," or line == " " or line == "\n":
            if currentsteps == "":
                continue
            currentcoord, seen_repeat = move(currentcoord, currentdirection, int(currentsteps), seen_repeat)
            currentsteps = ""
        else:
            currentsteps += line
    print(currentcoord)
        
    