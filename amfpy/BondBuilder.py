from .Builder2D import *


class BondBuilder:
    def __init__(self):
        self.drawer = Drawer()

    def singleBond(self, atomlist: list, bondlist: list):
        self.drawer.plotBond(
           [float(atomlist[int(bondlist[-1][3]) - 1][3]), float(atomlist[int(bondlist[-1][4]) - 1][3])],
           [float(atomlist[int(bondlist[-1][3]) - 1][4]), float(atomlist[int(bondlist[-1][4]) - 1][4])])

    def doubleBond(self, atomlist: list, bondlist: list):
        result = m.atan(
            ((float(atomlist[int(bondlist[-1][4]) - 1][3])) - (float(atomlist[int(bondlist[-1][3]) - 1][3]))) / (
                    (float(atomlist[int(bondlist[-1][4]) - 1][4])) - (float(atomlist[int(bondlist[-1][3]) - 1][4]))))
        distance = 0.1
        self.drawer.plotBond([float(atomlist[int(bondlist[-1][3]) - 1][3]) + (distance * m.cos(result)),
                              float(atomlist[int(bondlist[-1][4]) - 1][3]) + (distance * m.cos(result))],
                             [float(atomlist[int(bondlist[-1][3]) - 1][4]) + (distance * m.sin(result + (45 * m.pi))),
                              float(atomlist[int(bondlist[-1][4]) - 1][4]) + (distance * m.sin(result + (45 * m.pi)))])

        self.drawer.plotBond([float(atomlist[int(bondlist[-1][3]) - 1][3]) + (distance * m.cos(result + (45 * m.pi))),
                              float(atomlist[int(bondlist[-1][4]) - 1][3]) + (distance * m.cos(result + (45 * m.pi)))],
                             [float(atomlist[int(bondlist[-1][3]) - 1][4]) + (distance * m.sin(result)),
                              float(atomlist[int(bondlist[-1][4]) - 1][4]) + (distance * m.sin(result))])

    def tripleBond(self, atomlist: list, bondlist: list):
        result = m.atan(
            ((float(atomlist[int(bondlist[-1][4]) - 1][3])) - (float(atomlist[int(bondlist[-1][3]) - 1][3]))) / (
                    (float(atomlist[int(bondlist[-1][4]) - 1][4])) - (float(atomlist[int(bondlist[-1][3]) - 1][4]))))
        distance = 0.15
        self.drawer.plotBond(
            [float(atomlist[int(bondlist[-1][3]) - 1][3]), float(atomlist[int(bondlist[-1][4]) - 1][3])],
            [float(atomlist[int(bondlist[-1][3]) - 1][4]), float(atomlist[int(bondlist[-1][4]) - 1][4])])
        self.drawer.plotBond([float(atomlist[int(bondlist[-1][3]) - 1][3]) + (distance * m.cos(result)),
                              float(atomlist[int(bondlist[-1][4]) - 1][3]) + (distance * m.cos(result))],
                             [float(atomlist[int(bondlist[-1][3]) - 1][4]) + (distance * m.sin(result + (45 * m.pi))),
                              float(atomlist[int(bondlist[-1][4]) - 1][4]) + (distance * m.sin(result + (45 * m.pi)))])

        self.drawer.plotBond([float(atomlist[int(bondlist[-1][3]) - 1][3]) + (distance * m.cos(result + (45 * m.pi))),
                              float(atomlist[int(bondlist[-1][4]) - 1][3]) + (distance * m.cos(result + (45 * m.pi)))],
                             [float(atomlist[int(bondlist[-1][3]) - 1][4]) + (distance * m.sin(result)),
                              float(atomlist[int(bondlist[-1][4]) - 1][4]) + (distance * m.sin(result))])
