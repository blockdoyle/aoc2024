# Read file and return data as an array of integers
def readFile():
    with open('challenge-3-input.txt') as f:
        data = [line.strip() for line in f.readlines()]
    return (data)

# Split item into an array of integers
def splitItem(item):
    return [int(x) for x in item.split(' ')]

# For this challenge, safe levels are defined as levels that are within 3 of the current level
def findMaxDifference(currentInteger):
    maxLow = currentInteger - 3
    if maxLow < 0:
        maxLow = 0
    maxHigh = currentInteger + 3
    return (maxLow, maxHigh)

# Check if array of integers is always increasing or decreasing
def checkIfIncreasingOrDecreasing(array):
    increasing = True
    decreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            decreasing = False
        if array[i] < array[i-1]:
            increasing = False
        if array[i] == array[i-1]:
            return "The array is neither increasing nor decreasing and is UNSAFE"
    if increasing:
        return "The array is increasing and is SAFE"
    elif decreasing:
        return "The array is decreasing and is SAFE"
    else:
        return "The array is neither increasing nor decreasing and is UNSAFE"
    
def checkIfSafe(reports):
    safeReports = 0
    for report in reports:
        isSafe = True
        split_report = splitItem(report)
        # check if next item is within 3 of the current item
        for i in range(1, len(split_report)):
            maxLow, maxHigh = findMaxDifference(split_report[i-1])
            if split_report[i] < maxLow or split_report[i] > maxHigh:
                isSafe = False
                # print(f"Report {report} is UNSAFE due to value out of range")
                break
        # check if array is always increasing or decreasing
        if checkIfIncreasingOrDecreasing(split_report) == "The array is neither increasing nor decreasing and is UNSAFE":
            isSafe = False
            # print(f"Report {report} is UNSAFE due to not being strictly increasing or decreasing")
        
        if isSafe:
            safeReports += 1
            # print(f"Report {report} is SAFE, adding 1 to safeReports")
    
    return f"There are {safeReports} safe reports"
    

levelReports = readFile()
print(checkIfSafe(levelReports))