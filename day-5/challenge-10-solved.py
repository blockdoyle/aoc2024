# Get file contents
def readFile(filename):
    with open(filename, 'r') as file:
        data = [line.strip() for line in file.readlines()]
    return (data)

# Split item by pipe
def splitPipe(content):
    return content.split("|")

# Parse the rules
def parseRules(rules):
    parsedRules = []
    for rule in rules:
        left, right = map(int, splitPipe(rule))
        parsedRules.append((left, right))
    return parsedRules

# Parse the sets
def parseSets(sets):
    parsedSets = []
    for setStr in sets:
        parsedSets.append(list(map(int, setStr.split(','))))
    return parsedSets

# Create rule dictionary
def createRuleDict(rules):
    ruleDict = {}
    for left,right in rules:
        if left not in ruleDict:
            ruleDict[left] = []
        ruleDict[left].append(right)
    return ruleDict

# Check if array follows the rules
def followsRules(array, ruleDict):
    for left in ruleDict:
        for right in ruleDict[left]:
            if left in array and right in array:
                if array.index(left) > array.index(right):
                    return False
    return True

# Find all sets that follow the rules defined in ruleDictionary
def findCorrectSets(setsArray):
    correct = []
    incorrect = []
    for set in setsArray:
        if followsRules(set, ruleDictionary):
            correct.append(set)
        else:
            incorrect.append(set)
    return correct,incorrect

# Find middle integer of array and return it
def getMiddleInteger(array):
    return len(array) // 2

# Make list of middle integers
def createMiddleIndexList(sets):
    middleIntegers = []
    for set in sets:
        middleIntegers.append(getMiddleInteger(set))
    return middleIntegers

# Get sum of middle integers
def getSum(array):
    print(array)
    sum = 0
    for i in array:
        sum += i
        # print(sum)
    return sum

# Main
pageRules = readFile("day-5-input.txt")
pageSets = readFile("day-5-input-2.txt")
rules = parseRules(pageRules)
parsedSets = parseSets(pageSets)
ruleDictionary = createRuleDict(rules)
correctSets,incorrectSets = findCorrectSets(parsedSets)
print(f"There are {len(correctSets)} correct sets")
middleIntegerArray = createMiddleIndexList(correctSets)
total = getSum(middleIntegerArray)
print(f"Sum of middle integers: {total}")

# testDict = {
#     1: [2],
#     2: [3, 4],
#     97: [1,2,3,4],
# }

# testArray = [97,1,2,3,4]
# print(followsRules(testArray, testDict))

# print(f"There are {len(correctSets)} correct sets")
# print(getMiddleInteger(testArray))
