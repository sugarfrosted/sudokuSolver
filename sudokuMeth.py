#from numpy import array

SUBSQUARE = 2

class sudoku:
    def gen(self, TupeRange = POSS):
        pass

    #ONLY MODIFY SOLUTIONS IF COPYING
    def __init__(self, TupleDict, solutions = None):
        self.puzzle = TupleDict
        if solutions is None:
            self.solutions = self.gen()

    def add(self, address, contents):
        pass

    def copy(self):
        return sudoku(self.TupleDict.copy(), solutions = self.solutions.copy())

    def get(self, z):
        pass

    def keys(self):
        return self.solutions()

       #make length, make [] address 
    

#################################################
# Finds least z with the least number of        #
# possibilities.                                #
#################################################

def get_minimal(possiDict, bigPoss):
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
    

test = {1: [1,2,3], 2: [], 3: True}

print(test, get_minimal(test, 5)) 


def worker(puzzle):
    smallest = get_minimal(puzzle, BIGGEST_POSITION) #questionable
    if smallest is False:
        return False
    elif smallest is True:
        puzzle.out()
    else:
        choices = puzzle[smallest]
        for option in choices:
            passpuzzle = puzzle.copy()
            passpuzzle.append(z, puzzle.get(z))
            worker(passpuzzle)



