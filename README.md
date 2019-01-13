# fem-pipe
Finite-element simulation examples on hypothetical pipe geometries 
using [PyGimli](http://www.pygimli.org/), [Tetgen](http://wias-berlin.de/software/tetgen/) and [Paraview](http://www.paraview.org/). The examples were produced for demonstration purposes only.

## Example 1: 2D acoustic wave propagation
[[source](https://github.com/peberg/fem-pipe/blob/master/pipe_2D_acoustic.ipynb)].

2D pipe geometry used for acoustic forward modelling
![](figs/2d_mesh.png)

Acoustic wave propagation and signals registered at sensor locations.
![](figs/2d_div_p.gif)

## Example 2: 3D electrostatic potential
[[source](https://github.com/peberg/fem-pipe/blob/master/pipe_3D_electrostatic.ipynb)].

Electrostatic potential resulting from electric current flow in pipeline wall (current electrodes locate towards the nearest model face). It might be interesting to note that the problem of thermal conduction would be handled with the exact same partial differential equation.

Mesh             |  Electrostatic potential
:-------------------------:|:-------------------------:
![](figs/3d_geom_raw_trunc.png)  |  ![](figs/3d_output_field_trunc.png)
