from itertools import repeat
from pprint import pprint #for testing only

################################################################################
# Solution States:                                                             #
#                                                                              #
#   * True: Already filled.                                                    #
#   * Set Object: Possible Solutions.                                          #
#                                                                              #
################################################################################


class sudoku:
    def initgen(self):
        for activeAddress in self.puzzle:
            activeValue = self.puzzle[activeAddress]
            self.solutions[activeAddress] = True
            for activeSquare in self.rangeGet(activeAddress):
                try:
                    self.solutions[activeSquare].remove(activeValue)
                except KeyError:
                    pass


    #ONLY MODIFY SOLUTIONS IF COPYING
    def __init__(self, initialState, subsquare = 3):
        highnum = subsquare ** 2 + 1
        possol = range(1, highnum)
        self.defaultRange = [(x, y) for x in possol for y in possol]
        self.solutions = {x: set(possol) for x in self.defaultRange}
        self.puzzle = initialState
        self.subsquare = subsquare
        self.initgen()

        pprint(self.solutions)
        pprint(self.puzzle)

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
        squareRange = []
        for i in range(2):
            squareRange.append((address[i] - 1)//self.subsquare + 1)
        line = address[0]
        lRange = list(zip(list(range(1, line)) +\
                list(range(line + 1, self.subsquare ** 2 + 1)), repeat(line)))
        line = address[1]
        lRange += list(zip(repeat(line), list(range(1, line)) +\
                list(range(line + 1, self.subsquare ** 2 + 1))))
        lRange += [(squareRange[0] + a, squareRange[1] + b)\
                for a in range(self.subsquare)\
                for b in range(self.subsquare)]
        lRange = list(set(lRange) - {address})
        return lRange


    def getPoss(self, z):
        pass


       #make length, make [] address 
    




sudoku({(1,1):4})
