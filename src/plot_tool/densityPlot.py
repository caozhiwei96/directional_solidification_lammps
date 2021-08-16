# rho-t plot

import matplotlib.pyplot as plt
import numpy as np
import os


def densityPlot(path, alloyType, numAtom, denStd,
                equStepNum, equThermoNum, equTimeStep,
                solStepNum, solThermoNum, solTimeStep):

    if not os.path.exists(str(path) + '/plot'):
        os.makedirs(str(path) + '/plot')

    # Slice
    data = np.loadtxt(str(path) + '/output/density.txt')

    step = data[:, 0]
    rho = data[:, 1]

    equStep = step[0:(int(equStepNum / equThermoNum))]
    solStep = step[int(equStepNum / equThermoNum):] - equStepNum

    equTime = equStep * equTimeStep
    solTime = solStep * solTimeStep + equStepNum * equTimeStep

    X = np.append(equTime, solTime)
    Y = np.array(rho)

    # Plot
    plt.rc('font', size=14)
    plt.plot(X, Y, linewidth=1.5)

    plt.xlabel("Time / ps")
    plt.ylabel("Density / $g \cdot cm^{-3}$")
    # plt.title("Density Change of " + str(alloyType))

    plt.xlim(0, X[-1])

    plt.axvline(x=equTime[-1], ls="--", c="black", linewidth=1.5)
    plt.annotate('Directional Solidification\nstarting at 30 ps',
                 xy=(equTime[-1], 2.1), xytext=(equTime[-1] + 100, 2.1),
                 arrowprops=dict(facecolor='black', arrowstyle='->'),
                 )

    # Theoretical Density
    if denStd != 0:  # set as 0 if not needed
        plt.axhline(y=denStd, ls="-", c="green", linewidth=1.5)
        plt.annotate('Theoretical Density', xy=(700, denStd - 0.03), c="green")

    plt.savefig(str(path) + '/plot/rho-t.png')

    plt.show()
