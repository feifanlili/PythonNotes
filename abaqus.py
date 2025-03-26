*Heading
Dynamic Mechanical Analysis (DMA) Simulation - PU Foam

** Define Part - Rectangular Specimen (100 mm x 10 mm x 10 mm)
*Part, name=Sample
*Node
1, 0.0, 0.0, 0.0
2, 100.0, 0.0, 0.0
3, 100.0, 10.0, 0.0
4, 0.0, 10.0, 0.0
5, 0.0, 0.0, 10.0
6, 100.0, 0.0, 10.0
7, 100.0, 10.0, 10.0
8, 0.0, 10.0, 10.0

*Element, type=C3D8R
1, 1, 2, 3, 4, 5, 6, 7, 8

** Define Material Properties
*Material, name=PU_Foam
*Density
1.2e-9   **(Density in tons/mm³)
*Elastic, type=ISO
10.0E3, 0.3  **(Initial Young’s modulus and Poisson's ratio)
*Viscoelastic, Frequency
0.1, 9.5E3, 0.3E3
1.0, 9.2E3, 0.8E3
10.0, 8.5E3, 1.2E3
100.0, 7.0E3, 2.0E3

** Define Section and Assign to Part
*Solid Section, material=PU_Foam, elset=AllElements
,

** Define Assembly
*Assembly, name=Assembly
*Instance, name=SampleInstance, part=Sample
*End Instance
*End Assembly

** Define Step for Frequency Domain Analysis
*Step, name=DMA_Test, nlgeom=YES
*Steady State Dynamics, Direct
0.1, 100.0, 10
*End Step

** Define Boundary Conditions
*Boundary
1, 1, 6, 0.0  **(Fully fixed one end of the sample)

** Define Sinusoidal Loading at Free End
*Cload
2, 3, 5.0  **(Apply 5N force in z-direction for oscillation)

** Define Output Requests
*Output, field
*Node Output
U, V  **(Displacement output for amplitude phase analysis)
*End Output

** End of Input File


