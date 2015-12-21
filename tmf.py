import sys
from collections import deque

def isNotComment(element):
    return not element.startswith('%')

def load(filePath):
    file = open(filePath)

    fileContent = file.readlines()
    fileContent = filter(isNotComment, fileContent)

    filterContent = deque([])
    for line in fileContent :
        filterContent.append(line.strip())

    triangels = []
    vertexPositions = []
    vertexColors = []

    #vertex pos
    while len(filterContent) > 0 and filterContent[0]!="#":
        line = filterContent.popleft().split(" ")
        floatsInLine = [float(x) for x in line]
        floatsInLine.append(1.0)
        vertexPositions += floatsInLine

    filterContent.popleft()
    #vertex colors
    while len(filterContent) > 0 and filterContent[0]!="#":
        line = filterContent.popleft().split(" ")
        floatsInLine = [float(x) for x in line]
        floatsInLine.append(1.0)
        vertexColors += floatsInLine

    filterContent.popleft()
    #triangels
    while len(filterContent) > 0 and filterContent[0]!="#":
        line = filterContent.popleft().split(" ")
        intsInLine = [int(x) for x in line]
        triangels += intsInLine

    return vertexPositions, vertexColors, triangels

if __name__ == "__main__":
    print load("testData.tmf")
