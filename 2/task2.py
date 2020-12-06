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
    indices = rule[0].split("-")
    ruleChar = rule[1]
    if (isSignAtIndex(ruleChar, int(indices[0])-1, password)) != (isSignAtIndex(ruleChar, int(indices[1])-1, password)):
        return True
    return False

def isSignAtIndex(sign, index, sequence):
    return sequence[index] == sign

if __name__ == "__main__":
    main()