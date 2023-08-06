import matplotlib.pyplot as plt
import math as m
import amfpy


def singleBond():
    plt.plot(
        [float(atomList[int(bondList[-1][3]) - 1][3]), float(atomList[int(bondList[-1][4]) - 1][3])],
        [float(atomList[int(bondList[-1][3]) - 1][4]), float(atomList[int(bondList[-1][4]) - 1][4])],
        color='dimgrey', zorder=1, linewidth=2)


def doubleBond():
    # TODO: add double bonding element; arctan() from MolecularModeller
    # float result = (
    #     Mathf.Atan((mousePos.x - startAtom.transform.position.x) / ((mousePos.y - startAtom.transform.position.y))));
    #
    # line1.SetPosition(0, startAtom.transform.position + new
    # Vector3(distance * Mathf.Cos(result), distance * Mathf.Sin(result + (45 * Mathf.PI)), 1
    # f));
    # line2.SetPosition(0, startAtom.transform.position + new
    # Vector3(distance * Mathf.Cos(result + (45 * Mathf.PI)), distance * Mathf.Sin(result), 1
    # f));

    result = m.atan(
        ((float(atomList[int(bondList[-1][4]) - 1][3])) - (float(atomList[int(bondList[-1][3]) - 1][3]))) / (
                (float(atomList[int(bondList[-1][4]) - 1][4])) - (float(atomList[int(bondList[-1][3]) - 1][4]))))
    # print(result)
    distance = 0.1
    plt.plot([float(atomList[int(bondList[-1][3]) - 1][3]) + (distance * m.cos(result)),
              float(atomList[int(bondList[-1][4]) - 1][3]) + (distance * m.cos(result))],
             [float(atomList[int(bondList[-1][3]) - 1][4]) + (distance * m.sin(result + (45 * m.pi))),
              float(atomList[int(bondList[-1][4]) - 1][4]) + (distance * m.sin(result + (45 * m.pi)))], zorder=1,
             color='dimgrey', linewidth=2)

    plt.plot([float(atomList[int(bondList[-1][3]) - 1][3]) + (distance * m.cos(result + (45 * m.pi))),
              float(atomList[int(bondList[-1][4]) - 1][3]) + (distance * m.cos(result + (45 * m.pi)))],
             [float(atomList[int(bondList[-1][3]) - 1][4]) + (distance * m.sin(result)),
              float(atomList[int(bondList[-1][4]) - 1][4]) + (distance * m.sin(result))], color='dimgrey',
             zorder=1,
             linewidth=2)


def tripleBond():
    pass


class Origin:
    def __init__(self, oriname):
        self.name = oriname
        self.cList = {}

    def add(self, args: list):
        # print("Key: " + args.copy()[0])
        self.cList[args.copy()[0]] = args.copy()

    def buildOriginPrefab(self, id, coords):
        global atomList, bondList
        x, y, z = coords
        for atom in self.cList[id][1:]:
            if len(atom) > 1:
                if atom.split()[0] == "ATOM":
                    if atom.split()[2] == '8':
                        oricolor = 'red'
                    elif atom.split()[2] == '1':
                        oricolor = 'whitesmoke'
                    elif atom.split()[2] == '7':
                        oricolor = "limegreen"
                    else:
                        oricolor = 'blue'
                    atomList.append(["ATOM", atom.split()[1], atom.split()[2], str(float(atom.split()[3]) + float(x)),
                                     str(float(atom.split()[4]) + float(y))])
                    plt.plot(float(atom.split()[3]) + float(x), float(atom.split()[4]) + float(y),
                             marker="o", color=oricolor)

                elif atom.split()[0] == "BND":
                    bondList.append(atom.split())

                    if bondList[-1][2] == "1":

                        # print("X1: ", x1, ", X2: ", x2, ", Y1: ", y1, ", Y2: ", y2)
                        # print(atomList[len(bondList) - 1])
                        singleBond()
                    elif bondList[-1][2] == "2":
                        print("DOUBLE BOND")
                        doubleBond()
                    elif bondList[-1][2] == "3":
                        tripleBond()
                    else:
                        # TODO: Add bond type: single, double, triple, quadruple, or aromatic

                        plt.plot(
                            [float(atomList[int(bondList[-1][3]) - 1][3]),
                             float(atomList[int(bondList[-1][4]) - 1][3])],
                            [float(atomList[int(bondList[-1][3]) - 1][4]),
                             float(atomList[int(bondList[-1][4]) - 1][4])],
                            color='g', zorder=2, linewidth=2)

                else:
                    break
        atomList = []
        bondList = []


##########################################################################


MOLECULE = "alanine.amf"

amfpy.Reader(MOLECULE)

plt.show()
