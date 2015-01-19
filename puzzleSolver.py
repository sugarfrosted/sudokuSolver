#################################################
# Finds least z with the least number of        #
# possibilities.                                #
#################################################


def get_minimal(possiDict, bigPoss): #implement puzzle class support or drop
    small_one = True
    bigPoss += 1
    iterator = sorted(possiDict.solutions.keys())
    for z in iterator:
        if possiDict[z] is not True:
            if len(possiDict[z]) < bigPoss:
                bigPoss = len(possiDict.solutions[z])
                small_one = z
                if bigPoss == 0:
                    small_one = False
                    break
    return small_one
    


def worker(puzzle):
    BIGGEST_POSITION = puzzle.subsquare ** 2 + 1
    smallest = get_minimal(puzzle, BIGGEST_POSITION) #questionable
    if smallest is False:
        return False
    elif smallest is True:
        puzzle.out()
    else:
        choices = puzzle.solutions[smallest]
        for option in choices:
            passpuzzle = puzzle.copy()
            passpuzzle.add(z, puzzle.get(z))
            worker(passpuzzle)
