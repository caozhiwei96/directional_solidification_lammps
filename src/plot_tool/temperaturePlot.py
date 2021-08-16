# rho-t plot

import matplotlib.pyplot as plt
import numpy as np
import os


def temperaturePlot(path, alloyType, numAtom, denStd,
                    equStepNum, equThermoNum, equTimeStep,
                    solStepNum, solThermoNum, solTimeStep):

    if not os.path.exists(str(path) + '/plot'):
        os.makedirs(str(path) + '/plot')

    temp_matrix = np.loadtxt(str(path) + '/output/temperature.txt')
    time = (temp_matrix[:, 0] - equStepNum) * solTimeStep
    temp_stable = temp_matrix[-1, 1:]

    # Plot
    plt.rc('font', size=14)

    plt.figure()
    plt.plot(time, temp_matrix[:, 1], linewidth=1.5, label='x = 0-3 nm')
    plt.plot(time, temp_matrix[:, 2], linewidth=1.5, label='x = 3-12 nm')
    plt.plot(time, temp_matrix[:, 3], linewidth=1.5, label='x = 12-18 nm')
    plt.plot(time, temp_matrix[:, 4], linewidth=1.5, label='x = 18-27 nm')
    plt.plot(time, temp_matrix[:, 5], linewidth=1.5, label='x = 27-30 nm')

    plt.xlabel("Time / ps")
    plt.ylabel("Temperature / K")
    # plt.title("Temperature Change of " + str(alloyType) + " during Solidification")
    plt.legend()
    plt.minorticks_on()
    plt.xlim(0, time[-1])
    plt.savefig(str(path) + '/plot/T-t.png', bbox_inches='tight')

    plt.figure()
    plt.plot([1.5, 7.5, 15, 22.5, 28.5], temp_stable, linewidth=1.5, marker='o')
    plt.xlim([0, 30])
    plt.minorticks_on()
    plt.grid()
    plt.xlabel("x / nm")
    plt.ylabel("Temperature / K")
    # plt.title("Temperature Plot of " + str(alloyType))
    plt.savefig(str(path) + '/plot/T-x.png', bbox_inches='tight')

    plt.show()
