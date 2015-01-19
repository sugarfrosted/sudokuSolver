from itertools import repeat

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


    def getPoss(self, z):
        pass


       #make length, make [] address 
    

#################################################
# Finds least z with the least number of        #
# possibilities.                                #
#################################################




