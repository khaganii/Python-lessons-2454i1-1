def find_largest_element(myList):
    maxi = -1
    for el in myList:
        if el > maxi:
            maxi = el
    return maxi

aList = [2,5,1,2,7,3,10,6,8]
print("max element = ", find_largest_element(aList))