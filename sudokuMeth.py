from itertools import repeat
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
        try:
            length = len(self.solutions[z])
        except: 
            length = None
        if self.solutions[z] is None:
            return False
        elif contents in self.solutions[z]:
            self.puzzle[z] = contents
            return True
        else:
            return False
        PowRange = self.rangeGet(z)
        self.gen(PowRange)

            

    def copy(self):
        return sudoku(self.TupleDict.copy(), solutions = self.solutions.copy())

    def rangeGet(self, address):
        A = []
        for i in range(2):
            A += (address[i] - 1)//SUBSQUARE + 1
        lRange = zip(range(1, a) + range(a + 1, n + 1), repeat(a))
        lRange += zip(repeat(a), range(1, a) + range(a + 1, n + 1))
        lRange += [(A[0] + a, A[1] + b) for a in range(SUBSQUARE) for b in range(SUBSQUARE)]
        lRange = list(set(lRange) - {address})
        return lRange


    def get(self, z):
        pass


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



