def main():
    slopeMap = []
    with open("input.txt") as file:
        for line in file:
            slopeMap.append(line.rstrip())
    solution = countCollisions(1, 1, slopeMap) * countCollisions(3, 1, slopeMap) * countCollisions(5, 1, slopeMap) * countCollisions(7, 1, slopeMap) * countCollisions(1, 2, slopeMap)
    print(str(solution))
        
def countCollisions(xMove, yMove, slopeMap):
    treeCollisions = 0
    stepCounter = 0
    index = 0
    while index < len(slopeMap):
        xCoordinate = (stepCounter * xMove) % len(slopeMap[index])
        if slopeMap[index][xCoordinate] == "#":
            treeCollisions = treeCollisions + 1
        index = index + yMove
        stepCounter = stepCounter + 1
    return treeCollisions
        

if __name__ == "__main__":
    main()