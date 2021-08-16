from ovito.io import *
from ovito.modifiers import *
from ovito.pipeline import *
import numpy as np
import matplotlib.pyplot as plt
import os


def compositionPlot(path, alloyType, numAtom, solStepNum, solTimeStep):

    if not os.path.exists(str(path) + '/plot'):
        os.makedirs(str(path) + '/plot')

    # This part is inspired by liou's post on https://zhuanlan.zhihu.com/p/270368857
    # Load a simulation trajectory consisting of several frames:
    pipeline = import_file(str(path) + '/output/dump.DS')
    # Insert the modifier into the pipeline:
    modifier = CommonNeighborAnalysisModifier()
    pipeline.modifiers.append(modifier)

    # Initialize array.
    CNA = np.zeros((1, 4))

    total_frames = pipeline.source.num_frames
    time = np.multiply(range(total_frames), 10)

    # Iterate over all frames of the sequence.
    for frame in range(total_frames):
        # Evaluate pipeline to let the modifier compute the RDF of the current frame:
        data = pipeline.compute(frame)
        n_temp = [(data.attributes['CommonNeighborAnalysis.counts.FCC'],
                   data.attributes['CommonNeighborAnalysis.counts.BCC'],
                   data.attributes['CommonNeighborAnalysis.counts.HCP'],
                   data.attributes['CommonNeighborAnalysis.counts.OTHER'])]
        CNA = np.append(CNA, n_temp, axis=0)

        # Progress indicator
        print(str(frame+1)+'/'+str(total_frames))

    # Export the CNA results to a text file:
    CNA = np.delete(CNA, 0, axis=0)  # To delete the initial zero array created by numpy.zeros

    np.savetxt(str(path) + "/output/CNA.txt", CNA)

    FCCratio = CNA[:, 0] / numAtom
    BCCratio = CNA[:, 1] / numAtom
    HCPratio = CNA[:, 2] / numAtom
    OTHratio = CNA[:, 3] / numAtom

    # Plot
    plt.rc('font', size=14)

    plt.plot(time, FCCratio, linewidth=1.5, label='FCC', color='green')
    plt.plot(time, HCPratio, linewidth=1.5, label='HCP', color='red')
    plt.plot(time, BCCratio, linewidth=1.5, label='BCC', color='blue')
    plt.plot(time, OTHratio, linewidth=1.5, label='OTHER', color='black')

    plt.xlabel("Time / ps")
    plt.ylabel("Ratio")
    # plt.title("Composition Ratio Change of " + str(alloyType) + " during Solidification")
    plt.legend()

    plt.xlim(0, time[-1])
    plt.ylim(0.0, 1.0)

    plt.savefig(str(path) + '/plot/ratio-t.png', bbox_inches='tight')

    plt.show()
