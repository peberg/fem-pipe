# fem-pipe
FEM simulations on hypothetical pipe geometries
using [PyGimli](http://www.pygimli.org/), [Tetgen](http://wias-berlin.de/software/tetgen/) and [Paraview](http://www.paraview.org/).

## Case: 2D acoustic wave propagation
[source](https://github.com/peberg/fem-pipe/blob/master/pipe_2D_acoustic.ipynb)

2D pipe geometry used for acoustic forward modelling.
![](figs/2d_mesh.png)

Acoustic wave propagation and pressure signals registered at sensor locations.
![](figs/2d_div_p.gif)

## Case: 3D electrostatic potential
[source](https://github.com/peberg/fem-pipe/blob/master/pipe_3D_electrostatic2.ipynb)

Mesh             |  Electrical potential
:-------------------------:|:-------------------------:
![](figs/3d_geom_raw_trunc.png)  |  ![](figs/3d_output_field_trunc.png)
