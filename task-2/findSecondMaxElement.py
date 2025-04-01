def find_nth_largest_element(n,myList):
    myList = sortMyList(myList)
    print(myList)
    if n > len(myList) or n < 0:
        return None
    return myList[n-1]

def sortMyList(bList):
    for i in range(0, len(bList)-1):
        for j in range(i+1, len(bList)):
            if bList[i] > bList[j]:
                t = bList[i]
                bList[i] = bList[j]
                bList[j] = t
    return bList


aList = [2,5,1,2,7,3,10,6,8]
print("max element = ", find_nth_largest_element(4,aList))