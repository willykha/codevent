def main():
    validCounter = 0
    linecount=0
    with open("input.txt") as file:
        for line in file:
            #rstrip() removes \n from line
            if checkLine(line.rstrip()):
                validCounter = validCounter + 1
    print(str(validCounter))

def checkLine(line):
    line = line.split(": ")
    rule = line[0].split(" ")
    password = line[1]
    return isValidPassword(rule, password)

def isValidPassword(rule, password):
    minMax = rule[0].split("-")
    ruleChar = rule[1]
    occurences = getOccurences(ruleChar, password)
    if (occurences >= int(minMax[0])) and (occurences <= int(minMax[1])):
        return True
    return False

def getOccurences(sign, sequence):
    occurences = 0
    for char in sequence:
        if sign == char:
            occurences = occurences + 1
    return occurences

if __name__ == "__main__":
    main()