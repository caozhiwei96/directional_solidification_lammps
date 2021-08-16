# Directional Solidification

In this repository, you can find the LAMMPS codes, accompanying the corresponding python codes for plotting, to study the directional solidification of alloys during additive manufacturing using molecular dynamics. 

This is an important part of Zhiwei Cao's Master's Thesis, *Directional Solidification of Alloys for Additive Manufacturing*, under the supervision of Prof. Dr. Julija Zavadlav at Professorship Multiscale Modeling of Fluid Materials at the Technical University of Munich. 

The LAMMPS input file template is `./src/in.DS`. 

An example of 304L stainless steel can be found in `./example`. 

The plot tool can be found in `./src/plot_tool`.

## Install

This project uses the following software and packages. Please make sure you installed them. 

1. [LAMMPS](https://www.lammps.org/) (necessary)
2. [Open MPI](https://www.open-mpi.org/) (necessary)
3. [python3](https://www.python.org/) (necessary)
4. [OVITO](https://www.ovito.org/) (necessary, basic version is enough)
5. [matplotlib](https://matplotlib.org/) (necessary)
6. [atomsk](https://atomsk.univ-lille.fr/) (recommended)

## Usage

1. Create simulation box. Here atomsk is used, this can also be done in LAMMPS code using `create_box` command. 

    For example, using atomsk to create a 304L stainless steel (atomic percent: Fe 70.0%, Cr 21.0%, Ni 9.0%) cubic simulation box with a side length of 30 nm: 

    ```
    atomsk --create fcc 3.56 Fe -duplicate 84 84 84 Fe_fcc.xsf
    ```
    ```
    atomsk Fe_fcc.xsf -select random 21.0% Fe -substitute Fe Cr FeCr21.cfg
    ```
    ```
    atomsk FeCr21.cfg -select random 11.40% Fe -substitute Fe Ni SS304L.cfg lmp
    ```
    
    This simulation box is very large, so it is not included in this repository. 

2. Choose EAM or MEAM potential. 

    In example, Zhou's potential for `pair_style eam/alloy` is used. This potential file is not included in this repository, please download from [IPR](https://www.ctcms.nist.gov/potentials/entry/2018--Zhou-X-W-Foster-M-E-Sills-R-B--Fe-Ni-Cr/) to `./example` and rename it as `FeNiCr.eam.alloy`. 

3. Edit LAMMPS input file. Most of the variables that need to be changed can be found in Initialization part. 

    Make sure to check the lmp file of initial simulation box for atom ID, and assign right potential to each atom. 
    
    Note that a larger number of simulation step of solidification stage (e.g. 5 ns) is recommended to ensure a full solidification. 

4. Run the simulation using MPI. Make sure simulation box file (.lmp), potential file, and input file are in the same directory. Then run the simulation.

    In example, 30 is chosen for the number of processes, as this has the highest simulation speed for the test case:

    ```
    mpirun -np 30 lmp_stable -in in.DS.SS
    ```

5. Post-process. A plot tool for this directional solidification can be found in `./src/plot_tool`, which can be run by

    ```
    python3 GUI.py
    ```

    Firstly, choose the directory of the simulation, for example `./example` here. 
    
    Then check other input parameters and press Submit button. 
    
    Next press Density-t, Composition-t, and Temperature-t buttons for corresponding plots. 
    
    Examples of these plots can be found in `./example/plot`. 
    
    
