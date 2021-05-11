
def createRoadsFromFile(filename):
    try:
        file = open(filename)
    except FileNotFoundError:
        print("nothing")
        return
    result = {}
    for line in file:
        start, end, length = line.split(",")
        miles = int(length)
        result[(str(start.strip()),str(end.strip()))] = miles
    file.close()
    #print(result)
    return result