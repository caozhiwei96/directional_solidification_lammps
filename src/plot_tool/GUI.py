from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory
from densityPlot import densityPlot
from compositionPlot import compositionPlot
from temperaturePlot import temperaturePlot
import os

window = Tk()

# Define window
window.title('Plot Tool v1.0')
window.geometry('600x400')


def selectPath():
    path_ = askdirectory(title='Select Directory',
                         initialdir=r'/home/zhiwei/Desktop/lammps-data')  # set default dir
    path.set(path_)


def submitted():  # Submit button
    res = "Input submitted!" \
          "\nPath: " + path.get() + \
          "\nAlloy: " + alloyTypeCombo.get() + \
          "\nAtoms: " + numAtom.get() + \
          "\nDensity: " + denStd.get()
    line2.configure(text=res)


def callDensity():
    densityPlot(path.get(), alloyTypeCombo.get(), int(numAtom.get()), float(denStd.get()),
                int(equStepNum.get()), int(equThermoNum.get()), float(equTimeStep.get()),
                int(solStepNum.get()), int(solThermoNum.get()), float(solTimeStep.get()),
                )


def callComposition():
    compositionPlot(path.get(), alloyTypeCombo.get(), int(numAtom.get()),
                    int(solStepNum.get()), float(solTimeStep.get())
                    )


def callTemperature():
    temperaturePlot(path.get(), alloyTypeCombo.get(), int(numAtom.get()), float(denStd.get()),
                    int(equStepNum.get()), int(equThermoNum.get()), float(equTimeStep.get()),
                    int(solStepNum.get()), int(solThermoNum.get()), float(solTimeStep.get()),
                    )



# TEXT
line1 = Label(window, text="Input for post processing")
line1.place(x=10, y=0)

# ENTRY
# Path
pathLabel = Label(window, text="Path: ")
pathLabel.place(x=10, y=30)
# path = StringVar(value='/home/')  # default value of path
path = StringVar()
pathEntry = Entry(window, width=50, textvariable=path)
pathEntry.place(x=50, y=30)
pathBtn = Button(window, text='Select', command=selectPath, width=8)
pathBtn.place(x=460, y=30)

# Alloy type
alloyTypeLabel = Label(window, text="Alloy: ")
alloyTypeLabel.place(x=10, y=60)
alloyTypeCombo = ttk.Combobox(window, width=15)
alloyTypeCombo['values'] = ('Al', 'SS304L', 'Al10SiMg')
alloyTypeCombo.current(1)
alloyTypeCombo.place(x=50, y=60)
# Number of Atoms
numAtomLabel = Label(window, text="Num of Atoms: ")
numAtomLabel.place(x=200, y=60)
numAtom = StringVar(value=2370816)  # default value of atom number
numAtomEntry = Entry(window, width=10, textvariable=numAtom)
numAtomEntry.place(x=300, y=60)
# Theoretical Density
denStdLabel = Label(window, text="Density: ")
denStdLabel.place(x=400, y=60)
denStd = StringVar(value=0)  # default value of density, 0 for not adding
denStdEntry = Entry(window, width=10, textvariable=denStd)
denStdEntry.place(x=460, y=60)

# Table
tableLabelX = Label(window, text='Num of Steps     ThermoNum       timestep/ps')
tableLabelY1 = Label(window, text='Equilibration Stage')
tableLabelY2 = Label(window, text='Solidification Stage')
tableLabelX.place(x=150, y=100)
tableLabelY1.place(x=10, y=120)
tableLabelY2.place(x=10, y=150)
# Equilibration Stage
equStepNum = StringVar(value=50000)
equThermoNum = StringVar(value=100)
equTimeStep = StringVar(value=0.003)
equStepNum = Entry(window, width=10, textvariable=equStepNum)
equThermoNum = Entry(window, width=10, textvariable=equThermoNum)
equTimeStep = Entry(window, width=10, textvariable=equTimeStep)
equStepNum.place(x=150, y=120)
equThermoNum.place(x=260, y=120)
equTimeStep.place(x=370, y=120)
# Solidification Stage
solStepNum = StringVar(value=5000000)
solThermoNum = StringVar(value=100)
solTimeStep = StringVar(value=0.001)
solStepNum = Entry(window, width=10, textvariable=solStepNum)
solThermoNum = Entry(window, width=10, textvariable=solThermoNum)
solTimeStep = Entry(window, width=10, textvariable=solTimeStep)
solStepNum.place(x=150, y=150)
solThermoNum.place(x=260, y=150)
solTimeStep.place(x=370, y=150)

# SUBMIT BUTTON
submitBtn = Button(window, text='Submit', command=submitted, width=10, height=2)
submitBtn.place(x=460, y=120)

# temp output
line2 = Label(window)
line2.place(x=10, y=300)

# Plot
if not os.path.exists(str(path)+'/plot'):
    os.makedirs(str(path)+'/plot')

# Call .py to plot
densityBtn = Button(window, text='Density-t', command=callDensity, width=10, height=2)
compositionBtn = Button(window, text='Composition-t', command=callComposition, width=10, height=2)
temperatureBtn = Button(window, text='Temperature-t', command=callTemperature, width=10, height=2)
densityBtn.place(x=10, y=200)
compositionBtn.place(x=160, y=200)
temperatureBtn.place(x=310, y=200)

window.mainloop()
