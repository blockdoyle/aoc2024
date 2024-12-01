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

# Find how many times left column number appears in right column
def findFrequency(leftColumn, rightColumn):
    frequencies = []
    for i in range(len(leftColumn)):
        frequency = rightColumn.count(leftColumn[i])
        frequencies.append(leftColumn[i] * frequency)
    return frequencies

def removeZeroesFromArray(array):
    return [x for x in array if x != 0]

def sumFrequency(frequencies):
    sum = 0
    for frequency in frequencies:
        sum += frequency
    return sum

# Main
data = readFile()
leftColumn, rightColumn = separateData(data)
frequencies = removeZeroesFromArray(findFrequency(leftColumn, rightColumn))
sumFrequencies = sumFrequency(frequencies)

print(f"Sum of frequencies: {sumFrequencies}")