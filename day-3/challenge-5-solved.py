import re

def readFile(filename):
    with open(filename, 'r') as file:
        return file.read()
    
def findPatterns(importString):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return re.findall(pattern, importString)

def multiply(a,b):
    return a * b

def createProductsArray(multiples):
    products = []
    for a,b in multiples:
        products.append((int(a), int(b)))
    return products

def getProduct(multiples):
    results = []
    for a,b in multiples:
        result = multiply(int(a), int(b))
        results.append(result)
    return results

def getSumOfProducts(productsArray):
    sumTotal = 0
    for product in productsArray:
        sumTotal += product
    return sumTotal

    
content = readFile("day-3-input.txt")
multiples = findPatterns(content)
products = createProductsArray(multiples)
productsResult = getProduct(products)
# print(productsResult)
total = getSumOfProducts(productsResult)
print(f"The sum of products is: {total}")