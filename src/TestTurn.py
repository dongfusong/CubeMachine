class Face:
    def __init__(self, color):
        self.content = [[]]
        self.neighbors = {'up':Face(),'right':Face(),'down':Face(),'left':Face()}

        for i in range(3):
            row = [color, color, color]
            self.content.append(row)

        self.getLines = {'left':self.__getLeftLine, 'right':self.__getRightLine,
            'up':self.__getUpLine, 'down': self.__getDownLine}

        self.setLines = {'left':self.__setLeftLine, 'right':self.__setRightLine,
            'up':self.__setUpLine, 'down': self.__setDownLine}

    def __getUpLine(self):
        return self.content[0]

    def __setUpLine(self, line):
        self.content[0] = line

    def __getDownLine(self):
        return self.content[2]

    def __setDownLine(self, line):
        self.content[2] = line

    def __getLeftLine(self):
        return [self.content[0][0], self.content[1][0], self.content[2][0]]

    def __setLeftLine(self, line):
        self.content[0][0] = line[0]
        self.content[1][0] = line[1]
        self.content[2][0] = line[2]

    def __getRightLine(self):
        return [self.content[0][2], self.content[1][2], self.content[2][2]]

    def __setRightLine(self, line):
        self.content[0][2] = line[0]
        self.content[1][2] = line[1]
        self.content[2][2] = line[2]


    def __getDirect(self,neighbor):
        for keyItem in self.neighbors.keys():
            if (self.neighbors[keyItem] == neighbor):
                return keyItem

    def setLine(self, neighbor, line):
        (self.setLines[self.__getDirect(neighbor)])(line)

    def getLine(self, neighbor):
        return (self.getLines[self.__getDirect(neighbor)])()

    def setNeighborFace(self, type, face):
        self.neighbors[type] = face

    def geNeighborLine(self, neighborFace):
        return neighborFace.getLine(self)

    def setNeighborLine(self, neighborFace, line):
        return neighborFace.setLine(self, line)

    def turnClockWise(self):
        leftLine = self.neighbors['left'].geNeighborLine(self)
        upLine = self.neighbors['up'].geNeighborLine(self)
        rightLine = self.neighbors['right'].geNeighborLine(self)
        downLine = self.neighbors['down'].geNeighborLine(self)

        self.neighbors['up'].setNeighborLine(self, leftLine)
        self.neighbors['right'].setNeighborLine(self, upLine)
        self.neighbors['down'].setNeighborLine(self, rightLine)
        self.neighbors['left'].setNeighborLine(self, downLine)

import unittest

class CubeMachine:
    def turnOn(self, cmd):
        try:
            self.commands[cmd]
        except:
            return

    # 设置各个面之间的关系
    def setRelation(self):
        pass

    def __init__(self):
        self.wFace = Face('w')
        self.yFace = Face('y')
        self.rFace = Face('r')
        self.oFace = Face('o')
        self.gFace = Face('g')
        self.bFace = Face('b')
        self.commands = {'U':self.wFace.turnClockWise,
                        'D':self.yFace.turnClockWise,
                        'F':self.rFace.turnClockWise,
                        'B':self.oFace.turnClockWise,
                        'L':self.gFace.turnClockWise,
                        'R':self.bFace.turnClockWise
                        }


class Test(unittest.TestCase):
    # 是遏制各个面的关系
    def setRelation(self):
        pass

    def setUp(self):
        self.machine = CubeMachine()
        self.machine.setRelation()

    def testTurnOn(self, cmd):
        self.machine.turnOn(cmd)
