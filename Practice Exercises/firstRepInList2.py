# Second version of the exercise 'firstRepInList', which works for numbers
# repeated more than two times.
def firstRep(numList):
    # Define counters
    c1 = 0
    c2 = 0
    # Variables used to compare the index for each of the two iterations done.
    indRep = 0
    guardRep = None
    for i in numList:
        c2 = c1
        c1 = c1 + 1
        for j in numList[c2+1:]:
            c2 = c2 + 1
            if j == i:
                indRep = c2
                if guardRep == None or guardRep > indRep:
                    guardRep = indRep
                # Exit the second iterator as soon as the first repetition is
                # found.
                break
    # Return the first repeated number's index.
    return guardRep

list = [1,2,5,6,1,6,1,2,3,6,7]
repNumInd = firstRep(list)
if repNumInd == 'None':
    print('There are no repeated numbers in the list',list)
else:
    print('First repeated number:',list[repNumInd])
