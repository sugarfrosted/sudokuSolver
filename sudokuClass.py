from itertools import repeat
from pprint import pprint #for testing only
#import pudb; pu.db

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
            self.gen(activeAddress)
            if activeAddress == (5, 3):
                pprint(sorted(self.rangeGet(activeAddress)))


    def gen(self, address):
        self.solutions[address] = True
        value = self.puzzle[address]
        for activeSquare in self.rangeGet(address):
            try:
                self.solutions[activeSquare].remove(value)
            except KeyError:
                pass
            except TypeError:
                pass
            except AttributeError:
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

        #pprint(self.solutions)
        #pprint(self.puzzle)

    def add(self, address, contents): #wtf was I on
        if address in self.defaultRange:
            if address not in self.puzzle:
                self.puzzle[address] = contents
                self.gen(address)
                return True
            else:
                return False
        else:
            return False
            

    def copy(self):
        return sudoku(deepcopy(self.TupleDict),\
                solutions = deepcopy(self.solutions),\
                subsquare = self.subsquare)

    def rangeGet(self, address):
        squareRange = []
        line = address[0]
        lRange = list(zip(list(range(1, self.subsquare ** 2 + 1)), repeat(line)))
        line = address[1]
        lRange += list(zip(repeat(line), list(range(1, self.subsquare ** 2 + 1))))
        lRange += self.squareGet(address)
        lRange = list(set(lRange) - {address})
        return lRange

    def squareGet(self, address):
        UpperLeft = [((address[a] - 1) // self.subsquare) * self.subsquare + 1 for a in range(2)]
        boxArea = [(UpperLeft[0] + a, UpperLeft[1] + b) for a in range(self.subsquare)\
                for b in range(self.subsquare)] 
        return boxArea


    def getPoss(self, z):
        pass

    def outputSolution(self):
        length = self.subspace ** 2
        out = '╔'
        for i in range(length - 1):
            pass

       #make length, make [] address 

    def getFormattedNum(self, address, numlength):
        if address in self.defaultRange:
            if address in self.puzzle:
                number = self.puzzle[address]
                output = '{:' + str(numlength) + 'd}'
                output = output.format(number)
                return output
            elif len(self.solutions[address]) == 0:
                return 'x' * numlength
            else:
                return ' ' * numlength


    def purple(self, row, col):
       numlength = len(str(self.subsquare ** 2))
       if col == 0:
           if row == 0:
               return '╔' + numlength * '═'
           elif row == (self.subsquare ** 2) * 2:
               return '╚' + numlength * '═'
           elif row % 2 == 1:
               return '║a'
           elif row % (2 * self.subsquare) == 0:
               return '╠' + numlength * '═'
           else:
               return '╟' + numlength * '─'
       elif col == (self.subsquare ** 2):
           if row == 0:
               return '╗'
           elif row == (self.subsquare ** 2) * 2:
               return '╝'
           elif row % 2 == 1:
               return '║'
           elif row % (2 * self.subsquare) == 0:
               return '╣'
           else:
               return '╢'
       elif col % self.subsquare == 0: 
           if row == 0:
               return '╦' + numlength * '═'
           elif row == (self.subsquare ** 2) * 2:
               return '╩' + numlength * '═'
           elif row % 2 == 1:
               return '║a'
           elif row % (2 * self.subsquare) == 0:
               return '╬' + numlength * '═'
           else:
               return '╫' + numlength * '─'
       else: 
           if row == 0:
               return '╤' + numlength * '═'
           elif row == (self.subsquare ** 2) * 2:
               return '╧' + numlength * '═'
           elif row % 2 == 1:
               return '│a'
           elif row % (2 * self.subsquare) == 0:
               return '╪' + numlength * '═'
           else:
               return '┼' + numlength * '─'
       
    




test = sudoku({(1, 2):3, (1, 6):9, (1, 9):7,(2, 3):7, (2,4):5, (2, 5):2, (2, 6): 8, (3, 1): 2, (3, 2):5, (3, 3):9,(3, 5):1, (3, 8): 4, (3, 9): 6, (4, 3): 2, (4, 5): 9, (4, 9): 3, (5, 2):4, (5,3): 6, (5, 5): 7, (5, 7):  9, (5, 8): 5, (6, 1) : 9, (6, 5) : 5, (6, 7) : 1, (7, 1) : 1, (7, 2) : 2, (7, 5) : 8, (7, 7) : 7, (7, 8) : 3, (7, 9) : 9, (8, 4) : 1, (8, 5) : 4, (8, 6) : 2, (8, 7) : 6, (9, 1) : 6, (9, 4) : 9, (9, 8) : 1}, subsquare = 3)
#print(test.solutions[(2, 2)])
#test.add((2, 1), 4)
#print(test.solutions[(2, 2)])
#test.add((1, 1), 8)
#print(test.solutions[(2, 2)])
#test.add((1, 3), 1)
hold = ''
for i in range(2 *test.subsquare ** 2 + 1):
    for j in range(test.subsquare ** 2 + 1):
        hold += test.purple(i ,j)
    print(hold)
    hold = ''
    
