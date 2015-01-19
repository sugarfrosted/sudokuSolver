from itertools import repeat


class sudoku:
    def gen(self, TupeRange):
        pass

    #ONLY MODIFY SOLUTIONS IF COPYING
    def __init__(self, TupleDict, solutions = None, subsquare = 3):
        self.puzzle = TupleDict
        self.subsquare = subsquare
        if solutions is None:
            self.solutions = self.gen()

    def add(self, address, contents): #checked
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
        return sudoku(deepcopy(self.TupleDict),\
                solutions = deepcopy(self.solutions),\
                subsquare = self.subsquare)

    def rangeGet(self, address):
        A = []
        for i in range(2):
            A += (address[i] - 1)//self.subsquare + 1
        lRange = zip(range(1, a) +\
                range(a + 1, self.subsquare ** 2 + 1), repeat(a))
        lRange += zip(repeat(a), range(1, a) +\
                range(a + 1, self.subsquare ** 2 + 1))
        lRange += [(A[0] + a, A[1] + b)\
                for a in range(subsquare)\
                for b in range(subsquare)]
        lRange = list(set(lRange) - {address})
        return lRange


    def getPoss(self, z):
        pass


       #make length, make [] address 
    





