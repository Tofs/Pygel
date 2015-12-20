import sys

def isNotComment(element):
    return not element.startswith('%')




def loadTMF(filePath):
    file = open(filePath)

    fileContent = file.readlines()
    fileContent = filter(isNotComment, fileContent)

    filterContent = []
    for line in fileContent :
        filterContent.append(line.strip())

    #triangels
    while len(filterContent) > 0 and filterContent[-1]!="#":
        filterContent.pop()

    filterContent.pop()

    #vertex colors
    while len(filterContent) > 0 and filterContent[-1]!="#":
        filterContent.pop()

    #vertex pos




if __name__ == "__main__":
    loadTMF("testData.tmf")
