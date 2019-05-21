heroes = ["아이언맨","토르","헐크","스칼렛 위치"]

def myindex(sourceList, item):
    sn = len(sourceList)
    for i in range(sn):
        if item == sourceList[i]:
            return i

    return -1

print(myindex(heroes,"헐크"))
