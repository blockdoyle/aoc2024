# Read file and return data as an array of integers
def readFile():
    with open('challenge-1-input.txt') as f:
        data = f.readlines()
    result = []
    for line in data:
        numbers = line.split()
        result.extend([int(x) for x in numbers])
    return result

# Separate data into two columns
def separateData(data):
    leftColumn = []
    rightColumn = []
    for i in range(0, len(data), 2):
        leftColumn.append(data[i])
        if i + 1 < len(data):
            rightColumn.append(data[i + 1])
    return leftColumn, rightColumn

# Find Distance between two columns
def findDistance(leftColumn, rightColumn):
    pairArray = []
    for i in range(len(leftColumn)):
        if leftColumn[i] > rightColumn[i]:
            pairArray.append(leftColumn[i] - rightColumn[i])
        else:
            pairArray.append(rightColumn[i] - leftColumn[i])
    return pairArray

# Get the sum of the distances between the two columns
def getSumOfDistances(distanceArray):
    sum = 0
    for distance in distanceArray:
        sum += distance
    return sum

data = readFile()
leftColumn, rightColumn = separateData(data)
leftColumn.sort() # Sort left column
rightColumn.sort() # Sort right column
distanceArray = findDistance(leftColumn, rightColumn)
sumDistances = getSumOfDistances(distanceArray)

print(f"Sum of distances between the two columns: {sumDistances}")