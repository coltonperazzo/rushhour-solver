## rushhour.py
## colton perazzo
## university of california, davis

import copy
from queue import PriorityQueue

# We use ascii char codes to specify which cars are which.
X_VAL = 88 #Ascii code for "X".
GOAL = [[2,4],[2,5]] #Our goal state, the X vehicle should reach here.

def rushhour(heuristicState, initalState):
    rushhourArray = convertInputIntoNumberArray(initalState)
    aStarResults,explored = aStarAlgorithm(heuristicState, rushhourArray, GOAL)
    for pathState in aStarResults:
        for pathRow in pathState:
            printReadableMove(pathRow)
        print("\n")
    print("Total moves:", len(aStarResults)-1) # We minus one to not count the inital state in the path.
    print("Total states explored:", explored)

def convertInputIntoNumberArray(initalState):
    rushhourArray = []
    for i in range(6):
        rushhourArray.append([0,0,0,0,0,0])
        for j in range(6):
            if initalState[i][j] != "-":
                rushhourArray[i][j] = ord(initalState[i][j])
    return rushhourArray

def getCharOutput(pathCharacter):
    if pathCharacter == 0:
        return "-"
    return chr(int(pathCharacter))

def printReadableMove(pathRow):
    print(getCharOutput(pathRow[0])
            +getCharOutput(pathRow[1])
            +getCharOutput(pathRow[2])
            +getCharOutput(pathRow[3])
            +getCharOutput(pathRow[4])
            +getCharOutput(pathRow[5])
        )

def getLocationOfXVehicle(rushhourArray):
    vehicleLocation = []
    for i in range(6):
        if len(vehicleLocation) == 2: break
        if rushhourArray[2][i] == X_VAL:
          vehicleLocation.append([2,i])  
    return vehicleLocation

def getLocationOfOtherVehicle(rushhourArray, asciiValue):
    vehicleLocation = []
    for i in range(6):
        if len(vehicleLocation) == 3: break
        for j in range(6):
            if len(vehicleLocation) == 3: break
            if rushhourArray[i][j] == asciiValue:
                vehicleLocation.append([i,j])
    return vehicleLocation

def getLocationOfSelectVehicles(rushhourArray, selectArray):
    vehicleLocations = {} # Dictionary
    for asciiValue in selectArray:
        vehicleLocations[asciiValue] = getLocationOfOtherVehicle(rushhourArray, asciiValue)
    return vehicleLocations

def getNextPossibleVehicleMoves(rushhourArray):
    visitedVehicles = []
    possibleMoves = []
    for i in range(6):
        for j in range(6):
            if rushhourArray[i][j] != 0:
                if rushhourArray[i][j] not in visitedVehicles:
                    visitedVehicles.append(rushhourArray[i][j])
                    vehicleLocation = getLocationOfOtherVehicle(rushhourArray, rushhourArray[i][j])
                    vehicleLocationSize = len(vehicleLocation) - 1
                    if vehicleLocation[0][0] != vehicleLocation[1][0]: # This vehicle can only move vertically.
                        if vehicleLocation[0][0] != 0:
                            if rushhourArray[vehicleLocation[0][0] - 1][vehicleLocation[0][1]] == 0:
                                # This vehicle can move up.
                                newState = copy.deepcopy(rushhourArray)
                                for k in range(6):
                                    for l in range(6): 
                                        if [k,l] in vehicleLocation:
                                            newState[k-1][l] = rushhourArray[i][j]
                                            newState[vehicleLocation[vehicleLocationSize][0]][vehicleLocation[vehicleLocationSize][1]] = 0
                                possibleMoves.append(newState)
                        if vehicleLocation[vehicleLocationSize][0] != 5: 
                            if rushhourArray[vehicleLocation[vehicleLocationSize][0] + 1][vehicleLocation[vehicleLocationSize][1]] == 0:
                                # This vehicle can move down.
                                newState = copy.deepcopy(rushhourArray)
                                for k in range(6):
                                    for l in range(6): 
                                        if [k,l] in vehicleLocation:
                                            newState[k+1][l] = rushhourArray[i][j]
                                            newState[vehicleLocation[0][0]][vehicleLocation[0][1]] = 0
                                possibleMoves.append(newState)
                    else: # This vehicle can only move horizontally.
                        if vehicleLocation[0][1] != 0:
                            # This vehicle can move left.
                            if rushhourArray[vehicleLocation[0][0]][vehicleLocation[0][1] - 1] == 0:
                                # This vehicle can move left.
                                newState = copy.deepcopy(rushhourArray)
                                for k in range(6):
                                    for l in range(6): 
                                        if [k,l] in vehicleLocation:
                                            newState[k][l-1] = rushhourArray[i][j]
                                            newState[vehicleLocation[vehicleLocationSize][0]][vehicleLocation[vehicleLocationSize][1]] = 0
                                possibleMoves.append(newState)
                        if vehicleLocation[vehicleLocationSize][1] != 5:
                            if rushhourArray[vehicleLocation[vehicleLocationSize][0]][vehicleLocation[vehicleLocationSize][1] + 1] == 0:
                                # This vehicle can move right.
                                newState = copy.deepcopy(rushhourArray)
                                for k in range(6):
                                    for l in range(6): 
                                        if [k,l] in vehicleLocation:
                                            newState[k][l+1] = rushhourArray[i][j]
                                            newState[vehicleLocation[0][0]][vehicleLocation[0][1]] = 0
                                possibleMoves.append(newState)
    return possibleMoves

# Returns how many vehicles, other than the main vehicle X is blocking it's path to the exit.
# @param rushhourMatrix => matrix of the current state.
# @returns integer => number of vehicles blocking the exit, array => vehicles blocking the exit
def blockingHeuristic(rushhourArray):
    visitedVehicles = []
    vehiclesBlocking = []
    xVehicleLocation = getLocationOfXVehicle(rushhourArray)
    blockingXVehicle = 1
    if (xVehicleLocation == GOAL):
        blockingXVehicle = 0
    for i in range(xVehicleLocation[len(xVehicleLocation)-1][1]+1, 6):
        if rushhourArray[xVehicleLocation[0][0]][i] != X_VAL and rushhourArray[xVehicleLocation[0][0]][i] != 0:
            if rushhourArray[xVehicleLocation[0][0]][i] not in visitedVehicles:
                visitedVehicles.append(rushhourArray[xVehicleLocation[0][0]][i])
                blockingXVehicle = blockingXVehicle + 1
                vehiclesBlocking.append(rushhourArray[xVehicleLocation[0][0]][i])
    return blockingXVehicle, vehiclesBlocking

def distanceBlockedHeuristic(rushhourArray):
    vehiclesBlockingX, vehiclesBlockingXArray = blockingHeuristic(rushhourArray)
    vehiclesBlockingXAlsoBlocked = 0
    xVehicleLocation = getLocationOfXVehicle(rushhourArray)
    vehiclesBlockingXLocations = getLocationOfSelectVehicles(rushhourArray, vehiclesBlockingXArray)
    distanceToExit = GOAL[1][1] - xVehicleLocation[len(xVehicleLocation)-1][1]
    for asciiValue in vehiclesBlockingXLocations.keys():
        vehicleLocationSize = len(vehiclesBlockingXLocations[asciiValue]) - 1
        if vehiclesBlockingXLocations[asciiValue][0][0] != vehiclesBlockingXLocations[asciiValue][1][0]: 
            # Vertical vehicle (eg: check up/down).
            if vehiclesBlockingXLocations[asciiValue][0][0] != 0:
                if rushhourArray[vehiclesBlockingXLocations[asciiValue][0][0] - 1][vehiclesBlockingXLocations[asciiValue][0][1]] != 0:
                    vehiclesBlockingXAlsoBlocked = vehiclesBlockingXAlsoBlocked + 1
            else:
                vehiclesBlockingXAlsoBlocked = vehiclesBlockingXAlsoBlocked + 1
            if vehiclesBlockingXLocations[asciiValue][vehicleLocationSize][0] != 5: 
                if rushhourArray[vehiclesBlockingXLocations[asciiValue][vehicleLocationSize][0] + 1][vehiclesBlockingXLocations[asciiValue][vehicleLocationSize][1]] != 0:
                    vehiclesBlockingXAlsoBlocked = vehiclesBlockingXAlsoBlocked + 1
            else:
                vehiclesBlockingXAlsoBlocked = vehiclesBlockingXAlsoBlocked + 1
        else: 
            # Horizontal vehicle.
            if vehiclesBlockingXLocations[asciiValue][0][1] != 0: 
                if rushhourArray[vehiclesBlockingXLocations[asciiValue][0][0]][vehiclesBlockingXLocations[asciiValue][0][1] - 1] != 0:
                    vehiclesBlockingXAlsoBlocked = vehiclesBlockingXAlsoBlocked + 1
            else:
                vehiclesBlockingXAlsoBlocked = vehiclesBlockingXAlsoBlocked + 1
            if vehiclesBlockingXLocations[asciiValue][vehicleLocationSize][1] != 5:
                if rushhourArray[vehiclesBlockingXLocations[asciiValue][vehicleLocationSize][0]][vehiclesBlockingXLocations[asciiValue][vehicleLocationSize][1] + 1] != 0:
                    vehiclesBlockingXAlsoBlocked = vehiclesBlockingXAlsoBlocked + 1
            else:
                vehiclesBlockingXAlsoBlocked = vehiclesBlockingXAlsoBlocked + 1
    return vehiclesBlockingXAlsoBlocked + distanceToExit

def aStarAlgorithm(heuristicState, initialState, goalState):
    seen = [initialState]
    unexplored = PriorityQueue()
    unexplored.put((1, [initialState]))
    explored = 0
    while not unexplored.empty():
        cost,path = unexplored.get()
        explored = explored + 1
        if path[-1][2][4] == X_VAL and path[-1][2][5] == X_VAL:
            break
        for nextState in getNextPossibleVehicleMoves(path[-1]):
            if nextState not in seen:
                seen.append(nextState)
                newPath = copy.deepcopy(path)
                newPath.append(nextState)
                totalCost = cost
                if heuristicState == 0:
                    vehiclesBlockingX, _ = blockingHeuristic(nextState)
                    totalCost = totalCost + vehiclesBlockingX
                else:
                    totalCost = totalCost + distanceBlockedHeuristic(nextState)
                unexplored.put((totalCost, newPath))
    return path, explored
