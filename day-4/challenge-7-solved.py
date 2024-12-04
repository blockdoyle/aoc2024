import re

def readFile(file):
    with open(file, 'r') as f:
        return f.read()
    
def splitLines(content):
    return content.splitlines()

def findOccurrences(lines, pattern):
    occurrnces = [] 
    for line in lines:
        occurrnces.extend(re.findall(pattern, line))
        occurrnces.extend(re.findall(pattern, line[::-1]))
    return occurrnces
    
def transposeLines(lines):
    return [''.join(row) for row in zip(*lines)]

def getDiagonals(lines):
    diagonals = []
    height = len(lines)
    width = len(lines[0])

    # Get diagonals from top-left to bottom-right
    for diag in range(height + width - 1):
        diagonal = []
        for i in range(max(diag - height + 1, 0 ), min(diag + 1, width)):
            diagonal.append(lines[diag - i][i])
        diagonals.append(''.join(diagonal))

    # Get diagonalds from top-right to bottom-left
    for diag in range(height + width -1 ):
        diagonal = []
        for i in range(max(diag - height + 1, 0), min (diag + 1, width)):
            diagonal.append(lines[diag - i][width - i - 1])
        diagonals.append(''.join(diagonal))

    return diagonals

xmasString = readFile("day-4-input.txt")
lines = splitLines(xmasString)

# Find horizontal occurrences
horizontalOccurrences = findOccurrences(lines, r'XMAS')
print(f"Horizontal Occurrences: {len(horizontalOccurrences)}")

# Transpose lines to find vertical occurrences
transposedLines = transposeLines(lines)
verticalOccurrences = findOccurrences(transposedLines, r'XMAS')
print(f"vertical Occurrences: {len(horizontalOccurrences)}")


# Get diagonals to find diagonal occurrences
diagonals = getDiagonals(lines)
diagonalOccurrences = findOccurrences(diagonals, r'XMAS')
print(f"diagonal Occurrences: {len(horizontalOccurrences)}")


# Sum all occurrences
sumOccurrences = horizontalOccurrences + verticalOccurrences + diagonalOccurrences
print(f"Total occurrrences of \"XMAS\": {len(sumOccurrences)}")
# print(sumOccurrences)