from numpy import array

SUBSQUARE = 2

#################################################
# Finds least z with the least number of        #
# possibilities.                                #
#################################################

def get_minimal(possiDict, bigPoss):
    small_one = True
    bigPoss += 1
    for z in possiDict:
        if possiDict[z] is not True:
            if len(possiDict) < bigPoss:
                bigPoss = len(possiDict)
                small_one = z
                if bigPoss == 0:
                    small_one = False
                    break
    return small_one
    

    




