def main():
    slopeMap = []
    with open("input.txt") as file:
        for line in file:
            slopeMap.append(line.rstrip())
    print(countCollisions(slopeMap))    
        
def countCollisions(slopeMap):
    treeCollisions = 0
    for index in range(0, len(slopeMap)):
        xCoordinate = (index * 3) % len(slopeMap[index])
        if slopeMap[index][xCoordinate] == "#":
            treeCollisions = treeCollisions + 1
    return treeCollisions
        

if __name__ == "__main__":
    main()