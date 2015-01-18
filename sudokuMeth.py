#from numpy import array

SUBSQUARE = 2

    

#################################################
# Finds least z with the least number of        #
# possibilities.                                #
#################################################

def get_minimal(possiDict, bigPoss):
    small_one = True
    bigPoss += 1
    iterator = sorted((possiDict.keys()))
    for z in iterator:
        if possiDict[z] is not True:
            if len(possiDict[z]) < bigPoss:
                bigPoss = len(possiDict[z])
                small_one = z
                if bigPoss == 0:
                    small_one = False
                    break
    return small_one
    

test = {1: [2, 3, 4], 2: True, 3: [4, 5, 6]}

print(test, get_minimal(test, 5)) 



