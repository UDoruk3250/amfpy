import matplotlib.pyplot as plt
from OriginBuilder import *
class Reader:
    MOLECULE = ""

    def __init__(self, MOLECULE):
        self.MOLECULE = MOLECULE

    commandList = []
    atomList = []
    condition = False
    bondList = []
    plt.axes().set_facecolor("black")
    with open(MOLECULE, "r") as f:
        # filelist = [(lambda x: [a.replace("\n", "") for a in x])(f.readlines()[len(commandList):].copy())]
        for line in f:
            if len(line) > 1:
                commandList.append(line.split())
                if commandList[-1][0] == "END":
                    break
                if commandList[-1][0] == "ORI":
                    builder = Origin("".join(commandList[-1][1:]))
                    file = open(MOLECULE, "r")
                    # asd = (lambda x: [a.replace("\n", "") for a in x])(f.readlines()[len(commandList):].copy())
                    builder.add(
                        (lambda x: [a.replace("\n", "") for a in x])(file.readlines()[len(commandList):].copy()))
                if commandList[-1][0] == "STT":
                    condition = True
                if condition:
                    if commandList[-1][0] == "ATOM":
                        atomList.append(line.split())
                        print(atomList[-1][2])
                        if atomList[-1][2] == '8':
                            color = 'red'
                        elif atomList[-1][2] == '1':
                            color = 'whitesmoke'
                        elif atomList[-1][2] == '7':
                            color = 'limegreen'
                        else:
                            color = 'blue'
                        plt.plot(int(commandList[-1][3]), int(commandList[-1][4]),
                                 marker="o", color=color)
                    elif commandList[-1][0] == "INS":
                        builder.buildOriginPrefab("ORI " + commandList[-1][1], commandList[-1][2:])
                    elif commandList[-1][0] == "BND":
                        bondList.append(line.split())
                        plt.plot(
                            [float(atomList[int(bondList[-1][2]) - 1][3]),
                             float(atomList[int(bondList[-1][3]) - 1][3])],
                            [float(atomList[int(bondList[-1][2]) - 1][4]),
                             float(atomList[int(bondList[-1][3]) - 1][4])],
                            color='g', linewidth=2)