#List Reserve
QList = [12,34,64,21,3]
RList = []


length = len(QList)-1

while length > -1:
    RList.append(QList[length])
    length = length - 1


print(RList)